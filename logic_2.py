def make_bricks(small, big, goal):
    return goal % 5 <= small and goal - 5 * big <= small

def lone_sum(a, b, c):
    return (0 if a in (b, c) else a) + (0 if b in (a, c) else b) + (0 if c in (a, b) else c)

def lucky_sum(a, b, c):
    return 0 if a == 13 else a + (0 if b == 13 else b + (0 if c == 13 else c))

def no_teen_sum(a, b, c):
    return no_teen_sum_helper(a) + no_teen_sum_helper(b) + no_teen_sum_helper(c)

def no_teen_sum_helper(value):
    return value if value not in [13, 14, 17, 18, 19] else 0

def round_sum(a, b, c):
    return round_sum_helper(a) + round_sum_helper(b) + round_sum_helper(c)

def round_sum_helper(num):
    return num - num % 10 if num % 10 < 5 else num + 10 - num % 10

def close_far(a, b, c):
    return (abs(a - b) < 2 or abs(a - c) < 2) and abs(b - c) > 1 and (abs(a - b) > 1 or abs(a - c) > 1)

def blackjack(a, b):
    return min(a if a < 22 else 0, b if b < 22 else 0, key=lambda x: 21 - x)

def evenlySpaced(a, b, c):
    return (a + b + c) / 3 in (a, b, c)

def make_chocolate(small, big, goal):
    return (goal - 5 * big if 5 * big <= goal else goal % 5) if (goal % 5 <= small and goal - 5 * big <= small) else -1


assert make_bricks(3, 1, 8) == True
assert make_bricks(3, 1, 9) == False
assert make_bricks(3, 2, 10) == True
assert make_bricks(3, 2, 8) == True
assert make_bricks(3, 2, 9) == False
assert make_bricks(6, 1, 11) == True
assert make_bricks(6, 0, 11) == False
assert make_bricks(1, 4, 11) == True
assert make_bricks(0, 3, 10) == True
assert make_bricks(1, 4, 12) == False
assert make_bricks(3, 1, 7) == True
assert make_bricks(1, 1, 7) == False
assert make_bricks(2, 1, 7) == True
assert make_bricks(7, 1, 11) == True
assert make_bricks(7, 1, 8) == True
assert make_bricks(7, 1, 13) == False
assert make_bricks(43, 1, 46) == True
assert make_bricks(40, 1, 46) == False
assert make_bricks(40, 2, 47) == True
assert make_bricks(40, 2, 50) == True
assert make_bricks(40, 2, 52) == False
assert make_bricks(22, 2, 33) == False
assert make_bricks(0, 2, 10) == True
assert make_bricks(1000000, 1000, 1000100) == True
assert make_bricks(2, 1000000, 100003) == False
assert make_bricks(20, 0, 19) == True
assert make_bricks(20, 0, 21) == False
assert make_bricks(20, 4, 51) == False
assert make_bricks(20, 4, 39) == True

assert lone_sum(1, 2, 3) == 6
assert lone_sum(3, 2, 3) == 2
assert lone_sum(3, 3, 3) == 0
assert lone_sum(9, 2, 2) == 9
assert lone_sum(2, 2, 9) == 9
assert lone_sum(2, 9, 2) == 9
assert lone_sum(2, 9, 3) == 14
assert lone_sum(4, 2, 3) == 9
assert lone_sum(1, 3, 1) == 3

assert lucky_sum(1, 2, 3) == 6
assert lucky_sum(1, 2, 13) == 3
assert lucky_sum(1, 13, 3) == 1
assert lucky_sum(1, 13, 13) == 1
assert lucky_sum(6, 5, 2) == 13
assert lucky_sum(13, 2, 3) == 0
assert lucky_sum(13, 2, 13) == 0
assert lucky_sum(13, 13, 2) == 0
assert lucky_sum(9, 4, 13) == 13
assert lucky_sum(8, 13, 2) == 8
assert lucky_sum(7, 2, 1) == 10
assert lucky_sum(3, 3, 13) == 6

assert no_teen_sum(1, 2, 3) == 6
assert no_teen_sum(2, 13, 1) == 3
assert no_teen_sum(2, 1, 14) == 3
assert no_teen_sum(2, 1, 15) == 18
assert no_teen_sum(2, 1, 16) == 19
assert no_teen_sum(2, 1, 17) == 3
assert no_teen_sum(17, 1, 2) == 3
assert no_teen_sum(2, 15, 2) == 19
assert no_teen_sum(16, 17, 18) == 16
assert no_teen_sum(17, 18, 19) == 0
assert no_teen_sum(15, 16, 1) == 32
assert no_teen_sum(15, 15, 19) == 30
assert no_teen_sum(15, 19, 16) == 31
assert no_teen_sum(5, 17, 18) == 5
assert no_teen_sum(17, 18, 16) == 16
assert no_teen_sum(17, 19, 18) == 0

