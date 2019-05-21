def scoresIncreasing(scores):
    for idx in range(len(scores) - 1):
        if scores[idx] > scores[idx + 1]:
            return False
    return True

def scores100(scores):
    for idx in range(len(scores)):
        if scores[idx:idx + 2] == [100, 100]:
            return True
    return False

def scoresClump(scores):
    for idx, score in enumerate(scores[:-2]):
        s_range = range(score - 2, score + 3)
        if scores[idx + 1] in s_range and scores[idx + 2] in s_range:
            return True
    return False

def scoresAverage(scores):
    l_half = scores[:int(len(scores)/2)]
    r_half = scores[int(len(scores)/2):]
    return max(sum(l_half)/len(l_half), sum(r_half)/len(r_half))

def wordsCount(words, n):
    return len([word for word in words if len(word) == n])

def wordsFront(words, n):
    return words[:n]

def wordsWithoutList(words, length):
    return [word for word in words if len(word) != length]

def hasOne(n):
    return 1 in [int(x) for x in str(n)]

def dividesSelf(n):
    n_digits = [int(x) for x in str(n)]
    return len(n_digits) == len([x for x in n_digits if x and not n % x])

def copyEvens(nums, count):
    return [num for num in nums if not num % 2][:count]

def copyEndy(nums, count):
    return [num for num in nums if (num in range(0, 11) or num in range(90, 101))][:count]

def matchUp(a, b):
    return len([x for idx, x in enumerate(a) if (x and b[idx]) and x[0] == b[idx][0]])

def scoreUp(key, answers):
    score_model = lambda x, y: 4 if x == y else (0 if x == '?' else -1)
    return sum([score_model(x, key[idx]) for idx, x in enumerate(answers)])

def wordsWithout(words, target):
    return [x for x in words if x != target]

def scoresSpecial(a, b):
    a = [x for x in a if not x % 10]
    b = [x for x in b if not x % 10]
    return (max(a) if a else 0) + (max(b) if b else 0)

def sumHeights(heights, start, end):
    delta_h = 0
    for idx in range(start, end):
        delta_h += abs(heights[idx] - heights[idx + 1])
    return delta_h

def sumHeights2(heights, start, end):
    delta_h = 0
    for idx in range(start, end):
        if heights[idx + 1] > heights[idx]:
            delta_h += 2 * (heights[idx + 1] - heights[idx])
        else:
            delta_h += heights[idx] - heights[idx + 1]
    return delta_h

def bigHeights(heights, start, end):
    big_steps = 0
    for idx in range(start, end):
        if abs(heights[idx] - heights[idx + 1]) >= 5:
            big_steps += 1
    return big_steps

def userCompare(aName, aId, bName, bId):
    if aName != bName:
        return -1 if aName < bName else 1
    elif aId != bId:
        return -1 if aId < bId else 1
    return 0

def mergeTwo(a, b, n):
    return sorted(set(a) | set(b))[:n]

def commonTwo(a, b):
    return len(set(a) | set(b)) - len(set(a) ^ set(b))


assert scoresIncreasing([1, 3, 4]) == True
assert scoresIncreasing([1, 3, 2]) == False
assert scoresIncreasing([1, 1, 4]) == True
assert scoresIncreasing([1, 1, 2, 4, 4, 7]) == True
assert scoresIncreasing([1, 1, 2, 4, 3, 7]) == False
assert scoresIncreasing([-5, 4, 11]) == True

assert scores100([1, 100, 100]) == True
assert scores100([1, 100, 99, 100]) == False
assert scores100([100, 1, 100, 100]) == True
assert scores100([100, 1, 100, 1]) == False
assert scores100([1, 2, 3, 4, 5]) == False
assert scores100([1, 2, 100, 4, 5]) == False

