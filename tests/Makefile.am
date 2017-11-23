# vim:set noet ts=4:
#
# ibus-anthy - The Anthy engine for IBus
#
# Copyright (c) 2017 Takao Fujiwara <takao.fujiwara1@gmail.com>
# Copyright (c) 2017 Red Hat, Inc.
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

check:
	ARGS="--exit";                                                  \
	if test x$(FORCE_TEST) != x ; then                              \
	    ARGS="$$ARGS --force";                                      \
	fi;                                                             \
	ibus-daemon --daemonize --verbose;                              \
	sleep 1;                                                        \
	ps -ef | grep $$USER | grep ibus | grep -v grep;                \
	echo "#### Starting Python3 API test $$ARGS";                   \
	env IBUS_ANTHY_ENGINE_PATH=$(srcdir)/../engine/python3          \
	    IBUS_ANTHY_SETUP_PATH=$(srcdir)/../setup/python3            \
	python3 $(srcdir)/anthytest.py $$ARGS;                          \
	if test $$? -ne 0 ; then                                        \
	    exit -1;                                                    \
	fi;                                                             \
	if test x$(FORCE_TEST) = x ; then                               \
	    rm -r $$HOME/.anthy;                                        \
	fi;                                                             \
	echo "#### Starting Python2 API test";                          \
	env IBUS_ANTHY_ENGINE_PATH=$(srcdir)/../engine/python2          \
	    IBUS_ANTHY_SETUP_PATH=$(srcdir)/../setup/python2            \
	python2 $(srcdir)/anthytest.py $$ARGS;
	ibus exit

EXTRA_DIST = \
        anthycases.py \
        anthytest.py \
        $(NULL)
