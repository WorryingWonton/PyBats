def double_char(str):
    return ''.join([2 * x for x in str])

def count_hi(str):
    return len(str.split('hi')) - 1

def cat_dog(str):
    return len(str.split('cat')) == len(str.split('dog'))

def count_code(str):
    return len([x for idx, x in enumerate(str) if (idx < len(str) - 3 and x + str[idx + 1] + str[idx + 3] == 'coe')])

def end_other(a, b):
    return a[len(a) - len(b):].lower() == b.lower() or b[len(b) - len(a):].lower() == a.lower()

def xyz_there(str):
    return 'xyz' in ''.join(str.split('.xyz'))

def bobThere(str):
    for idx in range(1, len(str) - 1):
        if ['b', 'b'] == [str[idx - 1], str[idx + 1]]:
            return True
    return False

def xyBalance(str):
    return 'x' not in str or 'y' in str.split('x')[-1]

def mixString(a, b):
    new_str = ''
    min_len = min(len(a), len(b))
    for index in range(min_len):
        new_str += a[index] + b[index]
    return new_str + b[min_len:] + a[min_len:]

def repeatEnd(str, n):
    return n * str[-n:]

def repeatFront(str, n):
    return ''.join([str[:idx] for idx in range(n, 0, -1)])

def repeatSeparator(word, sep, count):
    return ((word + sep) * count)[:(len(word) + len(sep)) * count - len(sep)]

def prefixAgain(str, n):
    return str[:n] in str[n:]

def xyzMiddle(str):
    return 'xyz' in str[int(len(str) / 2) - 2 + len(str) % 2:int(len(str) / 2) + 3 - len(str) % 2]

def getSandwich(str):
    return str[str.index('bread') + 5:len(str) - str[::-1].index('daerb') - 5] if len(str) > 9 else ''

def sameStarChar(str):
    for idx in range(1, len(str) - 1):
        if str[idx] == '*' and str[idx - 1] != str[idx + 1]:
            return False
    return True

def oneTwo(str):
    new_str = ''
    for idx in range(0, len(str) - 2, 3):
        new_str += str[idx + 1:idx + 3] + str[idx]
    return new_str

def zipZap(str):
    return ''.join([x for idx, x in enumerate(str) if str[idx - 1:idx + 2] != f'z{x}p'])

def starOut(str):
    return ''.join([x for idx, x in enumerate(str) if '*' not in [str[idx - 1:idx], x, str[idx + 1:idx + 2]]])

def plusOut(str, word):
    return word.join(['+' * len(x) for x in str.split(word)])

def wordEnds(str, word):
    new_str = ''
    for idx in range(len(str)):
        if str[idx:idx + len(word)] == word:
            new_str += str[idx - 1:idx] + str[idx + len(word):idx + len(word) + 1]
    return new_str


assert double_char('The') == 'TThhee'
assert double_char('AAbb') == 'AAAAbbbb'
assert double_char('Hi-There') == 'HHii--TThheerree'
assert double_char('Word!') == 'WWoorrdd!!'
assert double_char('') == ''
assert double_char('a') == 'aa'
assert double_char('.') == '..'
assert double_char('aa') == 'aaaa'

assert count_hi('abc hi ho') == 1
assert count_hi('ABChi hi') == 2
assert count_hi('hihi') == 2
assert count_hi('hiHIhi') == 2
assert count_hi('') == 0
assert count_hi('h') == 0
assert count_hi('hi') == 1
assert count_hi('Hi is no HI on ahI') == 0
assert count_hi('hiho not HOHIhi') == 2

assert cat_dog('catdog') == True
assert cat_dog('catcat') == False
assert cat_dog('1cat1cadodog') == True
assert cat_dog('catxxdogxxxdog') == False
assert cat_dog('catxdogxdogxcat') == True
assert cat_dog('catxdogxdogxca') == False
assert cat_dog('dogdogcat') == False
assert cat_dog('dogogcat') == True
assert cat_dog('dog') == False
assert cat_dog('cat') == False
assert cat_dog('ca') == True
assert cat_dog('c') == True
assert cat_dog('') == True

