#!/usr/bin/python

# Finally decided to import anthy zipcode.t with UTF-8 into ibus-anthy
# because if digits without hyphen is grepped by engine, it could cause
# the timeout issue. If digits without hyphen are sent to anthy,
# digits with hyphen also need to be sent to anthy so the lookup could
# include too many and unnecessary candidates.
# Also wish to install the filename of 'zipcode.t' to simplify enigne.

# for python2
from __future__ import print_function

import codecs
import sys

if len(sys.argv) < 2:
    print('usage: %s /usr/share/anthy/zipcode.t' % sys.argv[0],
          file=sys.stderr)
    exit(-1)

anthy_zipfile = sys.argv[1]

try:
    contents = codecs.open(anthy_zipfile, 'r', 'euc_jp').read()
except UnicodeDecodeError as e:
    print('Your file is not eucJP? %s' % anthy_zipfile, file=sys.stderr)
    contents = open(anthy_zipfile).read()

output_zipfile = codecs.open('zipcode.t', 'w', 'utf-8')
output_zipfile.write('# copied %s with UTF-8.\n#\n' % anthy_zipfile)

for line in contents.split('\n'):
    if len(line) == 0 or line[0] == '#':
        output_zipfile.write('%s\n' % line)
        continue

    words = line.split()
    if len(words) < 3:
        continue

    if len(words[0]) < 1 or ord(words[0][0]) > 0xff:
        mbcs_addr = words[0]
    else:
        uni_addr = ''
        i = 0
        for word in words[0]:
            # Convert ASCII number char to wide number char.
            if sys.version < '3':
                uni_addr += unichr(0xfee0 + ord(word))
            else:
                uni_addr += chr(0xfee0 + ord(word))
            if i == 2:
                # Insert wide hyphen
                if sys.version < '3':
                    uni_addr += unichr(0x30fc)
                else:
                    uni_addr += chr(0x30fc)
            i += 1
        mbcs_addr = uni_addr

    output_zipfile.write('%s %s %s\n' % \
            (mbcs_addr, '#T35*500', words[2]))

output_zipfile.flush()
output_zipfile.close()
