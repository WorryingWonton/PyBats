def factorial(n):
    return n * factorial(n - 1) if n > 0 else 1

def bunnyEars(n):
    return 2 + bunnyEars(n - 1) if n > 0 else 0

def fibonacci(n):
    return fibonacci(n - 1) + fibonacci(n - 2) if n > 1 else n

def bunnyEars2(n):
    return 2 + bunnyEars2(n - 1) if n % 2 else 3 + bunnyEars2(n - 1) if n > 0 else 0

def triangle(n):
    return triangle(n - 1) + n if n > 0 else 0

def sumDigits(n):
    return n % 10 + sumDigits(int(n / 10)) if n > 0 else 0

def count7(n):
    return 1 + count7(int(n / 10)) if n % 10 == 7 else (count7(int(n / 10)) if n > 0 else 0)

def count8(n):
    if n < 1:
        return 0
    if n % 10 == 8:
        return 2 + count8(int(n / 10)) if int(n / 10) % 10 == 8 else 1 + count8(int(n / 10))
    return count8(int(n / 10))

def powerN(base, n):
    return base * powerN(base, n - 1) if n > 0 else 1

def countX(str):
    return 1 + countX(str[1:]) if str[:1] == 'x' else (countX(str[1:]) if str else 0)

def countHi(str):
    return 1 + countHi(str[2:]) if str[:2] == 'hi' else (countHi(str[1:]) if str else 0)

def changeXY(str):
    return 'y' + changeXY(str[1:]) if str[:1] == 'x' else (str[0] + changeXY(str[1:]) if str else '')

def changePi(str):
    return '3.14' + changePi(str[2:]) if str[:2] == 'pi' else (str[0] + changePi(str[1:]) if str else '')

def noX(str):
    return str[0] + noX(str[1:]) if str and str[0] != 'x' else (noX(str[1:]) if str else '')

def array6(nums, index):
    return nums[index] == 6 or array6(nums, index + 1) if index < len(nums) else False

def array11(nums, index):
    if index == len(nums):
        return 0
    return 1 + array11(nums, index + 1) if nums[index] == 11 else array11(nums, index + 1)

def array220(nums, index):
    return nums[index + 1] == 10 * nums[index] or array220(nums, index + 1) if index < len(nums) - 1 else False

def allStar(str):
    return str[0] + '*' + allStar(str[1:]) if len(str) > 1 else str[:1]

def pairStar(str):
    if len(str) < 2:
        return str[:1]
    return str[0] + '*' + pairStar(str[1:]) if str[0] == str[1] else str[0] + pairStar(str[1:])

def endX(str):
    return endX(str[1:]) + 'x' if str[:1] == 'x' else (str[0] + endX(str[1:]) if str else '')

def countPairs(str):
    if len(str) < 3:
        return 0
    return 1 + countPairs(str[1:]) if str[0] == str[2] else countPairs(str[1:])

def countAbc(str):
    return 1 + countAbc(str[2:]) if str[:3] in ['abc', 'aba'] else countAbc(str[1:]) if len(str) > 2 else 0

def count11(str):
    return 1 + count11(str[2:]) if str[:2] == '11' else count11(str[1:]) if len(str) > 2 else 0

def stringClean(str):
    if len(str) == 1:
        return str
    return stringClean(str[1:]) if str[0] == str[1] else str[0] + stringClean(str[1:])

def countHi2(str):
    if not str:
        return 0
    if str[:3] == 'xhi':
        return countHi2(str[3:])
    if str[:2] == 'hi':
        return 1 + countHi2(str[2:])
    return countHi2(str[1:])

def parenBit(str):
    if str[0] == '(' and str[-1] == ')':
        return str
    elif str[0] == '(':
        return parenBit(str[:-1])
    elif str[-1] == ')':
        return parenBit(str[1:])
    return parenBit(str[1:-1])

def nestParen(str):
    if not str:
        return True
    if str[0] + str[-1] == '()':
        return nestParen(str[1:-1])
    return False

def strCount(str, sub):
    return 1 + strCount(str[len(sub):], sub) if str[:len(sub)] == sub else strCount(str[1:], sub) if len(str) > 0 else 0

def strCopies(str, sub, n):
    if not str:
        return n == 0
    if str[:len(sub)] == sub:
        return strCopies(str[1:], sub, n - 1)
    return strCopies(str[1:], sub, n)