assert count_code('aaacodebbb') == 1
assert count_code('codexxcode') == 2
assert count_code('cozexxcope') == 2
assert count_code('cozfxxcope') == 1
assert count_code('xxcozeyycop') == 1
assert count_code('cozcop') == 0
assert count_code('abcxyz') == 0
assert count_code('code') == 1
assert count_code('ode') == 0
assert count_code('c') == 0
assert count_code('') == 0
assert count_code('AAcodeBBcoleCCccoreDD') == 3
assert count_code('AAcodeBBcoleCCccorfDD') == 2
assert count_code('coAcodeBcoleccoreDD') == 3

assert end_other('Hiabc', 'abc') == True
assert end_other('AbC', 'HiaBc') == True
assert end_other('abc', 'abXabc') == True
assert end_other('Hiabc', 'abcd') == False
assert end_other('Hiabc', 'bc') == True
assert end_other('Hiabcx', 'bc') == False
assert end_other('abc', 'abc') == True
assert end_other('xyz', '12xyz') == True
assert end_other('yz', '12xz') == False
assert end_other('Z', '12xz') == True
assert end_other('12', '12') == True
assert end_other('abcXYZ', 'abcDEF') == False
assert end_other('ab', 'ab12') == False
assert end_other('ab', '12ab') == True

assert xyz_there('abcxyz') == True
assert xyz_there('abc.xyz') == False
assert xyz_there('xyz.abc') == True
assert xyz_there('abcxy') == False
assert xyz_there('xyz') == True
assert xyz_there('xy') == False
assert xyz_there('x') == False
assert xyz_there('') == False
assert xyz_there('abc.xyzxyz') == True
assert xyz_there('abc.xxyz') == True
assert xyz_there('.xyz') == False
assert xyz_there('12.xyz') == False
assert xyz_there('12xyz') == True
assert xyz_there('1.xyz.xyz2.xyz') == False

assert bobThere("abcbob") == True
assert bobThere("b9b") == True
assert bobThere("bac") == False
assert bobThere("bbb") == True
assert bobThere("abcdefb") == False
assert bobThere("123abcbcdbabxyz") == True
assert bobThere("b12") == False
assert bobThere("b1b") == True
assert bobThere("b12b1b") == True
assert bobThere("bbc") == False
assert bobThere("bbb") == True
assert bobThere("bb") == False
assert bobThere("b") == False

assert xyBalance("aaxbby") == True
assert xyBalance("aaxbb") == False
assert xyBalance("yaaxbb") == False
assert xyBalance("yaaxbby") == True
assert xyBalance("xaxxbby") == True
assert xyBalance("xaxxbbyx") == False
assert xyBalance("xxbxy") == True
assert xyBalance("xxbx") == False
assert xyBalance("bbb") == True
assert xyBalance("bxbb") == False
assert xyBalance("bxyb") == True
assert xyBalance("xy") == True
assert xyBalance("y") == True
assert xyBalance("x") == False
assert xyBalance("") == True
assert xyBalance("yxyxyxyx") == False
assert xyBalance("yxyxyxyxy") == True
assert xyBalance("12xabxxydxyxyzz") == True

assert mixString("abc", "xyz") == "axbycz"
assert mixString("Hi", "There") == "HTihere"
assert mixString("xxxx", "There") == "xTxhxexre"
assert mixString("xxx", "X") == "xXxx"
assert mixString("2/", "27 around") == "22/7 around"
assert mixString("", "Hello") == "Hello"
assert mixString("Abc", "") == "Abc"
assert mixString("", "") == ""
assert mixString("a", "b") == "ab"
assert mixString("ax", "b") == "abx"
assert mixString("a", "bx") == "abx"
assert mixString("So", "Long") == "SLoong"
assert mixString("Long", "So") == "LSoong"

assert repeatEnd("Hello", 3) == "llollollo"
assert repeatEnd("Hello", 2) == "lolo"
assert repeatEnd("Hello", 1) == "o"
assert repeatEnd("Hello", 0) == ""
assert repeatEnd("abc", 3) == "abcabcabc"
assert repeatEnd("1234", 2) == "3434"
assert repeatEnd("1234", 3) == "234234234"
assert repeatEnd("", 0) == ""

