def sleep_in(weekday, vacation):
    return not weekday or vacation

def monkey_trouble(a_smile, b_smile):
    return a_smile == b_smile

def sum_double(a, b):
    return a + b if a != b else 2 * (a + b)

def diff21(n):
    return abs(n - 21) if n < 22 else 2 * abs(n - 21)

def parrot_trouble(talking, hour):
    return talking and hour not in range(7, 21)

def makes10(a, b):
    return a + b == 10 or 10 in [a, b]

def near_hundred(n):
    return abs(100 - n) <= 10 or abs(200 - n) <= 10

def missing_char(str, n):
    return str[:n] + str[n + 1:]

def not_string(str):
    return 'not ' + str if str[:3] != 'not' else str

def pos_neg(a, b, negative):
    return (a < 0) ^ (b < 0) if not negative else (a < 0 and b < 0)

def front_back(str):
    return str[-1:] + str[1:-1] + str[:1] if len(str) > 1 else str

def front3(str):
    return 3 * str[0:3]

def backAround(str):
    return str[-1:] + str + str[-1:]

def or35(n):
    return not n % 3 or not n % 5

def front22(str):
    return str[:2] + str + str[:2]

def startHi(str):
    return str[:2] == 'hi'

def icyHot(temp1, temp2):
    return (temp1 < 0 and temp2 > 100) or (temp1 > 100 and temp2 < 0)

def in1020(a, b):
    return a in range(10, 21) or b in range(10, 21)

def hasTeen(a, b, c):
    return a in range(13, 20) or b in range(13, 20) or c in range(13, 20)

def loneTeen(a, b):
    return (a in range(13, 20)) ^ (b in range(13, 20))

def delDel(str):
    return str[0] + str[4:] if str[1:4] == 'del' else str

def mixStart(str):
    return str[1:3] == 'ix'

def startOz(str):
    return (str[:1] if str[:1] == 'o' else '') + (str[1:2] if str[1:2] == 'z' else '')

def intMax(a, b, c):
    return max(a, b, c)

def close10(a, b):
    return a if abs(10 - a) < abs(10 - b) else b if abs(10 - a) != abs(10 - b) else 0

def in3050(a, b):
    return (a in range(30, 41) and b in range(30, 41)) or (a in range(40, 51) and b in range(40, 51))

def max1020(a, b):
    return max(a if a in range(10, 21) else 0, b if b in range(10, 21) else 0)

def stringE(str):
    return str.count('e') in range(1, 4)

def lastDigit(a, b):
    return a % 10 == b % 10

def endUp(str):
    return str[:-3] + str[-3:].upper()

def everyNth(str, n):
    return str[0] + everyNth(str[n:], n) if str else ''


assert sleep_in(False, False) == True
assert sleep_in(True, False) == False
assert sleep_in(False, True) == True
assert sleep_in(True, True) == True

assert monkey_trouble(True, True) == True
assert monkey_trouble(False, False) == True
assert monkey_trouble(True, False) == False
assert monkey_trouble(False, True) == False

assert sum_double(1, 2) == 3
assert sum_double(3, 2) == 5
assert sum_double(2, 2) == 8
assert sum_double(-1, 0) == -1
assert sum_double(3, 3) == 12
assert sum_double(0, 0) == 0
assert sum_double(0, 1) == 1
assert sum_double(3, 4) == 7

assert diff21(19) == 2
assert diff21(10) == 11
assert diff21(21) == 0
assert diff21(22) == 2
assert diff21(25) == 8
assert diff21(30) == 18
assert diff21(0) == 21
assert diff21(1) == 20
assert diff21(2) == 19
assert diff21(-1) == 22
assert diff21(-2) == 23
assert diff21(50) == 58

assert parrot_trouble(True, 6) == True
assert parrot_trouble(True, 7) == False
assert parrot_trouble(False, 6) == False
assert parrot_trouble(True, 21) == True
assert parrot_trouble(False, 21) == False
assert parrot_trouble(False, 20) == False
assert parrot_trouble(True, 23) == True
assert parrot_trouble(False, 23) == False
assert parrot_trouble(True, 20) == False
assert parrot_trouble(False, 12) == False

assert makes10(9, 10) == True
assert makes10(9, 9) == False
assert makes10(1, 9) == True
assert makes10(10, 1) == True
assert makes10(10, 10) == True
assert makes10(8, 2) == True
assert makes10(8, 3) == False
assert makes10(10, 42) == True
assert makes10(12, -2) == True

