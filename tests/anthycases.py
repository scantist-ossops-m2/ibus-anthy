# 'init' has one array which is [keysym, keycode, modifier] and to be run
# before the main tests. E.g.
# Ctrl-space to enable Hiragana mode
#
# 'tests' cases are the main test cases.
# 'preedit' case runs to create a preedit text.
# 'commit' case runs to commit the preedit text.
# 'result' case is the expected output.
# 'preedit' and 'commit' can choose the type of either 'string' or 'keys'
# 'string' type is a string sequence which does not need modifiers

from gi import require_version as gi_require_version
gi_require_version('IBus', '1.0')
from gi.repository import IBus

TestCases = {
    #'init': [ord(' '), 0, IBus.ModifierType.CONTROL_MASK]
    'init': [IBus.KEY_Escape, 0, IBus.ModifierType.MOD1_MASK],
    'tests': [
                { 'preedit': { 'string': 'watashinonamaeha,pendesu.' },
                  'conversion': { 'string': ' '  },
                  'commit': { 'keys': [[IBus.KEY_Return, 0, 0]] },
                  'result': { 'string': '私の名前は、ペンです。' }
                },

                { 'preedit': { 'string': 'toukyo' },
                  'conversion': { 'keys': [[IBus.KEY_Tab, 0, 0],
                                           [IBus.KEY_Tab, 0, 0],
                                          ]
                                },
                  'commit': { 'keys': [[IBus.KEY_Return, 0, 0]] },
                  'result': { 'string': '東京' }
                },
             ]

}