assert repeatFront("Chocolate", 4) == "ChocChoChC"
assert repeatFront("Chocolate", 3) == "ChoChC"
assert repeatFront("Ice Cream", 2) == "IcI"
assert repeatFront("Ice Cream", 1) == "I"
assert repeatFront("Ice Cream", 0) == ""
assert repeatFront("xyz", 3) == "xyzxyx"
assert repeatFront("", 0) == ""
assert repeatFront("Java", 4) == "JavaJavJaJ"
assert repeatFront("Java", 1) == "J"

assert repeatSeparator("Word", "X", 3) == "WordXWordXWord"
assert repeatSeparator("This", "And", 2) == "ThisAndThis"
assert repeatSeparator("This", "And", 1) == "This"
assert repeatSeparator("Hi", "-n-", 2) == "Hi-n-Hi"
assert repeatSeparator("AAA", "", 1) == "AAA"
assert repeatSeparator("AAA", "", 4) == "AAAAAAAAAAAA"
assert repeatSeparator("AAA", "", 0) == ""
assert repeatSeparator("A", "B", 5) == "ABABABABA"
assert repeatSeparator("abc", "XX", 3) == "abcXXabcXXabc"
assert repeatSeparator("abc", "XX", 2) == "abcXXabc"
assert repeatSeparator("abc", "XX", 1) == "abc"
assert repeatSeparator("XYZ", "a", 2) == "XYZaXYZ"

assert prefixAgain("abXYabc", 1) == True
assert prefixAgain("abXYabc", 2) == True
assert prefixAgain("abXYabc", 3) == False
assert prefixAgain("xyzxyxyxy", 2) == True
assert prefixAgain("xyzxyxyxy", 3) == False
assert prefixAgain("Hi12345Hi6789Hi10", 1) == True
assert prefixAgain("Hi12345Hi6789Hi10", 2) == True
assert prefixAgain("Hi12345Hi6789Hi10", 3) == True
assert prefixAgain("Hi12345Hi6789Hi10", 4) == False
assert prefixAgain("a", 1) == False
assert prefixAgain("aa", 1) == True
assert prefixAgain("ab", 1) == False

assert xyzMiddle("AAxyzBB") == True
assert xyzMiddle("AxyzBB") == True
assert xyzMiddle("AxyzBBB") == False
assert xyzMiddle("AxyzBBBB") == False
assert xyzMiddle("AAAxyzB") == False
assert xyzMiddle("AAAxyzBB") == True
assert xyzMiddle("AAAAxyzBB") == False
assert xyzMiddle("AAAAAxyzBBB") == False
assert xyzMiddle("1x345xyz12x4") == True
assert xyzMiddle("xyzAxyzBBB") == True
assert xyzMiddle("xyzAxyzBxyz") == True
assert xyzMiddle("xyzxyzAxyzBxyzxyz") == True
assert xyzMiddle("xyzxyzAxyzBxyzxyz") == True
assert xyzMiddle("xyzxyzAxyzxyzxyz") == True
assert xyzMiddle("xyzxyzAxyzxyzxy") == False
assert xyzMiddle("AxyzxyzBB") == False
assert xyzMiddle("") == False
assert xyzMiddle("x") == False
assert xyzMiddle("xy") == False
assert xyzMiddle("xyz") == True
assert xyzMiddle("xyzz") == True

assert getSandwich("breadjambread") == "jam"
assert getSandwich("xxbreadjambreadyy") == "jam"
assert getSandwich("xxbreadyy") == ""
assert getSandwich("xxbreadbreadjambreadyy") == "breadjam"
assert getSandwich("breadAbread") == "A"
assert getSandwich("breadbread") == ""
assert getSandwich("abcbreaz") == ""
assert getSandwich("xyz") == ""
assert getSandwich("") == ""
assert getSandwich("breadbreaxbread") == "breax"
assert getSandwich("breaxbreadybread") == "y"
assert getSandwich("breadbreadbreadbread") == "breadbread"

assert sameStarChar("xy*yzz") == True
assert sameStarChar("xy*zzz") == False
assert sameStarChar("*xa*az") == True
assert sameStarChar("*xa*bz") == False
assert sameStarChar("*xa*a*") == True
assert sameStarChar("") == True
assert sameStarChar("*xa*a*a") == True
assert sameStarChar("*xa*a*b") == False
assert sameStarChar("*12*2*2") == True
assert sameStarChar("12*2*3*") == False
assert sameStarChar("abcDEF") == True
assert sameStarChar("XY*YYYY*Z*") == False
assert sameStarChar("XY*YYYY*Y*") == True
assert sameStarChar("12*2*3*") == False
assert sameStarChar("*") == True
assert sameStarChar("**") == True

