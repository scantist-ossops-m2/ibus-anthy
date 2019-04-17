#!/usr/bin/python3
# -*- coding: utf-8 -*-

from __future__ import print_function

from gi import require_version as gi_require_version
gi_require_version('GLib', '2.0')
gi_require_version('Gtk', '3.0')
gi_require_version('IBus', '1.0')
from gi.repository import GLib
from gi.repository import Gtk
from gi.repository import IBus

import getopt
import os
import sys
import subprocess

PY3K = sys.version_info >= (3, 0)
DONE_EXIT = False

if 'IBUS_ANTHY_ENGINE_PATH' in os.environ:
    engine_path = os.environ['IBUS_ANTHY_ENGINE_PATH']
    if engine_path != None and engine_path != '':
        sys.path.append(engine_path)
if 'IBUS_ANTHY_SETUP_PATH' in os.environ:
    setup_path = os.environ['IBUS_ANTHY_SETUP_PATH']
    if setup_path != None and setup_path != '':
        sys.path.append(setup_path)
sys.path.append('/usr/share/ibus-anthy/engine')

from anthycases import TestCases

class AnthyTest:
    global DONE_EXIT
    ENGINE_PATH = '/com/redhat/IBus/engines/Anthy/Test/Engine'
    def __init__(self):
        IBus.init()
        self.__id = 0
        self.__rerun = False
        self.__test_index = 0
        self.__conversion_index = 0
        self.__commit_done = False

    def register_ibus_engine(self):
        self.__bus = IBus.Bus()
        if not self.__bus.is_connected():
            error('ibus-daemon is not running')
            return False;
        self.__bus.get_connection().signal_subscribe('org.freedesktop.DBus',
                                              'org.freedesktop.DBus',
                                              'NameOwnerChanged',
                                              '/org/freedesktop/DBus',
                                              None,
                                              0,
                                              self.__name_owner_changed_cb,
                                              self.__bus)
        #self.__factory = factory.EngineFactory(self.__bus)
        self.__factory = IBus.Factory(
                object_path=IBus.PATH_FACTORY,
                connection=self.__bus.get_connection())
        self.__factory.connect('create-engine', self.__create_engine_cb)
        #command_line = '/usr/libexec/ibus-engine-anthy'
        self.__component = IBus.Component(name='org.freedesktop.IBus.Anthy.Test',
                                          description='Test Anthy Component',
                                          version='0.0.1',
                                          license='GPL',
                                          author='Takao Fujiwara <takao.fujiwara1@gmail.com>',
                                          homepage='https://github.com/ibus/ibus/wiki',
                                          command_line='',
                                          textdomain='ibus-anthy')
        if PY3K:
            symbol = chr(0x3042)
        else:
            symbol = unichr(0x3042)
        desc = IBus.EngineDesc(name='testanthy',
                                 longname='TestAnthy',
                                 description='Test Anthy Input Method',
                                 language='ja',
                                 license='GPL',
                                 author='Takao Fujiwara <takao.fujiwara1@gmail.com>',
                                 icon='ibus-anthy',
                                 symbol=symbol,
                                 )
        self.__component.add_engine(desc)
        self.__bus.register_component(self.__component)
        self.__bus.request_name('org.freedesktop.IBus.Anthy.Test', 0)
        return True

    def __name_owner_changed_cb(self, connection, sender_name, object_path,
                                interface_name, signal_name, parameters,
                                user_data):
        if signal_name == 'NameOwnerChanged':
            import engine
            engine.Engine.CONFIG_RELOADED()

    def __create_engine_cb(self, factory, engine_name):
        if engine_name == 'testanthy':
            import engine
            self.__id += 1
            self.__engine = engine.Engine(self.__bus, '%s/%d' % (self.ENGINE_PATH, self.__id))
            self.__engine.connect('focus-in', self.__engine_focus_in)
            self.__engine.connect('focus-out', self.__engine_focus_out)
            return self.__engine

    def __engine_focus_in(self, engine):
        if self.__test_index == len(TestCases['tests']):
            if DONE_EXIT:
                Gtk.main_quit()
            return
        # Workaround because focus-out resets the preedit text
        # ibus_bus_set_global_engine() calls bus_input_context_set_engine()
        # twice and it causes bus_engine_proxy_focus_out()
        if self.__rerun:
            self.__main_test()
        pass

    def __engine_focus_out(self, engine):
        self.__rerun = True

    def create_window(self):
        window = Gtk.Window(type = Gtk.WindowType.TOPLEVEL)
        self.__entry = entry = Gtk.Entry()
        window.connect('destroy', Gtk.main_quit)
        entry.connect('focus-in-event', self.__entry_focus_in_event_cb)
        entry.connect('preedit-changed', self.__entry_preedit_changed_cb)
        buffer = entry.get_buffer()
        buffer.connect('inserted-text', self.__buffer_inserted_text_cb)
        window.add(entry)
        window.show_all()

    def __entry_focus_in_event_cb(self, entry, event):
        if self.__test_index == len(TestCases['tests']):
            if DONE_EXIT:
                Gtk.main_quit()
            return False
        self.__bus.set_global_engine_async('testanthy', -1, None, self.__set_engine_cb)
        return False

    def __set_engine_cb(self, object, res):
        if not self.__bus.set_global_engine_async_finish(res):
            warning('set engine failed: ' + error.message)
            return
        print('enabled engine')
        self.__enable_hiragana()
        self.__main_test()

    def __get_test_condition_length(self, tag):
        tests = TestCases['tests'][self.__test_index]
        cases = tests[tag]
        type = list(cases.keys())[0]
        return len(cases[type])

    def __entry_preedit_changed_cb(self, entry, preedit_str):
        if len(preedit_str) == 0:
            return
        if self.__test_index == len(TestCases['tests']):
            if DONE_EXIT:
                Gtk.main_quit()
            return
        conversion_length = self.__get_test_condition_length('conversion')
        # Need to return again even if all the conversion is finished
        # until the final Engine.update_preedit() is called.
        if self.__conversion_index > conversion_length:
            return
        self.__run_cases('conversion',
                         self.__conversion_index,
                         self.__conversion_index + 1)
        if self.__conversion_index < conversion_length:
            self.__conversion_index += 1
            return
        self.__conversion_index += 1
        self.__run_cases('commit')

    def __enable_hiragana(self):
        commands = ['dconf', 'read',
                    '/desktop/ibus/engine/anthy/common/input-mode'
                   ]
        if PY3K:
            py3result = subprocess.run(commands, stdout=subprocess.PIPE)
            try:
                result = int(py3result.stdout)
            except ValueError:
                # No user data
                result = 0
        else:
            py2result = subprocess.check_output(commands)
            result = py2result
            if result == '':
                result = 0
        if result != 0:
            print('Enable hiragana', result)
            key = TestCases['init']
            self.__typing(key[0], key[1], key[2])
        else:
            print('Already hiragana')

    def __main_test(self):
        self.__conversion_index = 0
        self.__commit_done = False
        self.__run_cases('preedit')
        self.__run_cases('conversion',
                         self.__conversion_index,
                         self.__conversion_index + 1)
        self.__conversion_index += 1

    def __run_cases(self, tag, start=-1, end=-1):
        tests = TestCases['tests'][self.__test_index]
        if tests == None:
            return
        cases = tests[tag]
        type = list(cases.keys())[0]
        i = 0
        if type == 'string':
            if start == -1 and end == -1:
                print('test step:', tag, 'sequences: "' + cases['string'] + '"')
            for a in cases['string']:
                if start >= 0 and i < start:
                    i += 1
                    continue
                if end >= 0 and i >= end:
                    break;
                if start != -1 or end != -1:
                    print('test step:', tag, 'sequences: "' + cases['string'][i] + '"')
                self.__typing(ord(a), 0, 0)
                i += 1
        if type == 'keys':
            if start == -1 and end == -1:
                print('test step:', tag, 'sequences:', cases['keys'])
            for key in cases['keys']:
                if start >= 0 and i < start:
                    i += 1
                    continue
                if end >= 0 and i >= end:
                    break;
                if start != -1 or end != -1:
                    print('test step: %s sequences: [0x%X, 0x%X, 0x%X]' % (tag, key[0], key[1],  key[2]))
                self.__typing(key[0], key[1], key[2])
                i += 1

    def __typing(self, keyval, keycode, modifiers):
        self.__engine.emit('process-key-event', keyval, keycode, modifiers)
        modifiers |= IBus.ModifierType.RELEASE_MASK;
        self.__engine.emit('process-key-event', keyval, keycode, modifiers)

    def __buffer_inserted_text_cb(self, buffer, position, chars, nchars):
        tests = TestCases['tests'][self.__test_index]
        cases = tests['result']
        if cases['string'] == chars:
            print("OK: ", chars)
        else:
            print("NG: ", cases['string'], chars)
        self.__test_index += 1
        if self.__test_index == len(TestCases['tests']):
            if DONE_EXIT:
                Gtk.main_quit()
            return
        self.__entry.set_text('')
        self.__main_test()

    def run(self):
        Gtk.main()

