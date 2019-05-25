def noNeg(nums):
    return list(filter(lambda x: x > -1, nums))

def no9(nums):
    return list(filter(lambda x: x % 10 != 9, nums))

def noTeen(nums):
    return list(filter(lambda x: x not in range(13, 20), nums))

def noZ(strings):
    return list(filter(lambda x: 'z' not in x, strings))

def noLong(strings):
    return list(filter(lambda x: len(x) < 4, strings))

def no34(strings):
    return list(filter(lambda x: len(x) not in [3, 4], strings))

def noYY(strings):
    return list(filter(lambda x: 'yy' not in x, [x + 'y' for x in strings]))

def two2(nums):
    return list(filter(lambda x: x % 10 != 2, [2 * x for x in nums]))

def square56(nums):
    return list(filter(lambda x: x % 10 not in [5, 6], [x ** 2 + 10 for x in nums]))


assert noNeg([1, -2]) == [1]
assert noNeg([-3, -3, 3, 3]) == [3, 3]
assert noNeg([-1, -1, -1]) == []
assert noNeg([]) == []
assert noNeg([0, 1, 2]) == [0, 1, 2]
assert noNeg([3, -10, 1, -1, 4, -400]) == [3, 1, 4]
assert noNeg([-1, 3, 1, -1, -10, -100, -111, 5]) == [3, 1, 5]

assert no9([1, 2, 19]) == [1, 2]
assert no9([9, 19, 29, 3]) == [3]
assert no9([1, 2, 3]) == [1, 2, 3]
assert no9([45, 99, 90, 28, 13, 999, 0]) == [45, 90, 28, 13, 0]
assert no9([45, 99, 90, 28, 13, 999, 0]) == [45, 90, 28, 13, 0]
assert no9([9]) == []
assert no9([0, 9, 0]) == [0, 0]

assert noTeen([12, 13, 19, 20]) == [12, 20]
assert noTeen([1, 14, 1]) == [1, 1]
assert noTeen([15]) == []
assert noTeen([-15]) == [-15]
assert noTeen([]) == []
assert noTeen([0, 1, 2, -3]) == [0, 1, 2, -3]
assert noTeen([15, 17, 19, 21, 19]) == [21]
assert noTeen([-16, 2, 15, 3, 16, 25]) == [-16, 2, 3, 25]

assert noZ(["aaa", "bbb", "aza"]) == ["aaa", "bbb"]
assert noZ(["hziz", "hzello", "hi"]) == ["hi"]
assert noZ(["hello", "howz", "are", "youz"]) == ["hello", "are"]
assert noZ([]) == []
assert noZ([""]) == [""]
assert noZ(["x", "y", "z"]) == ["x", "y"]

assert noLong(["this", "not", "too", "long"]) == ["not", "too"]
assert noLong(["a", "bbb", "cccc"]) == ["a", "bbb"]
assert noLong(["cccc", "cccc", "cccc"]) == []
assert noLong([]) == []
assert noLong([""]) == [""]
assert noLong(["empty", "", "empty"]) == [""]
assert noLong(["a"]) == ["a"]
assert noLong(["aaaa", "bbb", "***", "333"]) == ["bbb", "***", "333"]

assert no34(["a", "bb", "ccc"]) == ["a", "bb"]
assert no34(["a", "bb", "ccc", "dddd"]) == ["a", "bb"]
assert no34(["ccc", "dddd", "apple"]) == ["apple"]
assert no34(["this", "not", "too", "long"]) == []
assert no34(["a", "bbb", "cccc", "xx"]) == ["a", "xx"]
assert no34(["dddd", "ddd", "xxxxxxx"]) == ["xxxxxxx"]
assert no34([]) == []
assert no34([""]) == [""]
assert no34(["empty", "", "empty"]) == ["empty", "", "empty"]
assert no34(["a"]) == ["a"]
assert no34(["aaaa", "bbb", "*****", "333"]) == ["*****"]

assert noYY(["a", "b", "c"]) == ["ay", "by", "cy"]
assert noYY(["a", "b", "cy"]) == ["ay", "by"]
assert noYY(["xx", "ya", "zz"]) == ["xxy", "yay", "zzy"]
assert noYY(["xx", "yay", "zz"]) == ["xxy", "zzy"]
assert noYY(["yyx", "y", "zzz"]) == ["zzzy"]
assert noYY(["hello", "there"]) == ["helloy", "therey"]
assert noYY(["ya"]) == ["yay"]
assert noYY([]) == []
assert noYY([""]) == ["y"]
assert noYY(["xx", "yy", "zz"]) == ["xxy", "zzy"]

assert two2([1, 2, 3]) == [4, 6]
assert two2([2, 6, 11]) == [4]
assert two2([0]) == [0]
assert two2([]) == []
assert two2([1, 11, 111, 16]) == []
assert two2([2, 3, 5, 7, 11]) == [4, 6, 10, 14]
assert two2([3, 1, 4, 1, 6, 99, 0]) == [6, 8, 198, 0]

assert square56([3, 1, 4]) == [19, 11]
assert square56([1]) == [11]
assert square56([2]) == [14]
assert square56([3]) == [19]
assert square56([4]) == []
assert square56([5]) == []
assert square56([6]) == []
assert square56([7]) == [59]
assert square56([1, 2, 3, 4, 5, 6, 7]) == [11, 14, 19, 59]
assert square56([3, -1, -4, 1, 5, 9]) == [19, 11, 11, 91]