assert oneTwo("abc") == "bca"
assert oneTwo("tca") == "cat"
assert oneTwo("tcagdo") == "catdog"
assert oneTwo("chocolate") == "hocolctea"
assert oneTwo("1234567890") == "231564897"
assert oneTwo("xabxabxabxabxabxabxab") == "abxabxabxabxabxabxabx"
assert oneTwo("abcdefx") == "bcaefd"
assert oneTwo("abcdefxy") == "bcaefd"
assert oneTwo("abcdefxyz") == "bcaefdyzx"
assert oneTwo("") == ""
assert oneTwo("x") == ""
assert oneTwo("xy") == ""
assert oneTwo("xyz") == "yzx"
assert oneTwo("abcdefghijklkmnopqrstuvwxyz1234567890") == "bcaefdhigkljmnkpqostrvwuyzx231564897"
assert oneTwo("abcdefghijklkmnopqrstuvwxyz123456789") == "bcaefdhigkljmnkpqostrvwuyzx231564897"
assert oneTwo("abcdefghijklkmnopqrstuvwxyz12345678") == "bcaefdhigkljmnkpqostrvwuyzx231564"

assert zipZap("zipXzap") == "zpXzp"
assert zipZap("zopzop") == "zpzp"
assert zipZap("zzzopzop") == "zzzpzp"
assert zipZap("zibzap") == "zibzp"
assert zipZap("zip") == "zp"
assert zipZap("zi") == "zi"
assert zipZap("z") == "z"
assert zipZap("") == ""
assert zipZap("zzp") == "zp"
assert zipZap("abcppp") == "abcppp"
assert zipZap("azbcppp") == "azbcppp"
assert zipZap("azbcpzpp") == "azbcpzp"

assert starOut("ab*cd") == "ad"
assert starOut("ab**cd") == "ad"
assert starOut("sm*eilly") == "silly"
assert starOut("sm*eil*ly") == "siy"
assert starOut("sm**eil*ly") == "siy"
assert starOut("sm***eil*ly") == "siy"
assert starOut("stringy*") == "string"
assert starOut("*stringy") == "tringy"
assert starOut("*str*in*gy") == "ty"
assert starOut("abc") == "abc"
assert starOut("a*bc") == "c"
assert starOut("ab") == "ab"
assert starOut("a*b") == ""
assert starOut("a") == "a"
assert starOut("a*") == ""
assert starOut("*a") == ""
assert starOut("*") == ""
assert starOut("") == ""

assert plusOut("12xy34", "xy") == "++xy++"
assert plusOut("12xy34", "1") == "1+++++"
assert plusOut("12xy34xyabcxy", "xy") == "++xy++xy+++xy"
assert plusOut("abXYabcXYZ", "ab") == "ab++ab++++"
assert plusOut("abXYabcXYZ", "abc") == "++++abc+++"
assert plusOut("abXYabcXYZ", "XY") == "++XY+++XY+"
assert plusOut("abXYxyzXYZ", "XYZ") == "+++++++XYZ"
assert plusOut("--++ab", "++") == "++++++"
assert plusOut("aaxxxxbb", "xx") == "++xxxx++"
assert plusOut("123123", "3") == "++3++3"

assert wordEnds("abcXY123XYijk", "XY") == "c13i"
assert wordEnds("XY123XY", "XY") == "13"
assert wordEnds("XY1XY", "XY") == "11"
assert wordEnds("XYXY", "XY") == "XY"
assert wordEnds("XY", "XY") == ""
assert wordEnds("Hi", "XY") == ""
assert wordEnds("", "XY") == ""
assert wordEnds("abc1xyz1i1j", "1") == "cxziij"
assert wordEnds("abc1xyz1", "1") == "cxz"
assert wordEnds("abc1xyz11", "1") == "cxz11"
assert wordEnds("abc1xyz1abc", "abc") == "11"
assert wordEnds("abc1xyz1abc", "b") == "acac"
assert wordEnds("abc1abc1abc", "abc") == "1111"