assert scoresClump([3, 4, 5]) == True
assert scoresClump([3, 4, 6]) == False
assert scoresClump([1, 3, 5, 5]) == True
assert scoresClump([2, 4, 5, 6]) == True
assert scoresClump([2, 4, 5, 7]) == False
assert scoresClump([2, 4, 4, 7]) == True
assert scoresClump([3, 3, 6, 7, 9]) == False
assert scoresClump([3, 3, 7, 7, 9]) == True
assert scoresClump([4, 5, 8]) == False

assert scoresAverage([2, 2, 4, 4]) == 4
assert scoresAverage([4, 4, 4, 2, 2, 2]) == 4
assert scoresAverage([3, 4, 5, 1, 2, 3]) == 4
assert scoresAverage([5, 6]) == 6
assert scoresAverage([5, 4]) == 5
assert scoresAverage([5, 4, 5, 6, 2, 1, 2, 3]) == 5

assert wordsCount(["a", "bb", "b", "ccc"], 1) == 2
assert wordsCount(["a", "bb", "b", "ccc"], 3) == 1
assert wordsCount(["a", "bb", "b", "ccc"], 4) == 0
assert wordsCount(["xx", "yyy", "x", "yy", "z"], 1) == 2
assert wordsCount(["xx", "yyy", "x", "yy", "z"], 2) == 2
assert wordsCount(["xx", "yyy", "x", "yy", "z"], 3) == 1

assert wordsFront(["a", "b", "c", "d"], 1) == ["a"]
assert wordsFront(["a", "b", "c", "d"], 2) == ["a", "b"]
assert wordsFront(["a", "b", "c", "d"], 3) == ["a", "b", "c"]
assert wordsFront(["a", "b", "c", "d"], 4) == ["a", "b", "c", "d"]
assert wordsFront(["Hi", "There"], 1) == ["Hi"]
assert wordsFront(["Hi", "There"], 2) == ["Hi", "There"]

assert wordsWithoutList(["a", "bb", "b", "ccc"], 1) == ["bb", "ccc"]
assert wordsWithoutList(["a", "bb", "b", "ccc"], 3) == ["a", "bb", "b"]
assert wordsWithoutList(["a", "bb", "b", "ccc"], 4) == ["a", "bb", "b", "ccc"]
assert wordsWithoutList(["xx", "yyy", "x", "yy", "z"], 1) == ["xx", "yyy", "yy"]
assert wordsWithoutList(["xx", "yyy", "x", "yy", "z"], 2) == ["yyy", "x", "z"]

assert hasOne(10) == True
assert hasOne(22) == False
assert hasOne(220) == False
assert hasOne(212) == True
assert hasOne(1) == True
assert hasOne(9) == False
assert hasOne(211112) == True
assert hasOne(121121) == True
assert hasOne(222222) == False
assert hasOne(56156) == True
assert hasOne(56556) == False

assert dividesSelf(128) == True
assert dividesSelf(12) == True
assert dividesSelf(120) == False
assert dividesSelf(122) == True
assert dividesSelf(13) == False
assert dividesSelf(32) == False
assert dividesSelf(22) == True
assert dividesSelf(42) == False
assert dividesSelf(212) == True
assert dividesSelf(213) == False
assert dividesSelf(162) == True

assert copyEvens([3, 2, 4, 5, 8], 2) == [2, 4]
assert copyEvens([3, 2, 4, 5, 8], 3) == [2, 4, 8]
assert copyEvens([6, 1, 2, 4, 5, 8], 3) == [6, 2, 4]
assert copyEvens([6, 1, 2, 4, 5, 8], 4) == [6, 2, 4, 8]
assert copyEvens([3, 1, 4, 1, 5], 1) == [4]
assert copyEvens([2], 1) == [2]
assert copyEvens([6, 2, 4, 8], 2) == [6, 2]
assert copyEvens([6, 2, 4, 8], 3) == [6, 2, 4]
assert copyEvens([6, 2, 4, 8], 4) == [6, 2, 4, 8]
assert copyEvens([1, 8, 4], 1) == [8]
assert copyEvens([1, 8, 4], 2) == [8, 4]
assert copyEvens([2, 8, 4], 2) == [2, 8]

