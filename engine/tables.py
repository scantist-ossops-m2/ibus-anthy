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

# string, result, cont
romaji_typing_rule_static = {
    u"-" : u"ー",
    u"a" : u"あ",
    u"i" : u"い",
    u"u" : u"う",
    u"e" : u"え",
    u"o" : u"お",
    u"xa" : u"ぁ",
    u"xi" : u"ぃ",
    u"xu" : u"ぅ",
    u"xe" : u"ぇ",
    u"xo" : u"ぉ",
    u"la" : u"ぁ",
    u"li" : u"ぃ",
    u"lu" : u"ぅ",
    u"le" : u"ぇ",
    u"lo" : u"ぉ",
    u"wha" : u"うぁ",
    u"whi" : u"うぃ",
    u"whe" : u"うぇ",
    u"who" : u"うぉ",
    u"va" : u"ヴぁ",
    u"vi" : u"ヴぃ",
    u"vu" : u"ヴ",
    u"ve" : u"ヴぇ",
    u"vo" : u"ヴぉ",
    u"ka" : u"か",
    u"ki" : u"き",
    u"ku" : u"く",
    u"ke" : u"け",
    u"ko" : u"こ",
    u"lka" : u"ヵ",
    u"lke" : u"ヶ",
#    u"xka" : u"ゕ",
    u"xka" : u"ヵ",
#    u"xke" : u"ゖ",
    u"xke" : u"ヶ",
    u"ga" : u"が",
    u"gi" : u"ぎ",
    u"gu" : u"ぐ",
    u"ge" : u"げ",
    u"go" : u"ご",
    u"kya" : u"きゃ",
    u"kyi" : u"きぃ",
    u"kyu" : u"きゅ",
    u"kye" : u"きぇ",
    u"kyo" : u"きょ",
    u"kwa" : u"くぁ",
    u"gya" : u"ぎゃ",
    u"gyi" : u"ぎぃ",
    u"gyu" : u"ぎゅ",
    u"gye" : u"ぎぇ",
    u"gyo" : u"ぎょ",
    u"gwa" : u"ぐぁ",
    u"sa" : u"さ",
    u"si" : u"し",
    u"su" : u"す",
    u"se" : u"せ",
    u"so" : u"そ",
    u"za" : u"ざ",
    u"zi" : u"じ",
    u"zu" : u"ず",
    u"ze" : u"ぜ",
    u"zo" : u"ぞ",
    u"sya" : u"しゃ",
    u"syi" : u"しぃ",
    u"syu" : u"しゅ",
    u"sye" : u"しぇ",
    u"syo" : u"しょ",
    u"sha" : u"しゃ",
    u"shi" : u"し",
    u"shu" : u"しゅ",
    u"she" : u"しぇ",
    u"sho" : u"しょ",
    u"zya" : u"じゃ",
    u"zyi" : u"じぃ",
    u"zyu" : u"じゅ",
    u"zye" : u"じぇ",
    u"zyo" : u"じょ",
    u"ja" : u"じゃ",
    u"jya" : u"じゃ",
    u"ji" : u"じ",
    u"jyi" : u"じぃ",
    u"ju" : u"じゅ",
    u"jyu" : u"じゅ",
    u"je" : u"じぇ",
    u"jye" : u"じぇ",
    u"jo" : u"じょ",
    u"jyo" : u"じょ",
    u"ta" : u"た",
    u"ti" : u"ち",
    u"tu" : u"つ",
    u"tsu" : u"つ",
    u"te" : u"て",
    u"to" : u"と",
    u"da" : u"だ",
    u"di" : u"ぢ",
    u"du" : u"づ",
    u"de" : u"で",
    u"do" : u"ど",
    u"xtu" : u"っ",
    u"xtsu" : u"っ",
    u"ltu" : u"っ",
    u"ltsu" : u"っ",
    u"tya" : u"ちゃ",
    u"tyi" : u"ちぃ",
    u"tyu" : u"ちゅ",
    u"tye" : u"ちぇ",
    u"tyo" : u"ちょ",
    u"cya" : u"ちゃ",
    u"cyi" : u"ちぃ",
    u"cyu" : u"ちゅ",
    u"cye" : u"ちぇ",
    u"cyo" : u"ちょ",
    u"cha" : u"ちゃ",
    u"chi" : u"ち",
    u"chu" : u"ちゅ",
    u"che" : u"ちぇ",
    u"cho" : u"ちょ",
    u"dya" : u"ぢゃ",
    u"dyi" : u"ぢぃ",
    u"dyu" : u"ぢゅ",
    u"dye" : u"ぢぇ",
    u"dyo" : u"ぢょ",
    u"tsa" : u"つぁ",
    u"tsi" : u"つぃ",
    u"tse" : u"つぇ",
    u"tso" : u"つぉ",
    u"tha" : u"てゃ",
    u"thi" : u"てぃ",
    u"thu" : u"てゅ",
    u"the" : u"てぇ",
    u"tho" : u"てょ",
    u"twu" : u"とぅ",
    u"dha" : u"でゃ",
    u"dhi" : u"でぃ",
    u"dhu" : u"でゅ",
    u"dhe" : u"でぇ",
    u"dho" : u"でょ",
    u"dwu" : u"どぅ",
    u"na" : u"な",
    u"ni" : u"に",
    u"nu" : u"ぬ",
    u"ne" : u"ね",
    u"no" : u"の",
    u"nya" : u"にゃ",
    u"nyi" : u"にぃ",
    u"nyu" : u"にゅ",
    u"nye" : u"にぇ",
    u"nyo" : u"にょ",
    u"ha" : u"は",
    u"hi" : u"ひ",
    u"hu" : u"ふ",
    u"he" : u"へ",
    u"ho" : u"ほ",
    u"ba" : u"ば",
    u"bi" : u"び",
    u"bu" : u"ぶ",
    u"be" : u"べ",
    u"bo" : u"ぼ",
    u"pa" : u"ぱ",
    u"pi" : u"ぴ",
    u"pu" : u"ぷ",
    u"pe" : u"ぺ",
    u"po" : u"ぽ",
    u"hya" : u"ひゃ",
    u"hyi" : u"ひぃ",
    u"hyu" : u"ひゅ",
    u"hye" : u"ひぇ",
    u"hyo" : u"ひょ",
    u"bya" : u"びゃ",
    u"byi" : u"びぃ",
    u"byu" : u"びゅ",
    u"bye" : u"びぇ",
    u"byo" : u"びょ",
    u"pya" : u"ぴゃ",
    u"pyi" : u"ぴぃ",
    u"pyu" : u"ぴゅ",
    u"pye" : u"ぴぇ",
    u"pyo" : u"ぴょ",
    u"fa" : u"ふぁ",
    u"fi" : u"ふぃ",
    u"fu" : u"ふ",
    u"fe" : u"ふぇ",
    u"fo" : u"ふぉ",
    u"fya" : u"ふゃ",
    u"fyi" : u"ふぃ",
    u"fyu" : u"ふゅ",
    u"fye" : u"ふぇ",
    u"fyo" : u"ふょ",
    u"ma" : u"ま",
    u"mi" : u"み",
    u"mu" : u"む",
    u"me" : u"め",
    u"mo" : u"も",
    u"mya" : u"みゃ",
    u"myi" : u"みぃ",
    u"myu" : u"みゅ",
    u"mye" : u"みぇ",
    u"myo" : u"みょ",
    u"ya" : u"や",
    u"yi" : u"い",
    u"yu" : u"ゆ",
    u"ye" : u"いぇ",
    u"yo" : u"よ",
    u"lya" : u"ゃ",
    u"lyi" : u"ぃ",
    u"lyu" : u"ゅ",
    u"lye" : u"ぇ",
    u"lyo" : u"ょ",
    u"xya" : u"ゃ",
    u"xyi" : u"ぃ",
    u"xyu" : u"ゅ",
    u"xye" : u"ぇ",
    u"xyo" : u"ょ",
    u"ra" : u"ら",
    u"ri" : u"り",
    u"ru" : u"る",
    u"re" : u"れ",
    u"ro" : u"ろ",
    u"rya" : u"りゃ",
    u"ryi" : u"りぃ",
    u"ryu" : u"りゅ",
    u"rye" : u"りぇ",
    u"ryo" : u"りょ",
    u"wa" : u"わ",
    u"wi" : u"うぃ",
    u"wu" : u"う",
    u"we" : u"うぇ",
    u"wo" : u"を",
    u"lwa" : u"ゎ",
    u"xwa" : u"ゎ",
    u"n'" : u"ん",
    u"nn" : u"ん",
    u"wyi" : u"ゐ",
    u"wye" : u"ゑ",
}