def print_help(out, v = 0):
    print('-e, --exit             Exit this program after test is done.',
          file=out)
    print('-f, --force            Run this program forcibly with .anthy.',
          file=out)
    print('-h, --help             show this message.', file=out)
    print('\nenvironment variables:', file=out)
    print('IBUS_ANTHY_ENGINE_PATH Indicates the path which includes ' \
          'engine.py. the default is /usr/share/ibus-anthy/engine', file=out)
    print('IBUS_ANTHY_SETUP_PATH  Indicates the path which includes ' \
          'prefs.py. the default is /usr/share/ibus-anthy/setup', file=out)
    sys.exit(v)

def get_userhome():
    if 'HOME' not in os.environ:
        import pwd
        userhome = pwd.getpwuid(os.getuid()).pw_dir
    else:
        userhome = os.environ['HOME']
    userhome = userhome.rstrip('/')
    return userhome

def main():
    shortopt = 'efh'
    longopt = ['exit', 'force', 'help']
    force_run = False
    try:
        opts, args = getopt.getopt(sys.argv[1:], shortopt, longopt)
    except getopt.GetoptError as err:
        print_help(sys.stderr, 1)

    for o, a in opts:
        if o in ('-e', '--exit'):
            global DONE_EXIT
            DONE_EXIT = True
        elif o in ('-f', '--force'):
            force_run = True
        elif o in ('-h', '--help'):
            print_help(sys.stderr)
        else:
            print('Unknown argument: %s' % o, file=sys.stderr)
            print_help(sys.stderr, 1)

    for anthy_config in ['/.config/anthy', '/.anthy']:
        anthy_user_dir = get_userhome() + anthy_config
        anthy_last_file = anthy_user_dir + '/last-record2_default.utf8'
        if os.path.exists(anthy_last_file) and not force_run:
            print('Please remove %s before the test' % anthy_last_file,
                  file=sys.stderr)
            sys.exit(-1)
    EngineTest = AnthyTest()
    if not EngineTest.register_ibus_engine():
        sys.exit(-1)
    EngineTest.create_window()
    EngineTest.run()

if __name__ == '__main__':
    main()