assert copyEndy([9, 11, 90, 22, 6], 2) == [9, 90]
assert copyEndy([9, 11, 90, 22, 6], 3) == [9, 90, 6]
assert copyEndy([12, 1, 1, 13, 0, 20], 2) == [1, 1]
assert copyEndy([12, 1, 1, 13, 0, 20], 3) == [1, 1, 0]
assert copyEndy([0], 1) == [0]
assert copyEndy([10, 11, 90], 2) == [10, 90]
assert copyEndy([90, 22, 100], 2) == [90, 100]
assert copyEndy([12, 11, 10, 89, 101, 4], 1) == [10]
assert copyEndy([13, 2, 2, 0], 2) == [2, 2]
assert copyEndy([13, 2, 2, 0], 3) == [2, 2, 0]
assert copyEndy([13, 2, 13, 2, 0, 30], 2) == [2, 2]
assert copyEndy([13, 2, 13, 2, 0, 30], 3) == [2, 2, 0]

assert matchUp(["aa", "bb", "cc"], ["aaa", "xx", "bb"]) == 1
assert matchUp(["aa", "bb", "cc"], ["aaa", "b", "bb"]) == 2
assert matchUp(["aa", "bb", "cc"], ["", "", "ccc"]) == 1
assert matchUp(["", "", "ccc"], ["aa", "bb", "cc"]) == 1
assert matchUp(["", "", ""], ["", "bb", "cc"]) == 0
assert matchUp(["aa", "bb", "cc"], ["", "", ""]) == 0
assert matchUp(["aa", "", "ccc"], ["", "bb", "cc"]) == 1
assert matchUp(["x", "y", "z"], ["y", "z", "x"]) == 0
assert matchUp(["", "y", "z"], ["", "y", "x"]) == 1
assert matchUp(["x", "y", "z"], ["xx", "yyy", "zzz"]) == 3
assert matchUp(["x", "y", "z"], ["xx", "yyy", ""]) == 2
assert matchUp(["b", "x", "y", "z"], ["a", "xx", "yyy", "zzz"]) == 3
assert matchUp(["aaa", "bb", "c"], ["aaa", "xx", "bb"]) == 1

assert scoreUp(["a", "a", "b", "b"], ["a", "c", "b", "c"]) == 6
assert scoreUp(["a", "a", "b", "b"], ["a", "a", "b", "c"]) == 11
assert scoreUp(["a", "a", "b", "b"], ["a", "a", "b", "b"]) == 16
assert scoreUp(["a", "a", "b", "b"], ["?", "c", "b", "?"]) == 3
assert scoreUp(["a", "a", "b", "b"], ["?", "c", "?", "?"]) == -1
assert scoreUp(["a", "a", "b", "b"], ["c", "?", "b", "b"]) == 7
assert scoreUp(["a", "a", "b", "b"], ["c", "?", "b", "?"]) == 3
assert scoreUp(["a", "b", "c"], ["a", "c", "b"]) == 2
assert scoreUp(["a", "a", "b", "b", "c", "c"], ["a", "c", "a", "c", "a", "c"]) == 4
assert scoreUp(["a", "a", "b", "b", "c", "c"], ["a", "c", "?", "?", "a", "c"]) == 6
assert scoreUp(["a", "a", "b", "b", "c", "c"], ["a", "c", "?", "?", "c", "c"]) == 11
assert scoreUp(["a", "b", "c"], ["a", "b", "c"]) == 12

assert wordsWithout(["a", "b", "c", "a"], "a") == ["b", "c"]
assert wordsWithout(["a", "b", "c", "a"], "b") == ["a", "c", "a"]
assert wordsWithout(["a", "b", "c", "a"], "c") == ["a", "b", "a"]
assert wordsWithout(["b", "c", "a", "a"], "b") == ["c", "a", "a"]
assert wordsWithout(["xx", "yyy", "x", "yy", "x"], "x") == ["xx", "yyy", "yy"]
assert wordsWithout(["xx", "yyy", "x", "yy", "x"], "yy") == ["xx", "yyy", "x", "x"]
assert wordsWithout(["aa", "ab", "ac", "aa"], "aa") == ["ab", "ac"]

