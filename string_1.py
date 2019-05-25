def hello_name(name):
    return 'Hello ' + name + '!'

def make_abba(a, b):
    return a + 2 * b + a

def make_tags(tag, word):
    return '<' + tag + '>' + word + '</' + tag + '>'

def make_out_word(out, word):
    return out[:2] + word + out[2:]

def extra_end(str):
    return 3 * str[-2:]

def first_two(str):
    return str[:2]

def first_half(str):
    return str[:int(len(str)/2)]

def without_end(str):
    return str[1:-1]

def combo_string(a, b):
    return min(a, b, key=len) + max(a, b, key=len) + min(a, b, key=len)

def non_start(a, b):
    return a[1:] + b[1:]

def left2(str):
    return str[2:] + str[:2]

def right2(str):
    return str[-2:] + str[:-2]

def theEnd(str, front):
    return str[0] if front else str[-1]

def withouEnd2(str):
    return str[1:-1]

def middleTwo(str):
    return str[int(len(str) / 2) - 1] + str[int(len(str) / 2)]

def endsLy(str):
    return str[-2:] == 'ly'

def nTwice(str, n):
    return str[:n] + str[-n:] if n else ''

def twoChar(str, index):
    return str[index:index + 2] if 0 < index + 1 < len(str) else str[:2]

def middleThree(str):
    return str[int(len(str) / 2) - 1:int(len(str) / 2) + 2]

def hasBad(str):
    return 'bad' in str[0:4]

def atFirst(str):
    return (str[0] if str else '@') + (str[1] if len(str) > 1 else '@')

def lastChars(a, b):
    return (a[0] if a else '@') + (b[-1] if b else '@')

def conCat(a, b):
    return a + (b if b[:1] != a[-1:] else b[1:])

def lastTwo(str):
    return str[:-2] + str[-1:] + str[-2:-1]

def seeColor(str):
    return 'red' if str[:3] == 'red' else 'blue' if str[:4] == 'blue' else ''

def frontAgain(str):
    return str[:2] == str[-2:] if len(str) > 1 else False

def minCat(a, b):
    return a[-min(len(a), len(b)):] + b[-min(len(a), len(b)):] if a and b else ''

def extraFront(str):
    return 3 * str[:2]

def without2(str):
    return str[2:] if str[-2:] == str[:2] and len(str) > 1 else str

def deFront(str):
    return (str[:1] if str[:1] == 'a' else '') + (str[1:2] if str[1:2] == 'b' else '') + str[2:]

def startWord(str, word):
    return str[:1] + word[1:] if word[1:] == str[1:len(word)] else ''

def withoutX(str):
    return (str[:1] if str[:1] != 'x' else '') + str[1:-1] + (str[-1:] if str[-1:] != 'x' else '')

def withoutX2(str):
    return (str[:1] if str[:1] != 'x' else '') + (str[1:2] if str[1:2] != 'x' else '') + str[2:]


assert hello_name('Bob') == 'Hello Bob!'
assert hello_name('Alice') == 'Hello Alice!'
assert hello_name('X') == 'Hello X!'
assert hello_name('Dolly') == 'Hello Dolly!'
assert hello_name('Alpha') == 'Hello Alpha!'
assert hello_name('Omega') == 'Hello Omega!'
assert hello_name('Goodbye') == 'Hello Goodbye!'
assert hello_name('ho ho ho') == 'Hello ho ho ho!'
assert hello_name('xyz!') == 'Hello xyz!!'
assert hello_name('Hello') == 'Hello Hello!'

assert make_abba('Hi', 'Bye') == 'HiByeByeHi'
assert make_abba('Yo', 'Alice') == 'YoAliceAliceYo'
assert make_abba('What', 'Up') == 'WhatUpUpWhat'
assert make_abba('aaa', 'bbb') == 'aaabbbbbbaaa'
assert make_abba('x', 'y') == 'xyyx'
assert make_abba('x', '') == 'xx'
assert make_abba('', 'y') == 'yy'
assert make_abba('Bo', 'Ya') == 'BoYaYaBo'
assert make_abba('Ya', 'Ya') == 'YaYaYaYa'