symbol_rule = {
    # symbols
    u" "  : u"　",
    u","  : u"、",
    u"."  : u"。",
    u"!"  : u"！",
    u"\"" : u"\u201d",
    u"#"  : u"＃",
    u"$"  : u"＄",
    u"%"  : u"％",
    u"&"  : u"＆",
    u"'"  : u"\u2019",
    u"("  : u"（",
    u")"  : u"）",
    u"~"  : u"\uff5e",
    u"-"  : u"ー",
    u"="  : u"＝",
    u"^"  : u"＾",
    u"\\" : u"＼",
    u"|"  : u"｜",
    u"`"  : u"\u2018",
    u"@"  : u"＠",
    u"{"  : u"｛",
    u"["  : u"「",
    u"+"  : u"＋",
    u";"  : u"；",
    u"*"  : u"＊",
    u":"  : u"：",
    u"}"  : u"｝",
    u"]"  : u"」",
    u"<"  : u"＜",
    u">"  : u"＞",
    u"?"  : u"？",
    u"/"  : u"／",
    u"_"  : u"＿",
    u"¥"  : u"￥",

    # numbers
    u'0': u'０',
    u'1': u'１',
    u'2': u'２',
    u'3': u'３',
    u'4': u'４',
    u'5': u'５',
    u'6': u'６',
    u'7': u'７',
    u'8': u'８',
    u'9': u'９',
}