assert round_sum(16, 17, 18) == 60
assert round_sum(12, 13, 14) == 30
assert round_sum(6, 4, 4) == 10
assert round_sum(4, 6, 5) == 20
assert round_sum(4, 4, 6) == 10
assert round_sum(9, 4, 4) == 10
assert round_sum(0, 0, 1) == 0
assert round_sum(0, 9, 0) == 10
assert round_sum(10, 10, 19) == 40
assert round_sum(20, 30, 40) == 90
assert round_sum(45, 21, 30) == 100
assert round_sum(23, 11, 26) == 60
assert round_sum(23, 24, 25) == 70
assert round_sum(25, 24, 25) == 80
assert round_sum(23, 24, 29) == 70
assert round_sum(11, 24, 36) == 70
assert round_sum(24, 36, 32) == 90
assert round_sum(14, 12, 26) == 50
assert round_sum(12, 10, 24) == 40

assert close_far(1, 2, 10) == True
assert close_far(1, 2, 3) == False
assert close_far(4, 1, 3) == True
assert close_far(4, 5, 3) == False
assert close_far(4, 3, 5) == False
assert close_far(-1, 10, 0) == True
assert close_far(0, -1, 10) == True
assert close_far(10, 10, 8) == True
assert close_far(10, 8, 9) == False
assert close_far(8, 9, 10) == False
assert close_far(8, 9, 7) == False
assert close_far(8, 6, 9) == True

assert blackjack(19, 21) == 21
assert blackjack(21, 19) == 21
assert blackjack(19, 22) == 19
assert blackjack(22, 19) == 19
assert blackjack(22, 50) == 0
assert blackjack(22, 22) == 0
assert blackjack(33, 1) == 1
assert blackjack(1, 2) == 2
assert blackjack(34, 33) == 0
assert blackjack(17, 19) == 19
assert blackjack(18, 17) == 18
assert blackjack(16, 23) == 16
assert blackjack(3, 4) == 4
assert blackjack(3, 2) == 3
assert blackjack(21, 20) == 21

assert evenlySpaced(2, 4, 6) == True
assert evenlySpaced(4, 6, 2) == True
assert evenlySpaced(4, 6, 3) == False
assert evenlySpaced(6, 2, 4) == True
assert evenlySpaced(6, 2, 8) == False
assert evenlySpaced(2, 2, 2) == True
assert evenlySpaced(2, 2, 3) == False
assert evenlySpaced(9, 10, 11) == True
assert evenlySpaced(10, 9, 11) == True
assert evenlySpaced(10, 9, 9) == False
assert evenlySpaced(2, 4, 4) == False
assert evenlySpaced(2, 2, 4) == False
assert evenlySpaced(3, 6, 12) == False
assert evenlySpaced(12, 3, 6) == False

assert make_chocolate(4, 1, 9) == 4
assert make_chocolate(4, 1, 10) == -1
assert make_chocolate(4, 1, 7) == 2
assert make_chocolate(6, 2, 7) == 2
assert make_chocolate(4, 1, 5) == 0
assert make_chocolate(4, 1, 4) == 4
assert make_chocolate(5, 4, 9) == 4
assert make_chocolate(9, 3, 18) == 3
assert make_chocolate(3, 1, 9) == -1
assert make_chocolate(1, 2, 7) == -1
assert make_chocolate(1, 2, 6) == 1
assert make_chocolate(1, 2, 5) == 0
assert make_chocolate(6, 1, 10) == 5
assert make_chocolate(6, 1, 11) == 6
assert make_chocolate(6, 1, 12) == -1
assert make_chocolate(6, 1, 13) == -1
assert make_chocolate(6, 2, 10) == 0
assert make_chocolate(6, 2, 11) == 1
assert make_chocolate(6, 2, 12) == 2
assert make_chocolate(60, 100, 550) == 50
assert make_chocolate(1000, 1000000, 5000006) == 6
assert make_chocolate(7, 1, 12) == 7
assert make_chocolate(7, 1, 13) == -1
assert make_chocolate(7, 2, 13) == 3