assert make_tags('i', 'Yay') == '<i>Yay</i>'
assert make_tags('i', 'Hello') == '<i>Hello</i>'
assert make_tags('cite', 'Yay') == '<cite>Yay</cite>'
assert make_tags('address', 'here') == '<address>here</address>'
assert make_tags('body', 'Heart') == '<body>Heart</body>'
assert make_tags('i', 'i') == '<i>i</i>'
assert make_tags('i', '') == '<i></i>'

assert make_out_word('<<>>', 'Yay') == '<<Yay>>'
assert make_out_word('<<>>', 'WooHoo') == '<<WooHoo>>'
assert make_out_word('[[]]', 'word') == '[[word]]'
assert make_out_word('HHoo', 'Hello') == 'HHHellooo'
assert make_out_word('abyz', 'YAY') == 'abYAYyz'

assert extra_end('Hello') == 'lololo'
assert extra_end('ab') == 'ababab'
assert extra_end('Hi') == 'HiHiHi'
assert extra_end('Candy') == 'dydydy'
assert extra_end('Code') == 'dedede'

assert first_two('Hello') == 'He'
assert first_two('abcdefg') == 'ab'
assert first_two('ab') == 'ab'
assert first_two('a') == 'a'
assert first_two('') == ''
assert first_two('Kitten') == 'Ki'
assert first_two('hi') == 'hi'
assert first_two('hiya') == 'hi'

assert first_half('WooHoo') == 'Woo'
assert first_half('HelloThere') == 'Hello'
assert first_half('abcdef') == 'abc'
assert first_half('ab') == 'a'
assert first_half('') == ''
assert first_half('0123456789') == '01234'
assert first_half('kitten') == 'kit'

assert without_end('Hello') == 'ell'
assert without_end('java') == 'av'
assert without_end('coding') == 'odin'
assert without_end('code') == 'od'
assert without_end('ab') == ''
assert without_end('Chocolate!') == 'hocolate'
assert without_end('kitten') == 'itte'
assert without_end('woohoo') == 'ooho'

assert combo_string('Hello', 'hi') == 'hiHellohi'
assert combo_string('hi', 'Hello') == 'hiHellohi'
assert combo_string('aaa', 'b') == 'baaab'
assert combo_string('b', 'aaa') == 'baaab'
assert combo_string('aaa', '') == 'aaa'
assert combo_string('', 'bb') == 'bb'
assert combo_string('aaa', '1234') == 'aaa1234aaa'
assert combo_string('aaa', 'bb') == 'bbaaabb'
assert combo_string('a', 'bb') == 'abba'
assert combo_string('bb', 'a') == 'abba'
assert combo_string('xyz', 'ab') == 'abxyzab'

assert non_start('Hello', 'There') == 'ellohere'
assert non_start('java', 'code') == 'avaode'
assert non_start('shotl', 'java') == 'hotlava'
assert non_start('ab', 'xy') == 'by'
assert non_start('ab', 'x') == 'b'
assert non_start('ab', 'x') == 'b'
assert non_start('x', 'ac') == 'c'
assert non_start('a', 'x') == ''
assert non_start('kit', 'kat') == 'itat'
assert non_start('mart', 'dart') == 'artart'

assert left2('Hello') == 'lloHe'
assert left2('java') == 'vaja'
assert left2('Hi') == 'Hi'
assert left2('code') == 'deco'
assert left2('cat') == 'tca'
assert left2('12345') == '34512'
assert left2('Chocolate') == 'ocolateCh'
assert left2('bricks') == 'icksbr'

assert right2("Hello") == "loHel"
assert right2("java") == "vaja"
assert right2("Hi") == "Hi"
assert right2("code") == "deco"
assert right2("cat") == "atc"
assert right2("12345") == "45123"

assert theEnd("Hello", True) == "H"
assert theEnd("Hello", False) == "o"
assert theEnd("oh", True) == "o"
assert theEnd("oh", False) == "h"
assert theEnd("x", True) == "x"
assert theEnd("x", False) == "x"
assert theEnd("java", True) == "j"
assert theEnd("chocolate", False) == "e"
assert theEnd("1234", True) == "1"
assert theEnd("code", False) == "e"

