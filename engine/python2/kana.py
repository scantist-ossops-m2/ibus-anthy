# vim:set et sts=4 sw=4:
# -*- coding: utf-8 -*-
#
# ibus-anthy - The Anthy engine for IBus
#
# Copyright (c) 2007-2008 Peng Huang <shawn.p.huang@gmail.com>
# Copyright (c) 2010-2013 Takao Fujiwara <takao.fujiwara1@gmail.com>
# Copyright (c) 2007-2013 Red Hat, Inc.
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import sys

from tables import *
import segment

_UNFINISHED_HIRAGANA = set(u'かきくけこさしすせそたちつてとはひふへほ')

class KanaSegment(segment.Segment):
    _prefs = None
    _kana_typing_rule_section = None
    _kana_voiced_consonant_rule = None

    def __init__(self, enchars=u'', jachars=u''):
        if not jachars:
            jachars = self.__get_kana_typing_rule(enchars, u'')
        super(KanaSegment, self).__init__(enchars, jachars)

    @classmethod
    def INIT_KANA_TYPING_RULE(cls, prefs):
        cls._prefs = prefs
        if prefs == None:
            cls._kana_typing_rule_section = None
            return
        if cls._kana_typing_rule_section == None:
            cls._init_kana_typing_method()
        if cls._kana_voiced_consonant_rule == None and \
           cls._kana_typing_rule_section != None:
            cls._init_kana_voiced_consonant_rule()

    @classmethod
    def _init_kana_typing_method(cls, method=None):
        prefs = cls._prefs
        if method == None:
            method = prefs.get_value('kana_typing_rule', 'method')
        if method == None:
            method = 'jp'
        cls._kana_typing_rule_section = 'kana_typing_rule/' + method
        if cls._kana_typing_rule_section not in prefs.sections():
            cls._kana_typing_rule_section = None

    @classmethod
    def _init_kana_voiced_consonant_rule(cls):
        prefs = cls._prefs
        # Create kana_voiced_consonant_rule dynamically.
        # E.g. 't' + '@' on jp kbd becomes Hiragana GA
        # 't' + '[' on us kbd becomes Hiragana GA
        # If the customized table provides U+309b with other chars,
        # it needs to be detected dynamically.
        cls._kana_voiced_consonant_rule = {}
        section = cls._kana_typing_rule_section
        for gkey in prefs.keys(section):
            value = prefs.get_value(section, gkey)
            key = prefs.typing_from_config_key(gkey)
            if key == '':
                continue
            if value == unichr(0x309b).encode('utf-8'):
                for no_voiced, voiced in \
                        kana_voiced_consonant_no_rule.items():
                    rule = no_voiced + key.decode('utf-8')
                    cls._kana_voiced_consonant_rule[rule] = voiced
            if value == unichr(0x309c).encode('utf-8'):
                for no_voiced, voiced in \
                        kana_semi_voiced_consonant_no_rule.items():
                    rule = no_voiced + key.decode('utf-8')
                    cls._kana_voiced_consonant_rule[rule] = voiced

    @classmethod
    def RESET(cls, prefs, section, name, value):
        cls._prefs = prefs
        if section == 'kana_typing_rule' and name == 'method' and \
           value != None:
            cls._kana_typing_rule_section = None
            cls._kana_voiced_consonant_rule = None
            cls._init_kana_typing_method(value)
        elif section.startswith('kana_typing_rule/'):
            # Probably it's better to restart ibus by manual
            # instead of saving the emitted values from config.
            cls._kana_voiced_consonant_rule = None

    def __get_kana_typing_rule(self, enchars, retval=None):
        prefs = self._prefs
        value = None
        section = self._kana_typing_rule_section
        if section != None:
            # Need to send Unicode to typing_to_config_key instead of UTF-8
            # not to separate U+A5
            gkey = prefs.typing_to_config_key(enchars)
            if gkey == '':
                return None
            enchars = gkey
            if enchars in prefs.keys(section):
                value = prefs.unicode(prefs.str(prefs.get_value(section, enchars)))
            else:
                prefs.set_no_key_warning(True)
                value = prefs.get_value_direct(section, enchars)
                prefs.set_no_key_warning(False)
                if value != None:
                    value = prefs.unicode(prefs.str(value))
            if value == '':
                value = None
            if value == None:
                value = retval 
        else:
            value = kana_typing_rule_static.get(enchars, retval)
        return value

    def is_finished(self):
        return not (self._jachars in _UNFINISHED_HIRAGANA)

    def append(self, enchar):
        if enchar == u'\0' or enchar == u'':
            return []
        if self._jachars:
            text = self._jachars + enchar
            if self._kana_voiced_consonant_rule != None:
                jachars = self._kana_voiced_consonant_rule.get(text, None)
            if jachars:
                self._enchars = self._enchars + enchar
                self._jachars = jachars
                return []
            return [KanaSegment(enchar)]
        self._enchars = self._enchars + enchar
        self._jachars = self.__get_kana_typing_rule(self._enchars, u'')
        return []

    def prepend(self, enchar):
        if enchar == u'\0' or enchar == u'':
            return []
        if self._enchars == u'':
            self._enchars = enchar
            self._jachars = self.__get_kana_typing_rule(self._enchars, u'')
            return []
        return [KanaSegment(enchar)]

    def pop(self, index=-1):
        if index == -1:
            index = len(self._enchars) - 1
        if index < 0 or index >= len(self._enchars):
            raise IndexError('Out of bound')
        if self.is_finished():
            self._enchars = u''
            self._jachars = u''
        else:
            enchars = list(self._enchars)
            del enchars[index]
            self._enchars = u''.join(enchars)
            self._jachars = self.__get_kana_typing_rule(self._enchars, u'')
