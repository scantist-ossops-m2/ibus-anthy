# vim:set et sts=4 sw=4:
# -*- coding: utf-8 -*-
#
# ibus-anthy - The Anthy engine for IBus
#
# Copyright (c) 2007-2008 Peng Huang <shawn.p.huang@gmail.com>
# Copyright (c) 2007-2011 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 675 Mass Ave, Cambridge, MA 02139, USA.

import os
import sys
import getopt
import locale

from gi.repository import GObject
from gi.repository import IBus

import _config as config
import factory

class IMApp:
    def __init__(self, exec_by_ibus):
        command_line = config.LIBEXECDIR + '/ibus-engine-anthy --ibus'
        self.__component = IBus.Component(name='org.freedesktop.IBus.Anthy',
                                          description='Anthy Component',
                                          version='0.1.0',
                                          license='GPL',
                                          author='Peng Huang <shawn.p.huang@gmail.com>',
                                          homepage='http://code.google.com/p/ibus/',
                                          command_line=command_line,
                                          textdomain='ibus-anthy')
        engine = IBus.EngineDesc(name='anthy',
                                 longname='anthy',
                                 description='Japanese Anthy',
                                 language='ja',
                                 license='GPL',
                                 author='Peng Huang <shawn.p.huang@gmail.com>',
                                 icon='ibus-anthy',
                                 layout='en')
        self.__component.add_engine(engine)
        self.__mainloop = GObject.MainLoop()
        self.__bus = IBus.Bus()
        self.__bus.connect('disconnected', self.__bus_disconnected_cb)
        self.__factory = factory.EngineFactory(self.__bus)
        if exec_by_ibus:
            self.__bus.request_name('org.freedesktop.IBus.Anthy', 0)
        else:
            self.__bus.register_component(self.__component)

    def run(self):
        self.__mainloop.run()

    def __bus_disconnected_cb(self, bus):
        self.__mainloop.quit()


def launch_engine(exec_by_ibus):
    IMApp(exec_by_ibus).run()

def print_help(out, v = 0):
    print >> out, '-i, --ibus             executed by ibus.'
    print >> out, '-h, --help             show this message.'
    print >> out, '-d, --daemonize        daemonize ibus.'
    sys.exit(v)

def main():
    try:
        locale.setlocale(locale.LC_ALL, '')
    except:
        pass

    exec_by_ibus = False
    daemonize = False

    shortopt = 'ihd'
    longopt = ['ibus', 'helpn', 'daemonize']

    try:
        opts, args = getopt.getopt(sys.argv[1:], shortopt, longopt)
    except getopt.GetoptError, err:
        print_help(sys.stderr, 1)

    for o, a in opts:
        if o in ('-h', '--help'):
            print_help(sys.stdout)
        elif o in ('-d', '--daemonize'):
            daemonize = True
        elif o in ('-i', '--ibus'):
            exec_by_ibus = True
        else:
            print >> sys.stderr, 'Unknown argument: %s' % o
            print_help(sys.stderr, 1)

    if daemonize:
        if os.fork():
            sys.exit()

    launch_engine(exec_by_ibus)

if __name__ == '__main__':
    main()
