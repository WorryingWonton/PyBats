def first_last6(nums):
    return nums[-1] == 6 or nums[0] == 6

def same_first_last(nums):
    return len(nums) > 0 and nums[0] == nums[-1]

def make_pi():
    return [3, 1, 4]

def common_end(a, b):
    return a[0] == b[0] or b[-1] == a[-1]

def sum3(nums):
    return sum(nums)

def rotate_left3(nums):
    return nums[1:] + nums[:1]

def reverse3(nums):
    return nums[::-1]

def max_end3(nums):
    return [max(nums[0], nums[2])] * 3

def sum2(nums):
    return sum(nums[:2])

def middle_way(a, b):
    return [a[1], b[1]]

def make_ends(nums):
    return [nums[0], nums[-1]]

def has23(nums):
    return 2 in nums or 3 in nums

def no23(nums):
    return not (2 in nums or 3 in nums)

def makeLast(nums):
    return [0] * (2 * len(nums) - 1) + nums[-1:]

def double23(nums):
    return nums == [2, 2] or nums == [3, 3]

def fix23(nums):
    return [2, 0] + nums[2:] if nums[:2] == [2, 3] else nums[:1] + [2, 0] if nums[-2:] == [2, 3] else nums

def start1(a, b):
    return (1 if a[:1] == [1] else 0) + (1 if b[:1] == [1] else 0)

def biggerTwo(a, b):
    return max(a, b, key=sum) if sum(a) != sum(b) else a

def makeMiddle(nums):
    return nums[int(len(nums) / 2) - 1:int(len(nums) / 2) + 1]

def plusTwo(a, b):
    return a + b

def swapEnds(nums):
    return nums[-1:] + nums[1:-1] + nums[:1] if len(nums) > 1 else nums

def midThree(nums):
    return nums[int(len(nums) / 2) - 1:int(len(nums) / 2) + 2]

def maxTriple(nums):
    return max(nums[0], nums[int(len(nums) / 2)], nums[-1])

def frontPiece(nums):
    return nums[:2]

def unlucky1(nums):
    return nums[0:2] == [1, 3] or nums[1:3] == [1, 3] or nums[-2:] == [1, 3] or nums[-3:] == [1, 3]

def make2(a, b):
    return (a[:2] + b)[:2]

def front11(a, b):
    return a[:1] + b[:1]


assert first_last6([1, 2, 6]) == True
assert first_last6([6, 1, 2, 3]) == True
assert first_last6([13, 6, 1, 2, 3]) == False
assert first_last6([13, 6, 1, 2, 6]) == True
assert first_last6([3, 2, 1]) == False
assert first_last6([3, 6, 1]) == False
assert first_last6([3, 6]) == True
assert first_last6([6]) == True
assert first_last6([3]) == False
assert first_last6([5, 6]) == True
assert first_last6([5, 5]) == False
assert first_last6([1, 2, 3, 4, 6]) == True
assert first_last6([1, 2, 3, 4]) == False

assert same_first_last([1, 2, 3]) == False
assert same_first_last([1, 2, 3, 1]) == True
assert same_first_last([1, 2, 1]) == True
assert same_first_last([7]) == True
assert same_first_last([]) == False
assert same_first_last([1, 2, 3, 4, 5, 1]) == True
assert same_first_last([1, 2, 3, 4, 5, 13]) == False
assert same_first_last([13, 2, 3, 4, 5, 13]) == True
assert same_first_last([7, 7]) == True

assert make_pi() == [3, 1, 4]

assert common_end([1, 2, 3], [7, 3]) == True
assert common_end([1, 2, 3], [7, 3, 2]) == False
assert common_end([1, 2, 3], [1, 3]) == True
assert common_end([1, 2, 3], [1]) == True
assert common_end([1, 2, 3], [2]) == False

assert sum3([1, 2, 3]) == 6
assert sum3([5, 11, 2]) == 18
assert sum3([7, 0, 0]) == 7
assert sum3([1, 2, 1]) == 4
assert sum3([1, 1, 1]) == 3
assert sum3([2, 7, 2]) == 11

assert rotate_left3([1, 2, 3]) == [2, 3, 1]
assert rotate_left3([5, 11, 9]) == [11, 9, 5]
assert rotate_left3([7, 0, 0]) == [0, 0, 7]
assert rotate_left3([1, 2, 1]) == [2, 1, 1]
assert rotate_left3([0, 0, 1]) == [0, 1, 0]

assert reverse3([1, 2, 3]) == [3, 2, 1]
assert reverse3([5, 11, 9]) == [9, 11, 5]
assert reverse3([7, 0, 0]) == [0, 0, 7]
assert reverse3([2, 1, 2]) == [2, 1, 2]
assert reverse3([1, 2, 1]) == [1, 2, 1]
assert reverse3([2, 11, 3]) == [3, 11, 2]
assert reverse3([0, 6, 5]) == [5, 6, 0]
assert reverse3([7, 2, 3]) == [3, 2, 7]