assert scoresSpecial([12, 10, 4], [2, 20, 30]) == 40
assert scoresSpecial([20, 10, 4], [2, 20, 10]) == 40
assert scoresSpecial([12, 11, 4], [2, 20, 31]) == 20
assert scoresSpecial([1, 20, 2, 50], [3, 4, 5]) == 50
assert scoresSpecial([3, 4, 5], [1, 50, 2, 20]) == 50
assert scoresSpecial([10, 4, 20, 30], [20]) == 50
assert scoresSpecial([10, 4, 20, 30], [20]) == 50
assert scoresSpecial([10, 4, 20, 30], [3, 20, 99]) == 50
assert scoresSpecial([10, 4, 20, 30], [30, 20, 99]) == 60
assert scoresSpecial([], [2]) == 0
assert scoresSpecial([], [20]) == 20
assert scoresSpecial([14, 10, 4], [4, 20, 30]) == 40

assert sumHeights([5, 3, 6, 7, 2], 2, 4) == 6
assert sumHeights([5, 3, 6, 7, 2], 0, 1) == 2
assert sumHeights([5, 3, 6, 7, 2], 0, 4) == 11
assert sumHeights([5, 3, 6, 7, 2], 1, 1) == 0
assert sumHeights([1, 2, 3, 4, 5, 4, 3, 2, 10], 0, 3) == 3
assert sumHeights([1, 2, 3, 4, 5, 4, 3, 2, 10], 4, 8) == 11
assert sumHeights([1, 2, 3, 4, 5, 4, 3, 2, 10], 7, 8) == 8
assert sumHeights([1, 2, 3, 4, 5, 4, 3, 2, 10], 8, 8) == 0
assert sumHeights([1, 2, 3, 4, 5, 4, 3, 2, 10], 2, 2) == 0
assert sumHeights([1, 2, 3, 4, 5, 4, 3, 2, 10], 3, 6) == 3
assert sumHeights([10, 8, 7, 7, 7, 6, 7], 1, 4) == 1
assert sumHeights([10, 8, 7, 7, 7, 6, 7], 1, 5) == 2

assert sumHeights2([5, 3, 6, 7, 2], 2, 4) == 7
assert sumHeights2([5, 3, 6, 7, 2], 0, 1) == 2
assert sumHeights2([5, 3, 6, 7, 2], 0, 4) == 15
assert sumHeights2([5, 3, 6, 7, 2], 1, 1) == 0
assert sumHeights2([1, 2, 3, 4, 5, 4, 3, 2, 10], 0, 3) == 6
assert sumHeights2([1, 2, 3, 4, 5, 4, 3, 2, 10], 4, 8) == 19
assert sumHeights2([1, 2, 3, 4, 5, 4, 3, 2, 10], 7, 8) == 16
assert sumHeights2([1, 2, 3, 4, 5, 4, 3, 2, 10], 8, 8) == 0
assert sumHeights2([1, 2, 3, 4, 5, 4, 3, 2, 10], 2, 2) == 0
assert sumHeights2([1, 2, 3, 4, 5, 4, 3, 2, 10], 3, 6) == 4
assert sumHeights2([10, 8, 7, 7, 7, 6, 7], 1, 4) == 1
assert sumHeights2([10, 8, 7, 7, 7, 6, 7], 1, 5) == 2