# this is only used with romaji_typing_rule
romaji_double_consonat_typing_rule = {
    # double consonant rule
    u"bb" : (u"っ", u"b"),
    u"cc" : (u"っ", u"c"),
    u"dd" : (u"っ", u"d"),
    u"ff" : (u"っ", u"f"),
    u"gg" : (u"っ", u"g"),
    u"hh" : (u"っ", u"h"),
    u"jj" : (u"っ", u"j"),
    u"kk" : (u"っ", u"k"),
    u"mm" : (u"っ", u"m"),
    u"pp" : (u"っ", u"p"),
    u"rr" : (u"っ", u"r"),
    u"ss" : (u"っ", u"s"),
    u"tt" : (u"っ", u"t"),
    u"vv" : (u"っ", u"v"),
    u"ww" : (u"っ", u"w"),
    u"xx" : (u"っ", u"x"),
    u"yy" : (u"っ", u"y"),
    u"zz" : (u"っ", u"z"),
}

# this is only used with romaji_typing_rule
romaji_correction_rule = {
    u"nb" : (u"ん", u"b"),
    u"nc" : (u"ん", u"c"),
    u"nd" : (u"ん", u"d"),
    u"nf" : (u"ん", u"f"),
    u"ng" : (u"ん", u"g"),
    u"nh" : (u"ん", u"h"),
    u"nj" : (u"ん", u"j"),
    u"nk" : (u"ん", u"k"),
    u"nl" : (u"ん", u"l"),
    u"nm" : (u"ん", u"m"),
    u"np" : (u"ん", u"p"),
    u"nr" : (u"ん", u"r"),
    u"ns" : (u"ん", u"s"),
    u"nt" : (u"ん", u"t"),
    u"nv" : (u"ん", u"v"),
    u"nw" : (u"ん", u"w"),
    u"nx" : (u"ん", u"x"),
    u"nz" : (u"ん", u"z"),
    u"n\0" : (u"ん", u""),
    u"n," : (u"ん", u","),
    u"n." : (u"ん", u"."),
}

# EUC-JP and SJIS do not have the chars
romaji_utf8_rule = {
    u"う゛" : [u"ゔ"],
}