def strDist(str, sub):
    if str[:len(sub)] == sub and str[-len(sub):] == sub:
        return len(str)
    if str[:len(sub)] == sub:
        return strDist(str[:-1], sub)
    if str[-len(sub):] == sub:
        return strDist(str[1:], sub)
    return strDist(str[1:-1], sub) if len(str) > len(sub) else 0


assert factorial(1) == 1
assert factorial(2) == 2
assert factorial(3) == 6
assert factorial(4) == 24
assert factorial(5) == 120
assert factorial(6) == 720
assert factorial(7) == 5040
assert factorial(8) == 40320
assert factorial(12) == 479001600

assert bunnyEars(0) == 0
assert bunnyEars(1) == 2
assert bunnyEars(2) == 4
assert bunnyEars(3) == 6
assert bunnyEars(4) == 8
assert bunnyEars(5) == 10
assert bunnyEars(12) == 24
assert bunnyEars(50) == 100
assert bunnyEars(234) == 468

assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(4) == 3
assert fibonacci(5) == 5
assert fibonacci(6) == 8
assert fibonacci(7) == 13

assert bunnyEars2(0) == 0
assert bunnyEars2(1) == 2
assert bunnyEars2(2) == 5
assert bunnyEars2(3) == 7
assert bunnyEars2(4) == 10
assert bunnyEars2(5) == 12
assert bunnyEars2(6) == 15
assert bunnyEars2(10) == 25

assert triangle(0) == 0
assert triangle(1) == 1
assert triangle(2) == 3
assert triangle(3) == 6
assert triangle(4) == 10
assert triangle(5) == 15
assert triangle(6) == 21
assert triangle(7) == 28

assert sumDigits(126) == 9
assert sumDigits(49) == 13
assert sumDigits(12) == 3
assert sumDigits(10) == 1
assert sumDigits(1) == 1
assert sumDigits(0) == 0
assert sumDigits(730) == 10
assert sumDigits(1111) == 4
assert sumDigits(11111) == 5
assert sumDigits(10110) == 3
assert sumDigits(235) == 10

assert count7(717) == 2
assert count7(7) == 1
assert count7(123) == 0
assert count7(77) == 2
assert count7(7123) == 1
assert count7(771237) == 3
assert count7(771737) == 4
assert count7(47571) == 2
assert count7(777777) == 6
assert count7(70701277) == 4
assert count7(777576197) == 5
assert count7(99999) == 0
assert count7(99799) == 1

assert count8(8) == 1
assert count8(818) == 2
assert count8(8818) == 4
assert count8(8088) == 4
assert count8(123) == 0
assert count8(81238) == 2
assert count8(88788) == 6
assert count8(8234) == 1
assert count8(2348) == 1
assert count8(23884) == 3
assert count8(0) == 0
assert count8(1818188) == 5
assert count8(8818181) == 5
assert count8(1080) == 1
assert count8(188) == 3
assert count8(88888) == 9
assert count8(9898) == 2
assert count8(78) == 1

assert powerN(3, 1) == 3
assert powerN(3, 2) == 9
assert powerN(3, 3) == 27
assert powerN(2, 1) == 2
assert powerN(2, 2) == 4
assert powerN(2, 3) == 8
assert powerN(2, 4) == 16
assert powerN(2, 5) == 32
assert powerN(10, 1) == 10
assert powerN(10, 2) == 100
assert powerN(10, 3) == 1000

assert countX("xxhixx") == 4
assert countX("xhixhix") == 3
assert countX("hi") == 0
assert countX("h") == 0
assert countX("x") == 1
assert countX("") == 0
assert countX("hihi") == 0
assert countX("hiAAhi12hi") == 0

assert countHi("xxhixx") == 1
assert countHi("xhixhix") == 2
assert countHi("hi") == 1
assert countHi("hihih") == 2
assert countHi("h") == 0
assert countHi("") == 0
assert countHi("ihihihihih") == 4
assert countHi("ihihihihihi") == 5
assert countHi("hiAAhi12hi") == 3
assert countHi("xhixhxihihhhih") == 3
assert countHi("ship") == 1

assert changeXY("codex") == "codey"
assert changeXY("xxhixx") == "yyhiyy"
assert changeXY("xhixhix") == "yhiyhiy"
assert changeXY("hiy") == "hiy"
assert changeXY("h") == "h"
assert changeXY("x") == "y"
assert changeXY("") == ""
assert changeXY("xxx") == "yyy"
assert changeXY("yyhxyi") == "yyhyyi"
assert changeXY("hihi") == "hihi"