assert bigHeights([5, 3, 6, 7, 2], 2, 4) == 1
assert bigHeights([5, 3, 6, 7, 2], 0, 1) == 0
assert bigHeights([5, 3, 6, 7, 2], 0, 4) == 1
assert bigHeights([5, 3, 6, 7, 3], 0, 4) == 0
assert bigHeights([5, 3, 6, 7, 2], 1, 1) == 0
assert bigHeights([5, 13, 6, 7, 2], 1, 2) == 1
assert bigHeights([5, 13, 6, 7, 2], 1, 2) == 1
assert bigHeights([5, 13, 6, 7, 2], 0, 2) == 2
assert bigHeights([5, 13, 6, 7, 2], 1, 4) == 2
assert bigHeights([5, 13, 6, 7, 2], 0, 4) == 3
assert bigHeights([5, 13, 6, 7, 2], 0, 3) == 2
assert bigHeights([1, 2, 3, 4, 5, 4, 3, 2, 10], 0, 3) == 0
assert bigHeights([1, 2, 3, 4, 5, 4, 3, 2, 10], 4, 8) == 1
assert bigHeights([1, 2, 3, 14, 5, 4, 3, 2, 10], 0, 3) == 1
assert bigHeights([1, 2, 3, 14, 5, 4, 3, 2, 10], 7, 8) == 1
assert bigHeights([1, 2, 3, 14, 5, 4, 3, 2, 10], 3, 8) == 2
assert bigHeights([1, 2, 3, 14, 5, 4, 3, 2, 10], 2, 8) == 3

assert userCompare("bb", 1, "zz", 2) == -1
assert userCompare("bb", 1, "aa", 2) == 1
assert userCompare("bb", 1, "bb", 1) == 0
assert userCompare("bb", 5, "bb", 1) == 1
assert userCompare("bb", 5, "bb", 10) == -1
assert userCompare("adam", 1, "bob", 2) == -1
assert userCompare("bob", 1, "bob", 2) == -1
assert userCompare("bzb", 1, "bob", 2) == 1

assert mergeTwo(["a", "c", "z"], ["b", "f", "z"], 3) == ["a", "b", "c"]
assert mergeTwo(["a", "c", "z"], ["c", "f", "z"], 3) == ["a", "c", "f"]
assert mergeTwo(["f", "g", "z"], ["c", "f", "g"], 3) == ["c", "f", "g"]
assert mergeTwo(["a", "c", "z"], ["a", "c", "z"], 3) == ["a", "c", "z"]
assert mergeTwo(["a", "b", "c", "z"], ["a", "c", "z"], 3) == ["a", "b", "c"]
assert mergeTwo(["a", "c", "z"], ["a", "b", "c", "z"], 3) == ["a", "b", "c"]
assert mergeTwo(["a", "c", "z"], ["a", "c", "z"], 2) == ["a", "c"]
assert mergeTwo(["a", "c", "z"], ["a", "c", "y", "z"], 3) == ["a", "c", "y"]
assert mergeTwo(["x", "y", "z"], ["a", "b", "z"], 3) == ["a", "b", "x"]

assert commonTwo(["a", "c", "x"], ["b", "c", "d", "x"]) == 2
assert commonTwo(["a", "c", "x"], ["a", "b", "c", "x", "z"]) == 3
assert commonTwo(["a", "b", "c"], ["a", "b", "c"]) == 3
assert commonTwo(["a", "a", "b", "b", "c"], ["a", "b", "c"]) == 3
assert commonTwo(["a", "a", "b", "b", "c"], ["a", "b", "b", "b", "c"]) == 3
assert commonTwo(["a", "a", "b", "b", "c"], ["a", "b", "b", "c", "c"]) == 3
assert commonTwo(["b", "b", "b", "b", "c"], ["a", "b", "b", "b", "c"]) == 2
assert commonTwo(["a", "b", "c", "c", "d"], ["a", "b", "b", "c", "d", "d"]) == 4
assert commonTwo(["a", "a", "b", "b", "c"], ["b", "b", "b"]) == 1
assert commonTwo(["a", "a", "b", "b", "c"], ["c", "c"]) == 1
assert commonTwo(["a", "a", "b", "b", "c"], ["b", "b", "b", "x"]) == 1
assert commonTwo(["a", "a", "b", "b", "c"], ["b", "b"]) == 1
assert commonTwo(["a"], ["a", "b"]) == 1
assert commonTwo(["a"], ["b"]) == 0
assert commonTwo(["a", "a"], ["b", "b"]) == 0
assert commonTwo(["a", "b"], ["a", "b"]) == 2