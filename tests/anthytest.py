#!/usr/bin/python3

from gi import require_version as gi_require_version
gi_require_version('GLib', '2.0')
gi_require_version('Gtk', '3.0')
gi_require_version('IBus', '1.0')
from gi.repository import GLib
from gi.repository import Gtk
from gi.repository import IBus

import sys

sys.path.append('/usr/share/ibus-anthy/engine')
import engine

from anthycases import TestCases

class AnthyTest:
    ENGINE_PATH = '/com/redhat/IBus/engines/Anthy/Test/Engine'
    def __init__(self):
        IBus.init()
        self.__id = 0
        self.__rerun = False
        self.__test_index = 0
        self.__preedit_test_index = -1

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
        desc = IBus.EngineDesc(name='testanthy',
                                 longname='TestAnthy',
                                 description='Test Anthy Input Method',
                                 language='ja',
                                 license='GPL',
                                 author='Takao Fujiwara <takao.fujiwara1@gmail.com>',
                                 icon='ibus-anthy',
                                 symbol=chr(0x3042),
                                 )
        self.__component.add_engine(desc)
        self.__bus.register_component(self.__component)
        self.__bus.request_name('org.freedesktop.IBus.Anthy.Test', 0)
        return True

    def __name_owner_changed_cb(self, connection, sender_name, object_path,
                                interface_name, signal_name, parameters,
                                user_data):
        print('test ' + signal_name)
        if signal_name == 'NameOwnerChanged':
            engine.Engine.CONFIG_RELOADED(self.__bus)

    def __create_engine_cb(self, factory, engine_name):
        if engine_name == 'testanthy':
            self.__id += 1
            self.__engine = engine.Engine(self.__bus, '%s/%d' % (self.ENGINE_PATH, self.__id))
            self.__engine.connect('focus-in', self.__engine_focus_in)
            self.__engine.connect('focus-out', self.__engine_focus_out)
            return self.__engine

    def __engine_focus_in(self, engine):
        if self.__test_index == len(TestCases['tests']):
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
        window = Gtk.Window(Gtk.WindowType.TOPLEVEL)
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

    def __entry_preedit_changed_cb(self, entry, preedit_str):
        if self.__test_index == len(TestCases['tests']):
            return
        if self.__preedit_test_index == self.__test_index:
            return
        self.__preedit_test_index = self.__test_index
        self.__run_cases('conversion', 1)
        self.__run_cases('commit')

    def __enable_hiragana(self):
        key = TestCases['init']
        self.__typing(key[0], key[1], key[2])
        #self.__typing(ord(' '), 0, IBus.ModifierType.CONTROL_MASK)
        #self.__typing(IBus.KEY_Escape, 0, IBus.ModifierType.MOD1_MASK)

    def __main_test(self):
        self.__run_cases('preedit')
        self.__run_cases('conversion', 0, 1)

    def __run_cases(self, tag, start=-1, end=-1):
        print('test', self.__test_index, tag)
        tests = TestCases['tests'][self.__test_index]
        if tests == None:
            return
        cases = tests[tag]
        type = list(cases.keys())[0]
        i = 0
        if type == 'string':
            for a in cases['string']:
                if start >= 0 and i < start:
                    i += 1
                    continue
                if end >= 0 and i >= end:
                    break;
                print(a)
                self.__typing(ord(a), 0, 0)
                i += 1
        if type == 'keys':
            for key in cases['keys']:
                if start >= 0 and i < start:
                    i += 1
                    continue
                if end >= 0 and i >= end:
                    break;
                print(self.__test_index, tag, key, cases['keys'])
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
            return
        self.__entry.set_text('')
        self.__main_test()

    def run(self):
        Gtk.main()

def main():
    EngineTest = AnthyTest()
    if not EngineTest.register_ibus_engine():
        return -1;
    EngineTest.create_window()
    EngineTest.run()

if __name__ == '__main__':
    main()