# Hiragana normalization is needed for the personal dict.
romaji_normalize_rule = {
    u"ヴ" : [u"う゛"],
}

# a port of 101kana.sty from scim-anthy
kana_typing_rule_static = {
    # no modifiers keys
    u"1" : u"ぬ",
    u"2" : u"ふ",
    u"3" : u"あ",
    u"4" : u"う",
    u"5" : u"え",
    u"6" : u"お",
    u"7" : u"や",
    u"8" : u"ゆ",
    u"9" : u"よ",
    u"0" : u"わ",
    u"-" : u"ほ",
    u"^" : u"へ",

    u"q" : u"た",
    u"w" : u"て",
    u"e" : u"い",
    u"r" : u"す",
    u"t" : u"か",
    u"y" : u"ん",
    u"u" : u"な",
    u"i" : u"に",
    u"o" : u"ら",
    u"p" : u"せ",
    u"@" : u"゛",
    u"[" : u"゜",

    u"a" : u"ち",
    u"s" : u"と",
    u"d" : u"し",
    u"f" : u"は",
    u"g" : u"き",
    u"h" : u"く",
    u"j" : u"ま",
    u"k" : u"の",
    u"l" : u"り",
    u";" : u"れ",
    u":" : u"け",
    u"]" : u"む",

    u"z" : u"つ",
    u"x" : u"さ",
    u"c" : u"そ",
    u"v" : u"ひ",
    u"b" : u"こ",
    u"n" : u"み",
    u"m" : u"も",
    u"," : u"ね",
    u"." : u"る",
    u"/" : u"め",
    # u"\\" : u"ー",
    u"\\" : u"ろ",

    # shift modifiered keys
    u"!" : u"ぬ",
    u"\"" : u"ふ",
    u"#" : u"ぁ",
    u"$" : u"ぅ",
    u"%" : u"ぇ",
    u"&" : u"ぉ",
    u"'" : u"ゃ",
    u"(" : u"ゅ",
    u")" : u"ょ",
    u"~" : u"を",
    u"=" : u"ほ",
    u"|" : u"ー",

    u"Q" : u"た",
    u"W" : u"て",
    u"E" : u"ぃ",
    u"R" : u"す",
    u"T" : u"ヵ",
    u"Y" : u"ん",
    u"U" : u"な",
    u"I" : u"に",
    u"O" : u"ら",
    u"P" : u"せ",
    u"`" : u"゛",

    u"{" : u"「",

    u"A" : u"ち",
    u"S" : u"と",
    u"D" : u"し",
    u"F" : u"ゎ",
    u"G" : u"き",
    u"H" : u"く",
    u"J" : u"ま",
    u"K" : u"の",
    u"L" : u"り",
    u"+" : u"れ",
    u"*" : u"ヶ",

    u"}" : u"」",

    u"Z" : u"っ",
    u"X" : u"さ",
    u"C" : u"そ",
    u"V" : u"ゐ",
    u"B" : u"こ",
    u"M" : u"も",
    u"N" : u"み",
    u"<" : u"、",
    u">" : u"。",

    u"?" : u"・",
    u"_" : u"ろ",

    u"¥" : u"ー",
}

kana_voiced_consonant_rule = {
    u"か@" : u"が",
    u"き@" : u"ぎ",
    u"く@" : u"ぐ",
    u"け@" : u"げ",
    u"こ@" : u"ご",
    u"さ@" : u"ざ",
    u"し@" : u"じ",
    u"す@" : u"ず",
    u"せ@" : u"ぜ",
    u"そ@" : u"ぞ",
    u"た@" : u"だ",
    u"ち@" : u"ぢ",
    u"つ@" : u"づ",
    u"て@" : u"で",
    u"と@" : u"ど",
    u"は@" : u"ば",
    u"ひ@" : u"び",
    u"ふ@" : u"ぶ",
    u"へ@" : u"べ",
    u"ほ@" : u"ぼ",
    u"か`" : u"が",
    u"き`" : u"ぎ",
    u"く`" : u"ぐ",
    u"け`" : u"げ",
    u"こ`" : u"ご",
    u"さ`" : u"ざ",
    u"し`" : u"じ",
    u"す`" : u"ず",
    u"せ`" : u"ぜ",
    u"そ`" : u"ぞ",
    u"た`" : u"だ",
    u"ち`" : u"ぢ",
    u"つ`" : u"づ",
    u"て`" : u"で",
    u"と`" : u"ど",
    u"は`" : u"ば",
    u"ひ`" : u"び",
    u"ふ`" : u"ぶ",
    u"へ`" : u"べ",
    u"ほ`" : u"ぼ",
    u"は[" : u"ぱ",
    u"ひ[" : u"ぴ",
    u"ふ[" : u"ぷ",
    u"へ[" : u"ぺ",
    u"ほ[" : u"ぽ",
}