assert changePi("xpix") == "x3.14x"
assert changePi("pipi") == "3.143.14"
assert changePi("pip") == "3.14p"
assert changePi("pi") == "3.14"
assert changePi("hip") == "hip"
assert changePi("p") == "p"
assert changePi("x") == "x"
assert changePi("") == ""
assert changePi("pixx") == "3.14xx"
assert changePi("xyzzy") == "xyzzy"

assert noX("xaxb") == "ab"
assert noX("abc") == "abc"
assert noX("xx") == ""
assert noX("") == ""
assert noX("axxbxx") == "ab"
assert noX("Hellox") == "Hello"

assert array6([1, 6, 4], 0) == True
assert array6([1, 4], 0) == False
assert array6([6], 0) == True
assert array6([], 0) == False
assert array6([6, 2, 2], 0) == True
assert array6([2, 5], 0) == False
assert array6([1, 9, 4, 6, 6], 0) == True
assert array6([2, 5, 6], 0) == True

assert array11([1, 2, 11], 0) == 1
assert array11([11, 11], 0) == 2
assert array11([1, 2, 3, 4], 0) == 0
assert array11([1, 11, 3, 11, 11], 0) == 3
assert array11([11], 0) == 1
assert array11([1], 0) == 0
assert array11([], 0) == 0
assert array11([11, 2, 3, 4, 11, 5], 0) == 2
assert array11([11, 5, 11], 0) == 2

assert array220([1, 2, 20], 0) == True
assert array220([3, 30], 0) == True
assert array220([3], 0) == False
assert array220([], 0) == False
assert array220([3, 3, 30, 4], 0) == True
assert array220([2, 19, 4], 0) == False
assert array220([20, 2, 21], 0) == False
assert array220([20, 2, 21, 210], 0) == True
assert array220([2, 200, 2000], 0) == True
assert array220([0, 0], 0) == True
assert array220([1, 2, 3, 4, 5, 6], 0) == False
assert array220([1, 2, 3, 4, 5, 50, 6], 0) == True
assert array220([1, 2, 3, 4, 5, 51, 6], 0) == False
assert array220([1, 2, 3, 4, 4, 50, 500, 6], 0) == True

assert allStar("hello") == "h*e*l*l*o"
assert allStar("abc") == "a*b*c"
assert allStar("ab") == "a*b"
assert allStar("a") == "a"
assert allStar("") == ""
assert allStar("3.14") == "3*.*1*4"
assert allStar("Chocolate") == "C*h*o*c*o*l*a*t*e"
assert allStar("1234") == "1*2*3*4"

assert pairStar("hello") == "hel*lo"
assert pairStar("xxyy") == "x*xy*y"
assert pairStar("aaaa") == "a*a*a*a"
assert pairStar("aaab") == "a*a*ab"
assert pairStar("aa") == "a*a"
assert pairStar("a") == "a"
assert pairStar("") == ""
assert pairStar("noadjacent") == "noadjacent"
assert pairStar("abba") == "ab*ba"
assert pairStar("abbba") == "ab*b*ba"

assert endX("xxre") == "rexx"
assert endX("xxhixx") == "hixxxx"
assert endX("xhixhix") == "hihixxx"
assert endX("hiy") == "hiy"
assert endX("h") == "h"
assert endX("x") == "x"
assert endX("xx") == "xx"
assert endX("") == ""
assert endX("bxx") == "bxx"
assert endX("bxax") == "baxx"
assert endX("axaxax") == "aaaxxx"
assert endX("xxhxi") == "hixxx"

assert countPairs("axa") == 1
assert countPairs("axax") == 2
assert countPairs("axbx") == 1
assert countPairs("hi") == 0
assert countPairs("hihih") == 3
assert countPairs("ihihhh") == 3
assert countPairs("ihjxhh") == 0
assert countPairs("") == 0
assert countPairs("a") == 0
assert countPairs("aa") == 0
assert countPairs("aaa") == 1

assert countAbc("abc") == 1
assert countAbc("abcxxabc") == 2
assert countAbc("abaxxaba") == 2
assert countAbc("abaxxababa") == 3
assert countAbc("abaxxababax") == 3
assert countAbc("ababc") == 2
assert countAbc("abxbc") == 0
assert countAbc("aaabc") == 1
assert countAbc("hello") == 0
assert countAbc("") == 0
assert countAbc("ab") == 0
assert countAbc("aba") == 1
assert countAbc("aca") == 0
assert countAbc("aaa") == 0

assert count11("11abc11") == 2
assert count11("abc11x11x11") == 3
assert count11("111") == 1
assert count11("1111") == 2
assert count11("1") == 0
assert count11("") == 0
assert count11("hi") == 0
assert count11("11x111x1111") == 4
assert count11("1x111") == 1
assert count11("1Hello1") == 0
assert count11("Hello") == 0

