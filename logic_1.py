def cigar_party(cigars, is_weekend):
    return cigars in range(40, 61) if not is_weekend else cigars > 39

def date_fashion(you, date):
    return 2 if max(you, date) > 7 and min(you, date) > 2 else (1 if min(you, date) > 2 else 0)

def squirrel_play(temp, is_summer):
    return temp in range(60, 91) if not is_summer else temp in range(60, 101)

def caught_speeding(speed, is_birthday):
    bdm = 5 if is_birthday else 0
    return 1 if speed in range(61 + bdm, 81 + bdm) else 2 if speed > 80 + bdm else 0

def sorta_sum(a, b):
    return a + b if a + b not in range(10, 20) else 20

def alarm_clock(day, vacation):
    return ('10:00' if day in [6, 0] else '7:00') if not vacation else ('10:00' if day in range(1, 6) else 'off')

def love6(a, b):
    return 6 in [a, b] or a + b == 6 or abs(a - b) == 6

def in1to10(n, outside_mode):
    return n in range(1, 11) if not outside_mode else n not in range(2, 10)

def specialEleven(n):
    return not n % 11 or not n % 11 - 1

def more20(n):
    return not n % 20 - 1 or not n % 20 - 2

def old35(n):
    return (not n % 3 or not n % 5) and n % 15 > 0

def less20(n):
    return n % 20 + 1 == 20 or n % 20 + 2 == 20

def near_ten(num):
    return 10 - num % 10 in range(3) or num % 10 in range(3)

def teenSum(a, b):
    return a + b if (a not in range(13, 20) and b not in range(13, 20)) else 19

def answerCell(isMorning, isMom, isAsleep):
    return not isAsleep and (isMom or not isMorning)

def teaParty(tea, candy):
    return 0 if tea < 5 or candy < 5 else (2 if tea >= 2 * candy or candy >= 2 * tea else 1)

def fizzString(str):
    return (('Fizz' if str[0:1] == 'f' else '') + ('Buzz' if str[-1:] == 'b' else '')) or str

def fizzString2(n):
    return (('Fizz' * (not n % 3) + 'Buzz' * (not n % 5)) or str(n)) + '!'

def twoAsOne(a, b, c):
    return a + b == c or a + c == b or b + c == a

def inOrder(a, b, c, b0k):
    return (a < b < c) if not b0k else b < c

def inOrderEqual(a, b, c, equalOk):
    return a < b < c if not equalOk else a <= b <= c

def lastDigit(a, b, c):
    return a % 10 == b % 10 or c % 10 == a % 10 or b % 10 == c % 10

def lessBy10(a, b, c):
    return abs(a - b) > 9 or abs(b - c) > 9 or abs(a - c) > 9

def withoutDoubles(die1, die2, noDoubles):
    return ((1 if die1 == 6 and die1 == die2 else die1 + 1) + die2) if (noDoubles and die1 == die2) else die1 + die2

def maxMod5(a, b):
    return (max(a, b) if a % 5 != b % 5 else min(a, b)) if a != b else 0

def redTicket(a, b, c):
    return 10 if a == b == c == 2 else (5 if a == b == c else (1 if a != b and a != c else 0))

def greenTicket(a, b, c):
    return 20 if a == b == c else 10 if a == b or b == c or a == c else 0

def blueTicket(a, b, c):
    return 10 if a + b == 10 or b + c == 10 or c + a == 10 else 5 if a - c == 10 or b - c == 10 else 0

def shareDigit(a, b):
    al = int(a / 10) % 10
    bl = int(b / 10) % 10
    return a % 10 == b % 10 or al == bl or al == b % 10 or bl == a % 10

def sumLimit(a, b):
    return a + b if len(str(a)) == len(str(a + b)) else a


assert cigar_party(30, False) == False
assert cigar_party(50, False) == True
assert cigar_party(70, True) == True
assert cigar_party(30, True) == False
assert cigar_party(50, True) == True
assert cigar_party(60, False) == True
assert cigar_party(61, False) == False
assert cigar_party(40, False) == True
assert cigar_party(39, False) == False
assert cigar_party(40, True) == True
assert cigar_party(39, True) == False