assert max_end3([1, 2, 3]) == [3, 3, 3]
assert max_end3([11, 5, 9]) == [11, 11, 11]
assert max_end3([2, 11, 3]) == [3, 3, 3]
assert max_end3([11, 3, 3]) == [11, 11, 11]
assert max_end3([3, 11, 11]) == [11, 11, 11]
assert max_end3([2, 2, 2]) == [2, 2, 2]
assert max_end3([2, 11, 2]) == [2, 2, 2]
assert max_end3([0, 0, 1]) == [1, 1, 1]

assert sum2([1, 2, 3]) == 3
assert sum2([1, 1]) == 2
assert sum2([1, 1, 1, 1]) == 2
assert sum2([1, 2]) == 3
assert sum2([1]) == 1
assert sum2([]) == 0
assert sum2([4, 5, 6]) == 9
assert sum2([4]) == 4

assert middle_way([1, 2, 3], [4, 5, 6]) == [2, 5]
assert middle_way([7, 7, 7], [3, 8, 0]) == [7, 8]
assert middle_way([5, 2, 9], [1, 4, 5]) == [2, 4]
assert middle_way([1, 9, 7], [4, 8, 8]) == [9, 8]
assert middle_way([1, 2, 3], [3, 1, 4]) == [2, 1]
assert middle_way([1, 2, 3], [4, 1, 1]) == [2, 1]

assert make_ends([1, 2, 3]) == [1, 3]
assert make_ends([1, 2, 3, 4]) == [1, 4]
assert make_ends([7, 4, 6, 2]) == [7, 2]
assert make_ends([1, 2, 2, 2, 2, 2, 2, 3]) == [1, 3]
assert make_ends([7, 4]) == [7, 4]
assert make_ends([7]) == [7, 7]
assert make_ends([5, 2, 9]) == [5, 9]
assert make_ends([2, 3, 4, 1]) == [2, 1]

assert has23([2, 5]) == True
assert has23([4, 3]) == True
assert has23([4, 5]) == False
assert has23([2, 2]) == True
assert has23([3, 2]) == True
assert has23([3, 3]) == True
assert has23([7, 7]) == False
assert has23([3, 9]) == True
assert has23([9, 5]) == False

assert no23([4, 5]) == True
assert no23([4, 2]) == False
assert no23([3, 5]) == False
assert no23([1, 9]) == True
assert no23([2, 9]) == False
assert no23([1, 3]) == False
assert no23([1, 1]) == True
assert no23([2, 2]) == False
assert no23([3, 3]) == False
assert no23([7, 8]) == True
assert no23([8, 7]) == True

assert makeLast([4, 5, 6]) == [0, 0, 0, 0, 0, 6]
assert makeLast([1, 2]) == [0, 0, 0, 2]
assert makeLast([3]) == [0, 3]
assert makeLast([0]) == [0, 0]
assert makeLast([7, 7, 7]) == [0, 0, 0, 0, 0, 7]
assert makeLast([3, 1, 4]) == [0, 0, 0, 0, 0, 4]
assert makeLast([1, 2, 3, 4]) == [0, 0, 0, 0, 0, 0, 0, 4]
assert makeLast([1, 2, 3, 0]) == [0, 0, 0, 0, 0, 0, 0, 0]
assert makeLast([2, 4]) == [0, 0, 0, 4]

assert double23([2, 2]) == True
assert double23([3, 3]) == True
assert double23([2, 3]) == False
assert double23([3, 2]) == False
assert double23([4, 5]) == False
assert double23([2]) == False
assert double23([3]) == False
assert double23([]) == False
assert double23([3, 4]) == False

assert fix23([1, 2, 3]) == [1, 2, 0]
assert fix23([2, 3, 5]) == [2, 0, 5]
assert fix23([1, 2, 1]) == [1, 2, 1]
assert fix23([3, 2, 1]) == [3, 2, 1]
assert fix23([3, 2, 3]) == [3, 2, 0]
assert fix23([3, 2, 2]) == [3, 2, 2]
assert fix23([2, 2, 3]) == [2, 2, 0]
assert fix23([2, 3, 3]) == [2, 0, 3]

assert start1([1, 2, 3], [1, 3]) == 2
assert start1([7, 2, 3], [1]) == 1
assert start1([1, 2], []) == 1
assert start1([], [1, 2]) == 1
assert start1([7], []) == 0
assert start1([7], [1]) == 1
assert start1([1], [1]) == 2
assert start1([7], [8]) == 0
assert start1([], []) == 0
assert start1([1, 3], [1]) == 2