assert stringClean("yyzzza") == "yza"
assert stringClean("abbbcdd") == "abcd"
assert stringClean("Hello") == "Helo"
assert stringClean("XXabcYY") == "XabcY"
assert stringClean("112ab445") == "12ab45"
assert stringClean("Hello Bookkeeper") == "Helo Bokeper"

assert countHi2("ahixhi") == 1
assert countHi2("ahibhi") == 2
assert countHi2("xhixhi") == 0
assert countHi2("hixhi") == 1
assert countHi2("hixhhi") == 2
assert countHi2("hihihi") == 3
assert countHi2("hihihix") == 3
assert countHi2("xhihihix") == 2
assert countHi2("xxhi") == 0
assert countHi2("hixxhi") == 1
assert countHi2("hi") == 1
assert countHi2("xxxx") == 0
assert countHi2("h") == 0
assert countHi2("x") == 0
assert countHi2("") == 0
assert countHi2("Hellohi") == 1

assert parenBit("xyz(abc)123") == "(abc)"
assert parenBit("x(hello)") == "(hello)"
assert parenBit("(xy)1") == "(xy)"
assert parenBit("not really (possible)") == "(possible)"
assert parenBit("(abc)") == "(abc)"
assert parenBit("(abc)xyz") == "(abc)"
assert parenBit("(abc)x") == "(abc)"
assert parenBit("(x)") == "(x)"
assert parenBit("()") == "()"
assert parenBit("res (ipsa) loquitor") == "(ipsa)"
assert parenBit("hello(not really)there") == "(not really)"
assert parenBit("ab(ab)ab") == "(ab)"

assert nestParen("(())") == True
assert nestParen("((()))") == True
assert nestParen("(((x))") == False
assert nestParen("((())") == False
assert nestParen("((()()") == False
assert nestParen("()") == True
assert nestParen("") == True
assert nestParen("(yy)") == False
assert nestParen("(())") == True
assert nestParen("(((y))") == False
assert nestParen("((y)))") == False
assert nestParen("((()))") == True
assert nestParen("(())))") == False
assert nestParen("((yy())))") == False
assert nestParen("(((())))") == True

assert strCount("catcowcat", "cat") == 2
assert strCount("catcowcat", "cow") == 1
assert strCount("catcowcat", "dog") == 0
assert strCount("cacatcowcat", "cat") == 2
assert strCount("xyx", "x") == 2
assert strCount("iiiijj", "i") == 4
assert strCount("iiiijj", "ii") == 2
assert strCount("iiiijj", "iii") == 1
assert strCount("iiiijj", "j") == 2
assert strCount("iiiijj", "jj") == 1
assert strCount("aaabababab", "ab") == 4
assert strCount("aaabababab", "aa") == 1
assert strCount("aaabababab", "a") == 6
assert strCount("aaabababab", "b") == 4

assert strCopies("catcowcat", "cat", 2) == True
assert strCopies("catcowcat", "cow", 2) == False
assert strCopies("catcowcat", "cow", 1) == True
assert strCopies("iiijjj", "i", 3) == True
assert strCopies("iiijjj", "i", 4) == False
assert strCopies("iiijjj", "ii", 2) == True
assert strCopies("iiijjj", "ii", 3) == False
assert strCopies("iiijjj", "x", 3) == False
assert strCopies("iiijjj", "x", 0) == True
assert strCopies("iiiiij", "iii", 3) == True
assert strCopies("iiiiij", "iii", 4) == False
assert strCopies("ijiiiiij", "iiii", 2) == True
assert strCopies("ijiiiiij", "iiii", 3) == False
assert strCopies("dogcatdogcat", "dog", 2) == True

assert strDist("catcowcat", "cat") == 9
assert strDist("catcowcat", "cow") == 3
assert strDist("cccatcowcatxx", "cat") == 9
assert strDist("abccatcowcatcatxyz", "cat") == 12
assert strDist("xyx", "x") == 3
assert strDist("xyx", "y") == 1
assert strDist("xyx", "z") == 0
assert strDist("z", "z") == 1
assert strDist("x", "z") == 0
assert strDist("", "z") == 0
assert strDist("hiHellohihihi", "hi") == 13
assert strDist("hiHellohihihi", "hih") == 5
assert strDist("hiHellohihihi", "o") == 1
assert strDist("hiHellohihihi", "ll") == 2