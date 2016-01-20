# vim:set noet ts=4:
#
# ibus-anthy - The Anthy engine for IBus
#
# Copyright (c) 2007-2008 Peng Huang <shawn.p.huang@gmail.com>
# Copyright (c) 2010-2016 Takao Fujiwara <takao.fujiwara1@gmail.com>
# Copyright (c) 2007-2016 Red Hat, Inc.
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

SUBDIRS = \
	m4 \
	po \
	data \
	gir \
	engine \
	icons \
	setup \
	$(NULL)

ACLOCAL_AMFLAGS = -I m4

EXTRA_DIST = \
	autogen.sh \
	ibus-anthy.spec.in \
	python-config.py \
	$(NULL)

noinst_DIST = \
	$(NULL)


DISTCLEANFILES = \
	po/stamp-it \
	$(NULL)

dist-hook:
	if test -d .git ; then \
		git log --name-status --date=iso > $(distdir)/ChangeLog ; \
		PREV_MICRO_VERSION=`expr $(PACKAGE_VERSION_MICRO) - 1`; \
		PREV_VERSION=\
"$(PACKAGE_VERSION_MAJOR).$(PACKAGE_VERSION_MINOR).$$PREV_MICRO_VERSION"; \
		echo "Changes in $(PACKAGE_NAME) $(PACKAGE_VERSION)" \
		        > $(distdir)/NEWS; \
		echo "" >> $(distdir)/NEWS; \
		git log $$PREV_VERSION...$(PACKAGE_VERSION) --reverse \
		        --pretty=format:'%s (%an) %h' >> $(distdir)/NEWS; \
	fi

rpm: dist @PACKAGE_NAME@.spec
	rpmbuild -bb \
			--define "_sourcedir `pwd`" \
			--define "_builddir `pwd`" \
			--define "_srcrpmdir `pwd`" \
			--define "_rpmdir `pwd`" \
			--define "_specdir `pwd`" \
			@PACKAGE_NAME@.spec

srpm: dist @PACKAGE_NAME@.spec
	rpmbuild -bs \
			--define "_sourcedir `pwd`" \
			--define "_builddir `pwd`" \
			--define "_srcrpmdir `pwd`" \
			--define "_rpmdir `pwd`" \
			--define "_specdir `pwd`" \
			@PACKAGE_NAME@.spec

clean-rpm:
	$(RM) -r "`uname -i`"

clean-local: clean-rpm
