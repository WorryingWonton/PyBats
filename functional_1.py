def doubling(nums):
    return [2 * x for x in nums]

def square(nums):
    return [x * x for x in nums]

def addStar(strings):
    return [x + '*' for x in strings]

def copies3(strings):
    return [3 * x for x in strings]

def moreY(strings):
    return ['y' + x + 'y' for x in strings]

def math1(nums):
    return [(x + 1)*10 for x in nums]

def rightDigit(nums):
    return [int(str(x)[-1]) for x in nums]

def lower(strings):
    return [x.lower() for x in strings]

def noX(strings):
    return [''.join(x.split('x')) for x in strings]


assert doubling([1, 2, 3]) == [2, 4, 6]
assert doubling([6, 8, 6, 8, -1]) == [12, 16, 12, 16, -2]
assert doubling([]) == []
assert doubling([5]) == [10]
assert doubling([5, 10]) == [10, 20]
assert doubling([8, -5, 7, 3, 109]) == [16, -10, 14, 6, 218]
assert doubling([6, -3, 12, 23, 4, 1, 19, 11, 2, 3, 2]) == [12, -6, 24, 46, 8, 2, 38, 22, 4, 6, 4]
assert doubling([3, 1, 4, 1, 5, 9]) == [6, 2, 8, 2, 10, 18]

assert square([1, 2, 3]) == [1, 4, 9]
assert square([6, 8, -6, -8, 1]) == [36, 64, 36, 64, 1]
assert square([]) == []
assert square([12]) == [144]
assert square([5, 10]) == [25, 100]
assert square([6, -3, 12, 23, 4, 1, 19, 11, 2, 3, 2]) == [36, 9, 144, 529, 16, 1, 361, 121, 4, 9, 4]

assert addStar(["a", "bb", "ccc"]) == ["a*", "bb*", "ccc*"]
assert addStar(["hello", "there"]) == ["hello*", "there*"]
assert addStar(["*"]) == ["**"]
assert addStar([]) == []
assert addStar(["kittens", "and", "chocolate", "and"]) == ["kittens*", "and*", "chocolate*", "and*"]
assert addStar(["empty", "string", ""]) == ["empty*", "string*", "*"]

assert copies3(["a", "bb", "ccc"]) == ["aaa", "bbbbbb", "ccccccccc"]
assert copies3(["24", "a", ""]) == ["242424", "aaa", ""]
assert copies3(["hello", "there"]) == ["hellohellohello", "theretherethere"]
assert copies3(["no"]) == ["nonono"]
assert copies3([]) == []
assert copies3(["this", "and", "that", "and"]) == ["thisthisthis", "andandand", "thatthatthat", "andandand"]

assert moreY(["a", "b", "c"]) == ["yay", "yby", "ycy"]
assert moreY(["hello", "there"]) == ["yhelloy", "ytherey"]
assert moreY(["yay"]) == ["yyayy"]
assert moreY(["", "a", "xx"]) == ["yy", "yay", "yxxy"]
assert moreY([]) == []
assert moreY(["xx", "yy", "zz"]) == ["yxxy", "yyyy", "yzzy"]

assert math1([1, 2, 3]) == [20, 30, 40]
assert math1([6, 8, 6, 8, 1]) == [70, 90, 70, 90, 20]
assert math1([10]) == [110]
assert math1([]) == []
assert math1([5, 10]) == [60, 110]
assert math1([-1, -2, -3, -2, -1]) == [0, -10, -20, -10, 0]
assert math1([6, -3, 12, 23, 4, 1, 19, 11, 2, 3, 2]) == [70, -20, 130, 240, 50, 20, 200, 120, 30, 40, 30]

assert rightDigit([1, 22, 93]) == [1, 2, 3]
assert rightDigit([16, 8, 886, 8, 1]) == [6, 8, 6, 8, 1]
assert rightDigit([10, 0]) == [0, 0]
assert rightDigit([]) == []
assert rightDigit([5, 10]) == [5, 0]
assert rightDigit([5, 50, 500, 5000, 5000]) == [5, 0, 0, 0, 0]
assert rightDigit([6, 23, 12, 23, 4, 1, 19, 1119, 2, 3, 2]) == [6, 3, 2, 3, 4, 1, 9, 9, 2, 3, 2]

assert lower(["Hello", "Hi"]) == ["hello", "hi"]
assert lower(["AAA", "BBB", "ccc"]) == ["aaa", "bbb", "ccc"]
assert lower(["KitteN", "ChocolaTE"]) == ["kitten", "chocolate"]
assert lower([]) == []
assert lower(["EMPTY", ""]) == ["empty", ""]
assert lower(["aaX", "bYb", "Ycc", "ZZZ"]) == ["aax", "byb", "ycc", "zzz"]

assert noX(["ax", "bb", "cx"]) == ["a", "bb", "c"]
assert noX(["xxax", "xbxbx", "xxcx"]) == ["a", "bb", "c"]
assert noX(["x"]) == [""]
assert noX([""]) == [""]
assert noX([]) == []
assert noX(["the", "taxi"]) == ["the", "tai"]
assert noX(["the", "xxtxaxixxx"]) == ["the", "tai"]
assert noX(["this", "is", "the", "x"]) == ["this", "is", "the", ""]