#hiragana, katakana, half_katakana
hiragana_katakana_table = {
    u"あ" : (u"ア", u"ｱ"),
    u"い" : (u"イ", u"ｲ"),
    u"う" : (u"ウ", u"ｳ"),
    u"え" : (u"エ", u"ｴ"),
    u"お" : (u"オ", u"ｵ"),
    u"か" : (u"カ", u"ｶ"),
    u"き" : (u"キ", u"ｷ"),
    u"く" : (u"ク", u"ｸ"),
    u"け" : (u"ケ", u"ｹ"),
    u"こ" : (u"コ", u"ｺ"),
    u"が" : (u"ガ", u"ｶﾞ"),
    u"ぎ" : (u"ギ", u"ｷﾞ"),
    u"ぐ" : (u"グ", u"ｸﾞ"),
    u"げ" : (u"ゲ", u"ｹﾞ"),
    u"ご" : (u"ゴ", u"ｺﾞ"),
    u"さ" : (u"サ", u"ｻ"),
    u"し" : (u"シ", u"ｼ"),
    u"す" : (u"ス", u"ｽ"),
    u"せ" : (u"セ", u"ｾ"),
    u"そ" : (u"ソ", u"ｿ"),
    u"ざ" : (u"ザ", u"ｻﾞ"),
    u"じ" : (u"ジ", u"ｼﾞ"),
    u"ず" : (u"ズ", u"ｽﾞ"),
    u"ぜ" : (u"ゼ", u"ｾﾞ"),
    u"ぞ" : (u"ゾ", u"ｿﾞ"),
    u"た" : (u"タ", u"ﾀ"),
    u"ち" : (u"チ", u"ﾁ"),
    u"つ" : (u"ツ", u"ﾂ"),
    u"て" : (u"テ", u"ﾃ"),
    u"と" : (u"ト", u"ﾄ"),
    u"だ" : (u"ダ", u"ﾀﾞ"),
    u"ぢ" : (u"ヂ", u"ﾁﾞ"),
    u"づ" : (u"ヅ", u"ﾂﾞ"),
    u"で" : (u"デ", u"ﾃﾞ"),
    u"ど" : (u"ド", u"ﾄﾞ"),
    u"な" : (u"ナ", u"ﾅ"),
    u"に" : (u"ニ", u"ﾆ"),
    u"ぬ" : (u"ヌ", u"ﾇ"),
    u"ね" : (u"ネ", u"ﾈ"),
    u"の" : (u"ノ", u"ﾉ"),
    u"は" : (u"ハ", u"ﾊ"),
    u"ひ" : (u"ヒ", u"ﾋ"),
    u"ふ" : (u"フ", u"ﾌ"),
    u"へ" : (u"ヘ", u"ﾍ"),
    u"ほ" : (u"ホ", u"ﾎ"),
    u"ば" : (u"バ", u"ﾊﾞ"),
    u"び" : (u"ビ", u"ﾋﾞ"),
    u"ぶ" : (u"ブ", u"ﾌﾞ"),
    u"べ" : (u"ベ", u"ﾍﾞ"),
    u"ぼ" : (u"ボ", u"ﾎﾞ"),
    u"ぱ" : (u"パ", u"ﾊﾟ"),
    u"ぴ" : (u"ピ", u"ﾋﾟ"),
    u"ぷ" : (u"プ", u"ﾌﾟ"),
    u"ぺ" : (u"ペ", u"ﾍﾟ"),
    u"ぽ" : (u"ポ", u"ﾎﾟ"),
    u"ま" : (u"マ", u"ﾏ"),
    u"み" : (u"ミ", u"ﾐ"),
    u"む" : (u"ム", u"ﾑ"),
    u"め" : (u"メ", u"ﾒ"),
    u"も" : (u"モ", u"ﾓ"),
    u"や" : (u"ヤ", u"ﾔ"),
    u"ゆ" : (u"ユ", u"ﾕ"),
    u"よ" : (u"ヨ", u"ﾖ"),
    u"ら" : (u"ラ", u"ﾗ"),
    u"り" : (u"リ", u"ﾘ"),
    u"る" : (u"ル", u"ﾙ"),
    u"れ" : (u"レ", u"ﾚ"),
    u"ろ" : (u"ロ", u"ﾛ"),
    u"わ" : (u"ワ", u"ﾜ"),
    u"を" : (u"ヲ", u"ｦ"),
    u"ん" : (u"ン", u"ﾝ"),
    u"ぁ" : (u"ァ", u"ｧ"),
    u"ぃ" : (u"ィ", u"ｨ"),
    u"ぅ" : (u"ゥ", u"ｩ"),
    u"ぇ" : (u"ェ", u"ｪ"),
    u"ぉ" : (u"ォ", u"ｫ"),
    u"っ" : (u"ッ", u"ｯ"),
    u"ゃ" : (u"ャ", u"ｬ"),
    u"ゅ" : (u"ュ", u"ｭ"),
    u"ょ" : (u"ョ", u"ｮ"),
    u"ヵ" : (u"ヵ", u"ｶ"),
    u"ヶ" : (u"ヶ", u"ｹ"),
    u"ゎ" : (u"ヮ", u"ﾜ"),
    u"ゐ" : (u"ヰ", u"ｨ"),
    u"ゑ" : (u"ヱ", u"ｪ"),
    u"ヴ" : (u"ヴ", u"ｳﾞ"),

    # symbols
    u"ー" : (u"ー", u"ｰ"),
    u"、" : (u"、", u"､"),
    u"。" : (u"。", u"｡"),
    u"！" : (u"！", u"!"),
    u"\u201d"  : (u"\u201d", u"\""),
    u"＃" : (u"＃", u"#"),
    u"＄" : (u"＄", u"$"),
    u"％" : (u"％", u"%"),
    u"＆" : (u"＆", u"&"),
    u"\u2019"  : (u"\u2019", u"'"),
    u"（" : (u"（", u"("),
    u"）" : (u"）", u")"),
    u"\uff5e" : (u"\uff5e", u"~"),
    u"＝" : (u"＝", u"="),
    u"＾" : (u"＾", u"^"),
    u"＼" : (u"＼", u"\\"),
    u"｜" : (u"｜", u"|"),
    u"\u2018"  : (u"\u2018", u"`"),
    u"＠" : (u"＠", u"@"),
    u"゛" : (u"゛", u"ﾞ"),
    u"｛" : (u"｛", u"{"),
    u"゜" : (u"゜", u"ﾟ"),
    u"「" : (u"「", u"｢"),
    u"＋" : (u"＋", u"+"),
    u"；" : (u"；", u";"),
    u"＊" : (u"＊", u"*"),
    u"：" : (u"：", u":"),
    u"｝" : (u"｝", u"}"),
    u"」" : (u"」", u"｣"),
    u"＜" : (u"＜", u"<"),
    u"＞" : (u"＞", u">"),
    u"？" : (u"？", u"?"),
    u"・" : (u"・", u"･"),
    u"／" : (u"／", u"/"),
    u"＿" : (u"＿", u"_"),
    u"￥" : (u"￥", u"¥"),

    # numbers
    u'０': (u'０', u'0'),
    u'１': (u'１', u'1'),
    u'２': (u'２', u'2'),
    u'３': (u'３', u'3'),
    u'４': (u'４', u'4'),
    u'５': (u'５', u'5'),
    u'６': (u'６', u'6'),
    u'７': (u'７', u'7'),
    u'８': (u'８', u'8'),
    u'９': (u'９', u'9'),
}