assert date_fashion(5, 10) == 2
assert date_fashion(5, 2) == 0
assert date_fashion(5, 5) == 1
assert date_fashion(3, 3) == 1
assert date_fashion(10, 2) == 0
assert date_fashion(2, 9) == 0
assert date_fashion(9, 9) == 2
assert date_fashion(10, 5) == 2
assert date_fashion(2, 2) == 0
assert date_fashion(3, 7) == 1
assert date_fashion(2, 7) == 0
assert date_fashion(6, 2) == 0

assert squirrel_play(70, False) == True
assert squirrel_play(95, False) == False
assert squirrel_play(95, True) == True
assert squirrel_play(90, False) == True
assert squirrel_play(90, True) == True
assert squirrel_play(50, False) == False
assert squirrel_play(50, True) == False
assert squirrel_play(100, False) == False
assert squirrel_play(100, True) == True
assert squirrel_play(105, True) == False
assert squirrel_play(59, False) == False
assert squirrel_play(59, True) == False
assert squirrel_play(60, False) == True

assert caught_speeding(60, False) == 0
assert caught_speeding(65, False) == 1
assert caught_speeding(65, True) == 0
assert caught_speeding(80, False) == 1
assert caught_speeding(85, False) == 2
assert caught_speeding(85, True) == 1
assert caught_speeding(70, False) == 1
assert caught_speeding(75, False) == 1
assert caught_speeding(75, True) == 1
assert caught_speeding(40, False) == 0
assert caught_speeding(40, True) == 0
assert caught_speeding(90, False) == 2

assert sorta_sum(3, 4) == 7
assert sorta_sum(9, 4) == 20
assert sorta_sum(10, 11) == 21
assert sorta_sum(12, -3) == 9
assert sorta_sum(-3, 12) == 9
assert sorta_sum(4, 5) == 9
assert sorta_sum(4, 6) == 20
assert sorta_sum(14, 7) == 21
assert sorta_sum(14, 6) == 20

assert alarm_clock(1, False) == '7:00'
assert alarm_clock(5, False) == '7:00'
assert alarm_clock(0, False) == '10:00'
assert alarm_clock(6, False) == '10:00'
assert alarm_clock(0, True) == 'off'
assert alarm_clock(6, True) == 'off'
assert alarm_clock(1, True) == '10:00'
assert alarm_clock(3, True) == '10:00'
assert alarm_clock(5, True) == '10:00'

assert love6(6, 4) == True
assert love6(4, 5) == False
assert love6(1, 5) == True
assert love6(1, 6) == True
assert love6(1, 8) == False
assert love6(1, 7) == True
assert love6(7, 5) == False
assert love6(8, 2) == True
assert love6(6, 6) == True
assert love6(-6, 2) == False
assert love6(-4, -10) == True
assert love6(-7, 1) == False
assert love6(7, -1) == True
assert love6(-6, 12) == True
assert love6(-2, -4) == False
assert love6(7, 1) == True
assert love6(0, 9) == False
assert love6(8, 3) == False
assert love6(3, 3) == True
assert love6(3, 4) == False

assert in1to10(5, False) == True
assert in1to10(11, False) == False
assert in1to10(11, True) == True
assert in1to10(10, False) == True
assert in1to10(10, True) == True
assert in1to10(9, False) == True
assert in1to10(9, True) == False
assert in1to10(1, False) == True
assert in1to10(1, True) == True
assert in1to10(0, False) == False
assert in1to10(0, True) == True
assert in1to10(-1, False) == False
assert in1to10(-1, True) == True
assert in1to10(99, False) == False
assert in1to10(-99, True) == True

assert specialEleven(22) == True
assert specialEleven(23) == True
assert specialEleven(24) == False
assert specialEleven(21) == False
assert specialEleven(11) == True
assert specialEleven(12) == True
assert specialEleven(10) == False
assert specialEleven(9) == False
assert specialEleven(8) == False
assert specialEleven(0) == True
assert specialEleven(1) == True
assert specialEleven(2) == False
assert specialEleven(121) == True
assert specialEleven(122) == True
assert specialEleven(123) == False
assert specialEleven(46) == False
assert specialEleven(49) == False
assert specialEleven(52) == False
assert specialEleven(54) == False
assert specialEleven(55) == True

