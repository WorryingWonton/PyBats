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
    a = abs(a)
    b = abs(b)
    c = abs(c)
    return (abs(a - b) <= 1 and (abs(a - c) >= 2 and abs(b - c) >= 2)) or ((abs(a - b) >= 2 and abs(b - c) >= 2) and abs(a - c) <= 1)

def make_chocolate(small, big, goal):
    return (goal - 5 * big if 5 * big <= goal else goal % 5) if (goal % 5 <= small and goal - 5 * big <= small) else -1