assert biggerTwo([1, 2], [3, 4]) == [3, 4]
assert biggerTwo([3, 4], [1, 2]) == [3, 4]
assert biggerTwo([1, 1], [1, 2]) == [1, 2]
assert biggerTwo([2, 1], [1, 1]) == [2, 1]
assert biggerTwo([2, 2], [1, 3]) == [2, 2]
assert biggerTwo([1, 3], [2, 2]) == [1, 3]
assert biggerTwo([6, 7], [3, 1]) == [6, 7]

assert makeMiddle([1, 2, 3, 4]) == [2, 3]
assert makeMiddle([7, 1, 2, 3, 4, 9]) == [2, 3]
assert makeMiddle([1, 2]) == [1, 2]
assert makeMiddle([5, 2, 4, 7]) == [2, 4]
assert makeMiddle([9, 0, 4, 3, 9, 1]) == [4, 3]

assert plusTwo([1, 2], [3, 4]) == [1, 2, 3, 4]
assert plusTwo([4, 4], [2, 2]) == [4, 4, 2, 2]
assert plusTwo([9, 2], [3, 4]) == [9, 2, 3, 4]

assert swapEnds([1, 2, 3, 4]) == [4, 2, 3, 1]
assert swapEnds([1, 2, 3]) == [3, 2, 1]
assert swapEnds([8, 6, 7, 9, 5]) == [5, 6, 7, 9, 8]
assert swapEnds([3, 1, 4, 1, 5, 9]) == [9, 1, 4, 1, 5, 3]
assert swapEnds([1, 2]) == [2, 1]
assert swapEnds([1]) == [1]

assert midThree([1, 2, 3, 4, 5]) == [2, 3, 4]
assert midThree([8, 6, 7, 5, 3, 0, 9]) == [7, 5, 3]
assert midThree([1, 2, 3]) == [1, 2, 3]

assert maxTriple([1, 2, 3]) == 3
assert maxTriple([1, 5, 3]) == 5
assert maxTriple([5, 2, 3]) == 5
assert maxTriple([1, 2, 3, 1, 1]) == 3
assert maxTriple([1, 7, 3, 1, 5]) == 5
assert maxTriple([5, 1, 3, 7, 1]) == 5
assert maxTriple([5, 1, 7, 3, 7, 8, 1]) == 5
assert maxTriple([5, 1, 7, 9, 7, 8, 1]) == 9
assert maxTriple([5, 1, 7, 3, 7, 8, 9]) == 9
assert maxTriple([2, 2, 5, 1, 1]) == 5

assert frontPiece([1, 2, 3]) == [1, 2]
assert frontPiece([1, 2]) == [1, 2]
assert frontPiece([1]) == [1]
assert frontPiece([]) == []
assert frontPiece([6, 5, 0]) == [6, 5]
assert frontPiece([6, 5]) == [6, 5]
assert frontPiece([3, 1, 4, 1, 5]) == [3, 1]
assert frontPiece([6]) == [6]

assert unlucky1([1, 3, 4, 5]) == True
assert unlucky1([2, 1, 3, 4, 5]) == True
assert unlucky1([1, 1, 1]) == False
assert unlucky1([1, 3, 1]) == True
assert unlucky1([1, 1, 3]) == True
assert unlucky1([1, 2, 3]) == False
assert unlucky1([3, 3, 3]) == False
assert unlucky1([1, 3]) == True
assert unlucky1([1, 4]) == False
assert unlucky1([1]) == False
assert unlucky1([]) == False
assert unlucky1([1, 1, 1, 3, 1]) == False
assert unlucky1([1, 1, 3, 1, 1]) == True
assert unlucky1([1, 1, 1, 1, 3]) == True
assert unlucky1([1, 4, 1, 5]) == False
assert unlucky1([1, 1, 2, 3]) == False
assert unlucky1([2, 3, 2, 1]) == False
assert unlucky1([2, 3, 1, 3]) == True
assert unlucky1([1, 2, 3, 4, 1, 3]) == True

assert make2([4, 5], [1, 2, 3]) == [4, 5]
assert make2([4], [1, 2, 3]) == [4, 1]
assert make2([], [1, 2]) == [1, 2]
assert make2([1, 2], []) == [1, 2]
assert make2([3], [1, 2, 3]) == [3, 1]
assert make2([3], [1]) == [3, 1]
assert make2([3, 1, 4], []) == [3, 1]
assert make2([1], [1]) == [1, 1]
assert make2([1, 2, 3], [7, 8]) == [1, 2]
assert make2([7, 8], [1, 2, 3]) == [7, 8]
assert make2([7], [1, 2, 3]) == [7, 1]
assert make2([5, 4], [2, 3, 7]) == [5, 4]

assert front11([1, 2, 3], [7, 9, 8]) == [1, 7]
assert front11([1], [2]) == [1, 2]
assert front11([1, 7], []) == [1]
assert front11([], [2, 8]) == [2]
assert front11([], []) == []
assert front11([3], [1, 4, 1, 9]) == [3, 1]
assert front11([1, 4, 1, 9], []) == [1]