assert more20(20) == False
assert more20(21) == True
assert more20(22) == True
assert more20(23) == False
assert more20(25) == False
assert more20(30) == False
assert more20(31) == False
assert more20(59) == False
assert more20(60) == False
assert more20(61) == True
assert more20(62) == True
assert more20(1020) == False
assert more20(1021) == True
assert more20(1000) == False
assert more20(1001) == True
assert more20(50) == False
assert more20(55) == False
assert more20(40) == False
assert more20(41) == True
assert more20(39) == False
assert more20(42) == True

assert old35(3) == True
assert old35(10) == True
assert old35(15) == False
assert old35(5) == True
assert old35(9) == True
assert old35(8) == False
assert old35(7) == False
assert old35(6) == True
assert old35(17) == False
assert old35(18) == True
assert old35(29) == False
assert old35(20) == True
assert old35(21) == True
assert old35(22) == False
assert old35(45) == False
assert old35(99) == True

assert less20(18) == True
assert less20(19) == True
assert less20(20) == False
assert less20(8) == False
assert less20(17) == False
assert less20(23) == False
assert less20(25) == False
assert less20(30) == False
assert less20(31) == False
assert less20(58) == True
assert less20(59) == True
assert less20(60) == False
assert less20(61) == False
assert less20(62) == False
assert less20(1017) == False
assert less20(1018) == True
assert less20(1019) == True
assert less20(1020) == False
assert less20(1021) == False
assert less20(1022) == False
assert less20(1023) == False
assert less20(37) == False

assert near_ten(12) == True
assert near_ten(17) == False
assert near_ten(19) == True
assert near_ten(31) == True
assert near_ten(6) == False
assert near_ten(10) == True
assert near_ten(11) == True
assert near_ten(21) == True
assert near_ten(22) == True
assert near_ten(23) == False
assert near_ten(54) == False
assert near_ten(155) == False
assert near_ten(158) == True
assert near_ten(3) == False
assert near_ten(1) == True

assert teenSum(3, 4) == 7
assert teenSum(10, 13) == 19
assert teenSum(13, 2) == 19
assert teenSum(3, 19) == 19
assert teenSum(13, 13) == 19
assert teenSum(10, 10) == 20
assert teenSum(6, 14) == 19
assert teenSum(15, 2) == 19
assert teenSum(19, 19) == 19
assert teenSum(19, 20) == 19
assert teenSum(2, 18) == 19
assert teenSum(12, 4) == 16
assert teenSum(2, 20) == 22
assert teenSum(2, 17) == 19
assert teenSum(2, 16) == 19
assert teenSum(6, 7) == 13

assert answerCell(False, False, False) == True
assert answerCell(False, False, True) == False
assert answerCell(True, False, False) == False
assert answerCell(True, True, False) == True
assert answerCell(False, True, False) == True
assert answerCell(True, True, True) == False

assert teaParty(6, 8) == 1
assert teaParty(3, 8) == 0
assert teaParty(20, 6) == 2
assert teaParty(12, 6) == 2
assert teaParty(11, 6) == 1
assert teaParty(11, 4) == 0
assert teaParty(4, 5) == 0
assert teaParty(5, 5) == 1
assert teaParty(6, 6) == 1
assert teaParty(5, 10) == 2
assert teaParty(5, 9) == 1
assert teaParty(10, 4) == 0
assert teaParty(10, 20) == 2

assert fizzString("fig") == "Fizz"
assert fizzString("dib") == "Buzz"
assert fizzString("fib") == "FizzBuzz"
assert fizzString("abc") == "abc"
assert fizzString("fooo") == "Fizz"
assert fizzString("booo") == "booo"
assert fizzString("ooob") == "Buzz"
assert fizzString("fooob") == "FizzBuzz"
assert fizzString("f") == "Fizz"
assert fizzString("b") == "Buzz"
assert fizzString("") == ""
assert fizzString("abcb") == "Buzz"
assert fizzString("Hello") == "Hello"
assert fizzString("Hellob") == "Buzz"
assert fizzString("af") == "af"
assert fizzString("bf") == "bf"
assert fizzString("fb") == "FizzBuzz"