assert withouEnd2("Hello") == "ell"
assert withouEnd2("abc") == "b"
assert withouEnd2("ab") == ""
assert withouEnd2("a") == ""
assert withouEnd2("") == ""
assert withouEnd2("coldy") == "old"
assert withouEnd2("java code") == "ava cod"

assert middleTwo("string") == "ri"
assert middleTwo("code") == "od"
assert middleTwo("Practice") == "ct"
assert middleTwo("ab") == "ab"
assert middleTwo("0123456789") == "45"

assert endsLy("oddly") == True
assert endsLy("y") == False
assert endsLy("oddy") == False
assert endsLy("oddl") == False
assert endsLy("olydd") == False
assert endsLy("ly") == True
assert endsLy("") == False
assert endsLy("Falsey") == False
assert endsLy("evenly") == True

assert nTwice("Hello", 2) == "Helo"
assert nTwice("Chocolate", 3) == "Choate"
assert nTwice("Chocolate", 1) == "Ce"
assert nTwice("Chocolate", 0) == ""
assert nTwice("Hello", 4) == "Hellello"
assert nTwice("Code", 4) == "CodeCode"
assert nTwice("Code", 2) == "Code"

assert twoChar("java", 0) == "ja"
assert twoChar("java", 2) == "va"
assert twoChar("java", 3) == "ja"
assert twoChar("java", 4) == "ja"
assert twoChar("java", -1) == "ja"
assert twoChar("Hello", 0) == "He"
assert twoChar("Hello", 1) == "el"
assert twoChar("Hello", 99) == "He"
assert twoChar("Hello", 3) == "lo"
assert twoChar("Hello", 4) == "He"
assert twoChar("Hello", 5) == "He"
assert twoChar("Hello", -7) == "He"
assert twoChar("Hello", 6) == "He"
assert twoChar("Hello", -1) == "He"
assert twoChar("yay", 0) == "ya"

assert middleThree("Candy") == "and"
assert middleThree("and") == "and"
assert middleThree("solving") == "lvi"
assert middleThree("Hi yet Hi") == "yet"
assert middleThree("java yet java") == "yet"
assert middleThree("Chocolate") == "col"
assert middleThree("XabcxyzabcX") == "xyz"

assert hasBad("badxx") == True
assert hasBad("xbadxx") == True
assert hasBad("xxbadxx") == False
assert hasBad("code") == False
assert hasBad("bad") == True
assert hasBad("ba") == False
assert hasBad("xba") == False
assert hasBad("xbad") == True
assert hasBad("") == False
assert hasBad("badyy") == True

assert atFirst("hello") == "he"
assert atFirst("hi") == "hi"
assert atFirst("h") == "h@"
assert atFirst("") == "@@"
assert atFirst("kitten") == "ki"
assert atFirst("java") == "ja"
assert atFirst("j") == "j@"

assert lastChars("last", "chars") == "ls"
assert lastChars("yo", "java") == "ya"
assert lastChars("hi", "") == "h@"
assert lastChars("", "hello") == "@o"
assert lastChars("", "") == "@@"
assert lastChars("kitten", "hi") == "ki"
assert lastChars("k", "zip") == "kp"
assert lastChars("kitten", "") == "k@"
assert lastChars("kitten", "zip") == "kp"

assert conCat("abc", "cat") == "abcat"
assert conCat("dog", "cat") == "dogcat"
assert conCat("abc", "") == "abc"
assert conCat("", "cat") == "cat"
assert conCat("pig", "g") == "pig"
assert conCat("pig", "doggy") == "pigdoggy"

assert lastTwo("coding") == "codign"
assert lastTwo("cat") == "cta"
assert lastTwo("ab") == "ba"
assert lastTwo("a") == "a"
assert lastTwo("") == ""

