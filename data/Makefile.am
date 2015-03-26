# vim:set noet ts=4:
#
# ibus-anthy - The Anthy engine for IBus
#
# Copyright (c) 2010-2015 Takao Fujiwara <takao.fujiwara1@gmail.com>
# Copyright (c) 2010-2015 Red Hat, Inc.
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

dicts_DATA = \
	emoji.t \
	era.t \
	oldchar.t \
	symbol.t \
	$(NULL)

dictsdir = $(pkgdatadir)/dicts

appdata_in_files = anthy.appdata.xml.in
appdata_DATA = $(appdata_in_files:.xml.in=.xml)
appdatadir=$(datadir)/appdata

$(appdata_DATA): $(appdata_in_files) Makefile
	$(AM_V_GEN) sed \
	        -e "s|_summary|summary|g" \
	        -e "s|_description|description|g" \
	        $< > $@.tmp && mv $@.tmp $@

CLEANFILES = $(appdata_DATA)

if ENABLE_ZIPCODE
dicts_DATA += zipcode.t

zipcode.t: $(ANTHY_ZIPCODE_FILE)
	$(PYTHON) zipcode-textdic.py $<

CLEANFILES += zipcode.t
endif

EXTRA_DIST = \
        $(appdata_in_files) \
        emoji.t \
        era.t \
        oldchar.t \
        symbol.t \
        zipcode-textdic.py \
        $(NULL)