assert fizzString2(1) == "1!"
assert fizzString2(2) == "2!"
assert fizzString2(3) == "Fizz!"
assert fizzString2(4) == "4!"
assert fizzString2(5) == "Buzz!"
assert fizzString2(6) == "Fizz!"
assert fizzString2(7) == "7!"
assert fizzString2(8) == "8!"
assert fizzString2(9) == "Fizz!"
assert fizzString2(15) == "FizzBuzz!"
assert fizzString2(16) == "16!"
assert fizzString2(18) == "Fizz!"
assert fizzString2(19) == "19!"
assert fizzString2(21) == "Fizz!"
assert fizzString2(44) == "44!"
assert fizzString2(45) == "FizzBuzz!"
assert fizzString2(100) == "Buzz!"

assert twoAsOne(1, 2, 3) == True
assert twoAsOne(3, 1, 2) == True
assert twoAsOne(3, 2, 2) == False
assert twoAsOne(2, 3, 1) == True
assert twoAsOne(5, 3, -2) == True
assert twoAsOne(5, 3, -3) == False
assert twoAsOne(2, 5, 3) == True
assert twoAsOne(9, 5, 5) == False
assert twoAsOne(9, 4, 5) == True
assert twoAsOne(5, 4, 9) == True
assert twoAsOne(3, 3, 0) == True
assert twoAsOne(3, 3, 2) == False

assert inOrder(1, 2, 4, False) == True
assert inOrder(1, 2, 1, False) == False
assert inOrder(1, 1, 2, True) == True
assert inOrder(3, 2, 4, False) == False
assert inOrder(2, 3, 4, False) == True
assert inOrder(3, 2, 4, True) == True
assert inOrder(4, 2, 2, True) == False
assert inOrder(4, 5, 2, True) == False
assert inOrder(2, 4, 6, True) == True
assert inOrder(7, 9, 10, False) == True
assert inOrder(7, 5, 6, True) == True
assert inOrder(7, 5, 4, True) == False

assert inOrderEqual(2, 5, 11, False) == True
assert inOrderEqual(5, 7, 6, False) == False
assert inOrderEqual(5, 5, 7, True) == True
assert inOrderEqual(5, 5, 7, False) == False
assert inOrderEqual(2, 5, 4, False) == False
assert inOrderEqual(3, 4, 3, False) == False
assert inOrderEqual(3, 4, 4, False) == False
assert inOrderEqual(3, 4, 3, True) == False
assert inOrderEqual(3, 4, 4, True) == True
assert inOrderEqual(1, 5, 5, True) == True
assert inOrderEqual(5, 5, 5, True) == True
assert inOrderEqual(2, 2, 1, True) == False
assert inOrderEqual(9, 2, 2, True) == False
assert inOrderEqual(0, 1, 0, True) == False

assert lastDigit(23, 19, 13) == True
assert lastDigit(23, 19, 12) == False
assert lastDigit(23, 19, 3) == True
assert lastDigit(23, 19, 39) == True
assert lastDigit(1, 2, 3) == False
assert lastDigit(1, 1, 2) == True
assert lastDigit(1, 2, 2) == True
assert lastDigit(14, 25, 43) == False
assert lastDigit(14, 25, 45) == True
assert lastDigit(248, 106, 1002) == False
assert lastDigit(248, 106, 1008) == True
assert lastDigit(10, 11, 20) == True
assert lastDigit(0, 11, 0) == True

assert lessBy10(1, 7, 11) == True
assert lessBy10(1, 7, 10) == False
assert lessBy10(11, 1, 7) == True
assert lessBy10(10, 7, 1) == False
assert lessBy10(-10, 2, 2) == True
assert lessBy10(2, 11, 11) == False
assert lessBy10(3, 3, 30) == True
assert lessBy10(3, 3, 3) == False
assert lessBy10(10, 1, 11) == True
assert lessBy10(10, 11, 1) == True
assert lessBy10(10, 11, 2) == False
assert lessBy10(3, 30, 3) == True
assert lessBy10(2, 2, -8) == True
assert lessBy10(2, 8, 12) == True