assert near_hundred(93) == True
assert near_hundred(90) == True
assert near_hundred(89) == False
assert near_hundred(110) == True
assert near_hundred(111) == False
assert near_hundred(121) == False
assert near_hundred(-101) == False
assert near_hundred(-209) == False
assert near_hundred(190) == True
assert near_hundred(209) == True
assert near_hundred(0) == False
assert near_hundred(5) == False
assert near_hundred(-50) == False
assert near_hundred(191) == True
assert near_hundred(189) == False
assert near_hundred(200) == True
assert near_hundred(210) == True
assert near_hundred(211) == False
assert near_hundred(290) == False

assert pos_neg(1, -1, False) == True
assert pos_neg(-1, 1, False) == True
assert pos_neg(-4, -5, True) == True
assert pos_neg(-4, -5, False) == False
assert pos_neg(-4, 5, False) == True
assert pos_neg(-4, 5, True) == False
assert pos_neg(1, 1, False) == False
assert pos_neg(-1, -1, False) == False
assert pos_neg(1, -1, True) == False
assert pos_neg(-1, 1, True) == False
assert pos_neg(1, 1, True) == False
assert pos_neg(-1, -1, True) == True
assert pos_neg(5, -5, False) == True
assert pos_neg(-6, 6, False) == True
assert pos_neg(-5, -6, False) == False
assert pos_neg(-2, -1, False) == False
assert pos_neg(1, 2, False) == False
assert pos_neg(-5, 6, True) == False
assert pos_neg(-5, -5, True) == True

assert not_string('candy') == 'not candy'
assert not_string('x') == 'not x'
assert not_string('not bad') == 'not bad'
assert not_string('bad') == 'not bad'
assert not_string('not') == 'not'
assert not_string('is not') == 'not is not'
assert not_string('no') == 'not no'

assert missing_char('kitten', 1) == 'ktten'
assert missing_char('kitten', 0) == 'itten'
assert missing_char('kitten', 4) == 'kittn'
assert missing_char('Hi', 0) == 'i'
assert missing_char('Hi', 1) == 'H'
assert missing_char('code', 0) == 'ode'
assert missing_char('code', 1) == 'cde'
assert missing_char('code', 2) == 'coe'
assert missing_char('code', 3) == 'cod'
assert missing_char('chocolate', 8) == 'chocolat'

assert front_back('code') == 'eodc'
assert front_back('a') == 'a'
assert front_back('ab') == 'ba'
assert front_back('abc') == 'cba'
assert front_back('') == ''
assert front_back('Chocolate') == 'ehocolatC'
assert front_back('aavJ') == 'Java'
assert front_back('hello') == 'oellh'

assert front3('Java') == 'JavJavJav'
assert front3('Chocolate') == 'ChoChoCho'
assert front3('abc') == 'abcabcabc'
assert front3('abcXYZ') == 'abcabcabc'
assert front3('ab') == 'ababab'
assert front3('a') == 'aaa'
assert front3('') == ''

assert backAround("cat") == "tcatt"
assert backAround("Hello") == "oHelloo"
assert backAround("a") == "aaa"
assert backAround("abc") == "cabcc"
assert backAround("read") == "dreadd"
assert backAround("boo") == "obooo"

assert or35(3) == True
assert or35(10) == True
assert or35(8) == False
assert or35(15) == True
assert or35(5) == True
assert or35(9) == True
assert or35(4) == False
assert or35(7) == False
assert or35(6) == True
assert or35(17) == False
assert or35(18) == True
assert or35(29) == False
assert or35(20) == True
assert or35(21) == True
assert or35(22) == False
assert or35(45) == True
assert or35(99) == True
assert or35(100) == True
assert or35(101) == False
assert or35(121) == False
assert or35(122) == False
assert or35(123) == True

assert front22("kitten") == "kikittenki"
assert front22("Ha") == "HaHaHa"
assert front22("abc") == "ababcab"
assert front22("ab") == "ababab"
assert front22("a") == "aaa"
assert front22("") == ""
assert front22("Logic") == "LoLogicLo"

assert startHi("hi there") == True
assert startHi("hi") == True
assert startHi("hello hi") == False
assert startHi("he") == False
assert startHi("h") == False
assert startHi("") == False
assert startHi("ho hi") == False
assert startHi("hi ho") == True

assert icyHot(120, -1) == True
assert icyHot(-1, 120) == True
assert icyHot(2, 120) == False
assert icyHot(-1, 100) == False
assert icyHot(-2, -2) == False
assert icyHot(120, 120) == False

assert in1020(12, 99) == True
assert in1020(21, 12) == True
assert in1020(8, 99) == False
assert in1020(99, 10) == True
assert in1020(20, 20) == True
assert in1020(21, 21) == False
assert in1020(9, 9) == False

assert hasTeen(13, 20, 10) == True
assert hasTeen(20, 19, 10) == True
assert hasTeen(20, 10, 13) == True
assert hasTeen(1, 20, 12) == False
assert hasTeen(19, 20, 12) == True
assert hasTeen(12, 20, 19) == True
assert hasTeen(12, 9, 20) == False
assert hasTeen(12, 18, 20) == True
assert hasTeen(14, 2, 20) == True
assert hasTeen(4, 2, 20) == False
assert hasTeen(11, 22, 22) == False