assert seeColor("redxx") == "red"
assert seeColor("xxred") == ""
assert seeColor("blueTimes") == "blue"
assert seeColor("NoColor") == ""
assert seeColor("red") == "red"
assert seeColor("re") == ""
assert seeColor("blu") == ""
assert seeColor("blue") == "blue"
assert seeColor("a") == ""
assert seeColor("") == ""
assert seeColor("xyzred") == ""

assert frontAgain("edited") == True
assert frontAgain("edit") == False
assert frontAgain("ed") == True
assert frontAgain("jj") == True
assert frontAgain("jjj") == True
assert frontAgain("jjjj") == True
assert frontAgain("jjjk") == False
assert frontAgain("x") == False
assert frontAgain("") == False
assert frontAgain("java") == False
assert frontAgain("javaja") == True

assert minCat("Hello", "Hi") == "loHi"
assert minCat("Hello", "java") == "ellojava"
assert minCat("java", "Hello") == "javaello"
assert minCat("abc", "x") == "cx"
assert minCat("x", "abc") == "xc"
assert minCat("abc", "") == ""

assert extraFront("Hello") == "HeHeHe"
assert extraFront("ab") == "ababab"
assert extraFront("H") == "HHH"
assert extraFront("") == ""
assert extraFront("Candy") == "CaCaCa"
assert extraFront("Code") == "CoCoCo"

assert without2("HelloHe") == "lloHe"
assert without2("HelloHi") == "HelloHi"
assert without2("Hi") == ""
assert without2("Chocolate") == "Chocolate"
assert without2("xxx") == "x"
assert without2("xx") == ""
assert without2("x") == "x"
assert without2("") == ""
assert without2("Fruits") == "Fruits"

assert deFront("Hello") == "llo"
assert deFront("java") == "va"
assert deFront("away") == "aay"
assert deFront("axy") == "ay"
assert deFront("abc") == "abc"
assert deFront("xby") == "by"
assert deFront("ab") == "ab"
assert deFront("ax") == "a"
assert deFront("axb") == "ab"
assert deFront("aaa") == "aa"
assert deFront("xbc") == "bc"
assert deFront("bbb") == "bb"
assert deFront("bazz") == "zz"
assert deFront("ba") == ""
assert deFront("abxyz") == "abxyz"
assert deFront("hi") == ""
assert deFront("his") == "s"
assert deFront("xz") == ""
assert deFront("zzz") == "z"

assert startWord("hippo", "hi") == "hi"
assert startWord("hippo", "xip") == "hip"
assert startWord("hippo", "i") == "h"
assert startWord("hippo", "ix") == ""
assert startWord("h", "ix") == ""
assert startWord("", "i") == ""
assert startWord("hip", "zi") == "hi"
assert startWord("hip", "zip") == "hip"
assert startWord("hip", "zig") == ""
assert startWord("h", "z") == "h"
assert startWord("hippo", "xippo") == "hippo"
assert startWord("hippo", "xyz") == ""
assert startWord("hippo", "hip") == "hip"
assert startWord("kitten", "cit") == "kit"
assert startWord("kit", "cit") == "kit"

assert withoutX("xHix") == "Hi"
assert withoutX("xHi") == "Hi"
assert withoutX("Hxix") == "Hxi"
assert withoutX("Hi") == "Hi"
assert withoutX("xxHi") == "xHi"
assert withoutX("Hix") == "Hi"
assert withoutX("xaxbx") == "axb"
assert withoutX("xx") == ""
assert withoutX("x") == ""
assert withoutX("") == ""
assert withoutX("Hello") == "Hello"
assert withoutX("Hexllo") == "Hexllo"

assert withoutX2("xHi") == "Hi"
assert withoutX2("Hxi") == "Hi"
assert withoutX2("Hi") == "Hi"
assert withoutX2("xxHi") == "Hi"
assert withoutX2("Hix") == "Hix"
assert withoutX2("xaxb") == "axb"
assert withoutX2("axxb") == "axb"
assert withoutX2("xx") == ""
assert withoutX2("x") == ""
assert withoutX2("") == ""
assert withoutX2("Hello") == "Hello"
assert withoutX2("Hexllo") == "Hexllo"
assert withoutX2("xHxllo") == "Hxllo"