assert withoutDoubles(2, 3, True) == 5
assert withoutDoubles(3, 3, True) == 7
assert withoutDoubles(3, 3, False) == 6
assert withoutDoubles(2, 3, False) == 5
assert withoutDoubles(5, 4, True) == 9
assert withoutDoubles(5, 4, False) == 9
assert withoutDoubles(5, 5, True) == 11
assert withoutDoubles(5, 5, False) == 10
assert withoutDoubles(6, 6, True) == 7
assert withoutDoubles(6, 6, False) == 12
assert withoutDoubles(1, 6, True) == 7
assert withoutDoubles(6, 1, False) == 7

assert maxMod5(2, 3) == 3
assert maxMod5(6, 2) == 6
assert maxMod5(3, 2) == 3
assert maxMod5(8, 12) == 12
assert maxMod5(7, 12) == 7
assert maxMod5(11, 6) == 6
assert maxMod5(2, 7) == 2
assert maxMod5(7, 7) == 0
assert maxMod5(9, 1) == 9
assert maxMod5(9, 14) == 9
assert maxMod5(1, 2) == 2

assert redTicket(2, 2, 2) == 10
assert redTicket(2, 2, 1) == 0
assert redTicket(0, 0, 0) == 5
assert redTicket(2, 0, 0) == 1
assert redTicket(1, 1, 1) == 5
assert redTicket(1, 2, 1) == 0
assert redTicket(1, 2, 0) == 1
assert redTicket(0, 2, 2) == 1
assert redTicket(1, 2, 2) == 1
assert redTicket(0, 2, 0) == 0
assert redTicket(1, 1, 2) == 0

assert greenTicket(1, 2, 3) == 0
assert greenTicket(2, 2, 2) == 20
assert greenTicket(1, 1, 2) == 10
assert greenTicket(2, 1, 1) == 10
assert greenTicket(1, 2, 1) == 10
assert greenTicket(3, 2, 1) == 0
assert greenTicket(0, 0, 0) == 20
assert greenTicket(2, 0, 0) == 10
assert greenTicket(0, 9, 10) == 0
assert greenTicket(0, 10, 0) == 10
assert greenTicket(9, 9, 9) == 20
assert greenTicket(9, 0, 9) == 10

assert blueTicket(9, 1, 0) == 10
assert blueTicket(9, 2, 0) == 0
assert blueTicket(6, 1, 4) == 10
assert blueTicket(6, 1, 5) == 0
assert blueTicket(10, 0, 0) == 10
assert blueTicket(15, 0, 5) == 5
assert blueTicket(5, 15, 5) == 10
assert blueTicket(4, 11, 1) == 5
assert blueTicket(13, 2, 3) == 5
assert blueTicket(8, 4, 3) == 0
assert blueTicket(8, 4, 2) == 10
assert blueTicket(8, 4, 1) == 0

assert shareDigit(12, 23) == True
assert shareDigit(12, 43) == False
assert shareDigit(12, 44) == False
assert shareDigit(23, 12) == True
assert shareDigit(23, 24) == True
assert shareDigit(23, 39) == True
assert shareDigit(23, 19) == False
assert shareDigit(30, 90) == True
assert shareDigit(30, 91) == False
assert shareDigit(55, 55) == True
assert shareDigit(55, 44) == False

assert sumLimit(2, 3) == 5
assert sumLimit(8, 3) == 8
assert sumLimit(8, 1) == 9
assert sumLimit(11, 39) == 50
assert sumLimit(11, 99) == 11
assert sumLimit(0, 0) == 0
assert sumLimit(99, 0) == 99
assert sumLimit(99, 1) == 99
assert sumLimit(123, 1) == 124
assert sumLimit(1, 123) == 1
assert sumLimit(23, 60) == 83
assert sumLimit(23, 80) == 23
assert sumLimit(9000, 1) == 9001
assert sumLimit(90000000, 1) == 90000001
assert sumLimit(9000, 1000) == 9000