assert loneTeen(13, 99) == True
assert loneTeen(21, 19) == True
assert loneTeen(13, 13) == False
assert loneTeen(14, 20) == True
assert loneTeen(20, 15) == True
assert loneTeen(16, 17) == False
assert loneTeen(16, 9) == True
assert loneTeen(16, 18) == False
assert loneTeen(13, 19) == False
assert loneTeen(13, 20) == True
assert loneTeen(6, 18) == True
assert loneTeen(99, 13) == True
assert loneTeen(99, 99) == False

assert delDel("adelbc") == "abc"
assert delDel("adelHello") == "aHello"
assert delDel("adedbc") == "adedbc"
assert delDel("abcdel") == "abcdel"
assert delDel("add") == "add"
assert delDel("ad") == "ad"
assert delDel("a") == "a"
assert delDel("") == ""
assert delDel("del") == "del"
assert delDel("adel") == "a"
assert delDel("aadelbb") == "aadelbb"

assert mixStart("mix snacks") == True
assert mixStart("pix snacks") == True
assert mixStart("piz snacks") == False
assert mixStart("nix") == True
assert mixStart("ni") == False
assert mixStart("n") == False
assert mixStart("") == False

assert startOz("ozymandias") == "oz"
assert startOz("bzoo") == "z"
assert startOz("oxx") == "o"
assert startOz("oz") == "oz"
assert startOz("ounce") == "o"
assert startOz("o") == "o"
assert startOz("abc") == ""
assert startOz("") == ""
assert startOz("zoo") == ""
assert startOz("aztec") == "z"
assert startOz("zzzz") == "z"
assert startOz("oznic") == "oz"

assert intMax(1, 2, 3) == 3
assert intMax(1, 3, 2) == 3
assert intMax(3, 2, 1) == 3
assert intMax(9, 3, 3) == 9
assert intMax(3, 9, 3) == 9
assert intMax(3, 3, 9) == 9
assert intMax(8, 2, 3) == 8
assert intMax(-3, -1, -2) == -1
assert intMax(6, 2, 5) == 6
assert intMax(5, 6, 2) == 6
assert intMax(5, 2, 6) == 6

assert close10(8, 13) == 8
assert close10(13, 8) == 8
assert close10(13, 7) == 0
assert close10(7, 13) == 0
assert close10(9, 13) == 9
assert close10(13, 8) == 8
assert close10(10, 12) == 10
assert close10(11, 10) == 10
assert close10(5, 21) == 5
assert close10(0, 20) == 0
assert close10(10, 10) == 0

assert in3050(30, 31) == True
assert in3050(30, 41) == False
assert in3050(40, 50) == True
assert in3050(40, 51) == False
assert in3050(39, 50) == False
assert in3050(50, 39) == False
assert in3050(40, 39) == True
assert in3050(49, 48) == True
assert in3050(50, 40) == True
assert in3050(50, 51) == False
assert in3050(35, 36) == True
assert in3050(35, 45) == False

assert max1020(11, 19) == 19
assert max1020(19, 11) == 19
assert max1020(11, 9) == 11
assert max1020(9, 21) == 0
assert max1020(10, 21) == 10
assert max1020(21, 10) == 10
assert max1020(9, 11) == 11
assert max1020(23, 10) == 10
assert max1020(20, 10) == 20
assert max1020(7, 20) == 20
assert max1020(17, 16) == 17

assert stringE("Hello") == True
assert stringE("Heelle") == True
assert stringE("Heelele") == False
assert stringE("Hll") == False
assert stringE("e") == True
assert stringE("") == False

assert lastDigit(7, 17) == True
assert lastDigit(6, 17) == False
assert lastDigit(3, 113) == True
assert lastDigit(114, 113) == False
assert lastDigit(114, 4) == True
assert lastDigit(10, 0) == True
assert lastDigit(11, 0) == False

assert endUp("Hello") == "HeLLO"
assert endUp("hi there") == "hi thERE"
assert endUp("hi") == "HI"
assert endUp("woo hoo") == "woo HOO"
assert endUp("xyz12") == "xyZ12"
assert endUp("x") == "X"
assert endUp("") == ""

assert everyNth("Miracle", 2) == "Mrce"
assert everyNth("abcdefg", 2) == "aceg"
assert everyNth("abcdefg", 3) == "adg"
assert everyNth("Chocolate", 3) == "Cca"
assert everyNth("Chocolates", 3) == "Ccas"
assert everyNth("Chocolates", 4) == "Coe"
assert everyNth("Chocolates", 100) == "C"