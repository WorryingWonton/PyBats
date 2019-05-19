def count_evens(nums):
    return len([x for x in nums if not x % 2])

def big_diff(nums):
    return max(nums) - min(nums)

def centered_average(nums):
    return int((sum(nums) - max(nums) - min(nums)) / (len(nums) - 2))

def sum13(nums):
    return sum([x for idx, x in enumerate(nums) if x != 13 and (idx == 0 or nums[idx - 1] != 13)])

def sum67(nums):
    index = 0
    while index < len(nums):
        if nums[index] == 6:
            while nums[index] != 7:
                nums[index] = 0
                index += 1
            nums[index] = 0
        index += 1
    return sum(nums)

def has22(nums):
    for idx in range(len(nums)):
        if nums[idx:idx + 2] == [2, 2]:
            return True
    return False

def lucky13(nums):
    return 1 not in nums and 3 not in nums

def sum28(nums):
    return sum([x for x in nums if x == 2]) == 8

def more14(nums):
    return len([x for x in nums if x == 1]) > len([x for x in nums if x == 4])

def fizzArray(n):
    return list(range(n))

def only14(nums):
    for num in nums:
        if num not in [1, 4]:
            return False
    return True

def fizzArray2(n):
    return [str(x) for x in range(n)]

def no14(nums):
    return ((4 in nums) ^ (1 in nums)) or len(nums) == len([x for x in nums if x not in [1, 4]])

def isEverywhere(nums, val):
    for idx in range(len(nums) - 1):
        if nums[idx] != val and nums[idx + 1] != val:
            return False
    return True

def either24(nums):
    found_22 = False
    found_44 = False
    for idx in range(len(nums)):
        if nums[idx:idx + 2] == [2, 2]:
            found_22 = True
        if nums[idx:idx + 2] == [4, 4]:
            found_44 = True
    return found_22 != found_44

def matchUp(nums1, nums2):
    count = 0
    for idx, num in enumerate(nums1):
        if num in [nums2[idx] - 2, nums2[idx] -1, nums2[idx] + 1, nums2[idx] + 2]:
            count += 1
    return count

def has77(nums):
    has_77 = False
    for idx in range(len(nums)):
        if nums[idx] == 7 and (nums[idx + 1:idx + 2] == [7] or nums[idx + 2:idx + 3] == [7]):
            has_77 = True
    return has_77

def has12(nums):
    for idx in range(len(nums) - 1):
        if nums[idx] == 1 and 2 in nums[idx + 1:]:
            return True
    return False

def modThree(nums):
    for idx in range(len(nums) - 2):
        if nums[idx] % 2 == nums[idx + 1] % 2 == nums[idx + 2] % 2:
            return True
    return False

def haveThree(nums):
    three_count = 0
    for idx in range(len(nums)):
        if nums[idx] == 3 and (nums[idx - 1:idx] != [3] and nums[idx + 1:idx + 2] != [3]):
            three_count += 1
    return three_count == 3

def twoTwo(nums):
    for idx in range(len(nums)):
        if nums[idx] == 2 and nums[idx + 1:idx + 2] != [2] and nums[idx - 1:idx] != [2]:
            return False
    return True

def sameEnds(nums, length):
    return nums[0:length] == nums[len(nums) - length:]

def tripleUp(nums):
    for idx in range(len(nums) - 2):
        if nums[idx] == nums[idx + 1] - 1 == nums[idx + 2] - 2:
            return True
    return False

def fizzArray3(start, end):
    return list(range(start, end))

def shiftLeft(nums):
    return nums[1:] + nums[:1]

def tenRun(nums):
    ten_mult = None
    for idx in range(len(nums)):
        if not nums[idx] % 10:
            ten_mult = nums[idx]
        nums[idx] = nums[idx] if ten_mult is None else ten_mult
    return nums

def pre4(nums):
    return nums[0:nums.index(4)]

def post4(nums):
    if 4 not in nums:
        return nums
    else:
        return post4(nums[1:])

def notAlone(nums, val):
    for idx in range(1, len(nums) - 1):
        if nums[idx] == val and nums[idx - 1] != val != nums[idx + 1]:
            nums[idx] = max(nums[idx - 1], nums[idx + 1])
    return nums

def zeroFront(nums):
    return [num for num in nums if num == 0] + [num for num in nums if num != 0]

def withoutTen(nums):
    return [x for x in nums if x != 10] + [0 for x in nums if x == 10]

def zeroMax(nums):
    for idx in range(len(nums)):
        if nums[idx] == 0:
            nums[idx] = max([nums[idx]] + [x for x in nums[idx + 1:] if x % 2])
    return nums

def evenOdd(nums):
    return [x for x in nums if not x % 2] + [x for x in nums if x % 2]

def fizzBuzz(start, end):
    nums = list(range(start, end))
    for idx, num in enumerate(nums):
        if not num % 3:
            nums[idx] = 'Fizz'
        if not num % 5:
            nums[idx] = 'Buzz'
        if not num % 15:
            nums[idx] = 'FizzBuzz'
    return [str(x) for x in nums]


assert count_evens([2, 1, 2, 3, 4]) == 3
assert count_evens([2, 2, 0]) == 3
assert count_evens([1, 3, 5]) == 0
assert count_evens([]) == 0
assert count_evens([11, 9, 0, 1]) == 1
assert count_evens([2, 11, 9, 0]) == 2
assert count_evens([2]) == 1
assert count_evens([2, 5, 12]) == 2

assert big_diff([10, 3, 5, 6]) == 7
assert big_diff([7, 2, 10, 9]) == 8
assert big_diff([2, 10, 7, 2]) == 8
assert big_diff([2, 10]) == 8
assert big_diff([10, 2]) == 8
assert big_diff([10, 0]) == 10
assert big_diff([2, 3]) == 1
assert big_diff([2, 2]) == 0
assert big_diff([2]) == 0
assert big_diff([5, 1, 6, 1, 9, 9]) == 8
assert big_diff([7, 6, 8, 5]) == 3
assert big_diff([7, 7, 6, 8, 5, 5, 6]) == 3

assert centered_average([1, 2, 3, 4, 100]) == 3
assert centered_average([1, 1, 5, 5, 10, 8, 7]) == 5
assert centered_average([-10, -4, -2, -4, -2, 0]) == -3
assert centered_average([5, 3, 4, 6, 2]) == 4
assert centered_average([5, 3, 4, 0, 100]) == 4
assert centered_average([100, 0, 5, 3, 4]) == 4
assert centered_average([4, 0, 100]) == 4
assert centered_average([0, 2, 3, 4, 100]) == 3
assert centered_average([1, 1, 100]) == 1
assert centered_average([7, 7, 7]) == 7
assert centered_average([1, 7, 8]) == 7
assert centered_average([1, 1, 99, 99]) == 50
assert centered_average([1000, 0, 1, 99]) == 50
assert centered_average([4, 4, 4, 4, 5]) == 4
assert centered_average([4, 4, 4, 1, 5]) == 4
assert centered_average([6, 4, 8, 12, 3]) == 6

assert sum67([1, 2, 2]) == 5
assert sum67([1, 2, 2, 6, 99, 99, 7]) == 5
assert sum67([1, 1, 6, 7, 2]) == 4
assert sum67([1, 6, 2, 2, 7, 1, 6, 99, 99, 7]) == 2
assert sum67([1, 6, 2, 6, 2, 7, 1, 6, 99, 99, 7]) == 2
assert sum67([2, 7, 6, 2, 6, 7, 2, 7]) == 18
assert sum67([2, 7, 6, 2, 6, 2, 7]) == 9
assert sum67([1, 6, 7, 7]) == 8
assert sum67([6, 7, 1, 6, 7, 7]) == 8
assert sum67([6, 8, 1, 6, 7]) == 0
assert sum67([]) == 0
assert sum67([6, 7, 11]) == 11
assert sum67([11, 6, 7, 11]) == 22
assert sum67([2, 2, 6, 7, 7]) == 11

assert sum13([1, 2, 2, 1]) == 6
assert sum13([1, 1]) == 2
assert sum13([1, 2, 2, 1, 13]) == 6
assert sum13([1, 2, 13, 2, 1, 13]) == 4
assert sum13([13, 1, 2, 13, 2, 1, 13]) == 3
assert sum13([]) == 0
assert sum13([13]) == 0
assert sum13([13, 13]) == 0
assert sum13([13, 0, 13]) == 0
assert sum13([13, 1, 13]) == 0
assert sum13([5, 7, 2]) == 14
assert sum13([5, 13, 2]) == 5
assert sum13([0]) == 0
assert sum13([13, 0]) == 0
assert sum13([13, 13, 1]) == 0
assert sum13([2, 13, 13, 1]) == 2

assert has22([1, 2, 2]) == True
assert has22([1, 2, 1, 2]) == False
assert has22([2, 1, 2]) == False
assert has22([2, 2, 1, 2]) == True
assert has22([1, 3, 2]) == False
assert has22([1, 3, 2, 2]) == True
assert has22([2, 3, 2, 2]) == True
assert has22([4, 2, 4, 2, 2, 5]) == True
assert has22([1, 2]) == False
assert has22([2, 2]) == True
assert has22([2]) == False
assert has22([]) == False
assert has22([3, 3, 2, 2]) == True
assert has22([5, 2, 5, 2]) == False

assert lucky13([0, 2, 4]) == True
assert lucky13([1, 2, 3]) == False
assert lucky13([1, 2, 4]) == False
assert lucky13([2, 7, 2, 8]) == True
assert lucky13([2, 7, 1, 8]) == False
assert lucky13([3, 7, 2, 8]) == False
assert lucky13([2, 7, 2, 1]) == False
assert lucky13([1, 2]) == False
assert lucky13([2, 2]) == True
assert lucky13([2]) == True
assert lucky13([3]) == False
assert lucky13([]) == True

assert sum28([2, 3, 2, 2, 4, 2]) == True
assert sum28([2, 3, 2, 2, 4, 2, 2]) == False
assert sum28([1, 2, 3, 4]) == False
assert sum28([2, 2, 2, 2]) == True
assert sum28([1, 2, 2, 2, 2, 4]) == True
assert sum28([]) == False
assert sum28([2]) == False
assert sum28([8]) == False
assert sum28([2, 2, 2]) == False
assert sum28([2, 2, 2, 2, 2]) == False
assert sum28([1, 2, 2, 1, 2, 2]) == True
assert sum28([5, 2, 2, 2, 4, 2]) == True

assert more14([1, 4, 1]) == True
assert more14([1, 4, 1, 4]) == False
assert more14([1, 1]) == True
assert more14([1, 6, 6]) == True
assert more14([1]) == True
assert more14([1, 4]) == False
assert more14([6, 1, 1]) == True
assert more14([1, 6, 4]) == False
assert more14([1, 1, 4, 4, 1]) == True
assert more14([1, 1, 6, 4, 4, 1]) == True
assert more14([]) == False
assert more14([4, 1, 4, 6]) == False
assert more14([4, 1, 4, 6, 1]) == False
assert more14([1, 4, 1, 4, 1, 6]) == True

assert fizzArray(4) == [0, 1, 2, 3]
assert fizzArray(1) == [0]
assert fizzArray(10) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
assert fizzArray(0) == []
assert fizzArray(2) == [0, 1]
assert fizzArray(7) == [0, 1, 2, 3, 4, 5, 6]

assert only14([1, 4, 1, 4]) == True
assert only14([1, 4, 2, 4]) == False
assert only14([1, 1]) == True
assert only14([4, 1]) == True
assert only14([2]) == False
assert only14([]) == True
assert only14([1, 4, 1, 3]) == False
assert only14([3, 1, 3]) == False
assert only14([1]) == True
assert only14([4]) == True
assert only14([3, 4]) == False
assert only14([1, 3, 4]) == False
assert only14([1, 1, 1]) == True
assert only14([1, 1, 1, 5]) == False
assert only14([4, 1, 4, 1]) == True

assert fizzArray2(4) == ["0", "1", "2", "3"]
assert fizzArray2(10) == ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
assert fizzArray2(2) == ["0", "1"]
assert fizzArray2(1) == ["0"]
assert fizzArray2(0) == []
assert fizzArray2(7) == ["0", "1", "2", "3", "4", "5", "6"]
assert fizzArray2(9) == ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
assert fizzArray2(11) == ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

assert no14([1, 2, 3]) == True
assert no14([1, 2, 3, 4]) == False
assert no14([2, 3, 4]) == True
assert no14([1, 1, 4, 4]) == False
assert no14([2, 2, 4, 4]) == True
assert no14([2, 3, 4, 1]) == False
assert no14([2, 1, 1]) == True
assert no14([1, 4]) == False
assert no14([2]) == True
assert no14([2, 1]) == True
assert no14([1]) == True
assert no14([4]) == True
assert no14([]) == True
assert no14([1, 1, 1, 1]) == True
assert no14([9, 4, 4, 1]) == False
assert no14([4, 2, 3, 1]) == False
assert no14([4, 2, 3, 5]) == True
assert no14([4, 4, 2]) == True
assert no14([1, 4, 4]) == False

assert isEverywhere([1, 2, 1, 3], 1) == True
assert isEverywhere([1, 2, 1, 3], 2) == False
assert isEverywhere([1, 2, 1, 3, 4], 1) == False
assert isEverywhere([2, 1, 2, 1], 1) == True
assert isEverywhere([2, 1, 2, 1], 2) == True
assert isEverywhere([2, 1, 2, 3, 1], 2) == False
assert isEverywhere([3, 1], 3) == True
assert isEverywhere([3, 1], 2) == False
assert isEverywhere([3], 1) == True
assert isEverywhere([], 1) == True
assert isEverywhere([1, 2, 1, 2, 3, 2, 5], 2) == True
assert isEverywhere([1, 2, 1, 1, 1, 2], 2) == False
assert isEverywhere([2, 1, 2, 1, 1, 2], 2) == False
assert isEverywhere([2, 1, 2, 2, 2, 1, 1, 2], 2) == False
assert isEverywhere([2, 1, 2, 2, 2, 1, 2, 1], 2) == True
assert isEverywhere([2, 1, 2, 1, 2], 2) == True

assert either24([1, 2, 2]) == True
assert either24([4, 4, 1]) == True
assert either24([4, 4, 1, 2, 2]) == False
assert either24([1, 2, 3, 4]) == False
assert either24([3, 5, 9]) == False
assert either24([1, 2, 3, 4, 4]) == True
assert either24([2, 2, 3, 4]) == True
assert either24([1, 2, 3, 2, 2, 4]) == True
assert either24([1, 2, 3, 2, 2, 4, 4]) == False
assert either24([1, 2]) == False
assert either24([2, 2]) == True
assert either24([4, 4]) == True
assert either24([2]) == False
assert either24([]) == False

assert matchUp([1, 2, 3], [2, 3, 10]) == 2
assert matchUp([1, 2, 3], [2, 3, 5]) == 3
assert matchUp([1, 2, 3], [2, 3, 3]) == 2
assert matchUp([5, 3], [5, 5]) == 1
assert matchUp([5, 3], [4, 4]) == 2
assert matchUp([5, 3], [3, 3]) == 1
assert matchUp([5, 3], [2, 2]) == 1
assert matchUp([5, 3], [1, 1]) == 1
assert matchUp([5, 3], [0, 0]) == 0
assert matchUp([4], [4]) == 0
assert matchUp([4], [5]) == 1

assert has77([1, 7, 7]) == True
assert has77([1, 7, 1, 7]) == True
assert has77([1, 7, 1, 1, 7]) == False
assert has77([7, 7, 1, 1, 7]) == True
assert has77([2, 7, 2, 2, 7, 2]) == False
assert has77([2, 7, 2, 2, 7, 7]) == True
assert has77([7, 2, 7, 2, 2, 7]) == True
assert has77([7, 2, 6, 2, 2, 7]) == False
assert has77([7, 7, 7]) == True
assert has77([7, 1, 7]) == True
assert has77([7, 1, 1]) == False
assert has77([1, 2]) == False
assert has77([1, 7]) == False
assert has77([7]) == False

assert has12([1, 3, 2]) == True
assert has12([3, 1, 2]) == True
assert has12([3, 1, 4, 5, 2]) == True
assert has12([3, 1, 4, 5, 6]) == False
assert has12([3, 1, 4, 1, 6, 2]) == True
assert has12([2, 1, 4, 1, 6, 2]) == True
assert has12([2, 1, 4, 1, 6]) == False
assert has12([1]) == False
assert has12([2, 1, 3]) == False
assert has12([2, 1, 3, 2]) == True
assert has12([2]) == False
assert has12([3, 2]) == False
assert has12([3, 1, 3, 2]) == True
assert has12([3, 5, 9]) == False
assert has12([3, 5, 1]) == False
assert has12([3, 2, 1]) == False
assert has12([1, 2]) == True

assert modThree([2, 1, 3, 5]) == True
assert modThree([2, 1, 2, 5]) == False
assert modThree([2, 4, 2, 5]) == True
assert modThree([1, 2, 1, 2, 1]) == False
assert modThree([9, 9, 9]) == True
assert modThree([1, 2, 1]) == False
assert modThree([1, 2]) == False
assert modThree([1]) == False
assert modThree([]) == False
assert modThree([9, 7, 2, 9]) == False
assert modThree([9, 7, 2, 9, 2, 2]) == False
assert modThree([9, 7, 2, 9, 2, 2, 6]) == True

assert haveThree([3, 1, 3, 1, 3]) == True
assert haveThree([3, 1, 3, 3]) == False
assert haveThree([3, 4, 3, 3, 4]) == False
assert haveThree([1, 3, 1, 3, 1, 2]) == False
assert haveThree([1, 3, 1, 3, 1, 3]) == True
assert haveThree([1, 3, 3, 1, 3]) == False
assert haveThree([1, 3, 1, 3, 1, 3, 4, 3]) == False
assert haveThree([3, 4, 3, 4, 3, 4, 4]) == True
assert haveThree([3, 3, 3]) == False
assert haveThree([1, 3]) == False
assert haveThree([3]) == False
assert haveThree([1]) == False

assert twoTwo([4, 2, 2, 3]) == True
assert twoTwo([2, 2, 4]) == True
assert twoTwo([2, 2, 4, 2]) == False
assert twoTwo([1, 3, 4]) == True
assert twoTwo([1, 2, 2, 3, 4]) == True
assert twoTwo([1, 2, 3, 4]) == False
assert twoTwo([2, 2]) == True
assert twoTwo([2, 2, 7]) == True
assert twoTwo([2, 2, 7, 2, 1]) == False
assert twoTwo([4, 2, 2, 2]) == True
assert twoTwo([2, 2, 2]) == True
assert twoTwo([1, 2]) == False
assert twoTwo([2]) == False
assert twoTwo([1]) == True
assert twoTwo([]) == True
assert twoTwo([5, 2, 2, 3]) == True
assert twoTwo([2, 2, 5, 2]) == False

assert sameEnds([5, 6, 45, 99, 13, 5, 6], 1) == False
assert sameEnds([5, 6, 45, 99, 13, 5, 6], 2) == True
assert sameEnds([5, 6, 45, 99, 13, 5, 6], 3) == False
assert sameEnds([1, 2, 5, 2, 1], 1) == True
assert sameEnds([1, 2, 5, 2, 1], 2) == False
assert sameEnds([1, 2, 5, 2, 1], 0) == True
assert sameEnds([1, 2, 5, 2, 1], 5) == True
assert sameEnds([1, 1, 1], 0) == True
assert sameEnds([1, 1, 1], 1) == True
assert sameEnds([1, 1, 1], 2) == True
assert sameEnds([1, 1, 1], 3) == True
assert sameEnds([1], 1) == True
assert sameEnds([], 0) == True
assert sameEnds([4, 2, 4, 5], 1) == False

assert tripleUp([1, 4, 5, 6, 2]) == True
assert tripleUp([1, 2, 3]) == True
assert tripleUp([1, 2, 4]) == False
assert tripleUp([1, 2, 4, 5, 7, 6, 5, 6, 7, 6]) == True
assert tripleUp([1, 2, 4, 5, 7, 6, 5, 7, 7, 6]) == False
assert tripleUp([1, 2]) == False
assert tripleUp([1]) == False
assert tripleUp([]) == False
assert tripleUp([10, 9, 8, -100, -99, -98, 100]) == True
assert tripleUp([10, 9, 8, -100, -99, 99, 100]) == False
assert tripleUp([-100, -99, -99, 100, 101, 102]) == True
assert tripleUp([2, 3, 5, 6, 8, 9, 2, 3]) == False

assert fizzArray3(5, 10) == [5, 6, 7, 8, 9]
assert fizzArray3(11, 18) == [11, 12, 13, 14, 15, 16, 17]
assert fizzArray3(1, 3) == [1, 2]
assert fizzArray3(1, 2) == [1]
assert fizzArray3(1, 1) == []
assert fizzArray3(1000, 1005) == [1000, 1001, 1002, 1003, 1004]

assert shiftLeft([6, 2, 5, 3]) == [2, 5, 3, 6]
assert shiftLeft([1, 2]) == [2, 1]
assert shiftLeft([1]) == [1]
assert shiftLeft([]) == []
assert shiftLeft([1, 1, 2, 2, 4]) == [1, 2, 2, 4, 1]
assert shiftLeft([1, 1, 1]) == [1, 1, 1]
assert shiftLeft([1, 2, 3]) == [2, 3, 1]

assert tenRun([2, 10, 3, 4, 20, 5]) == [2, 10, 10, 10, 20, 20]
assert tenRun([10, 1, 20, 2]) == [10, 10, 20, 20]
assert tenRun([10, 1, 9, 20]) == [10, 10, 10, 20]
assert tenRun([1, 2, 50, 1]) == [1, 2, 50, 50]
assert tenRun([1, 20, 50, 1]) == [1, 20, 50, 50]
assert tenRun([10, 10]) == [10, 10]
assert tenRun([10, 2]) == [10, 10]
assert tenRun([0, 2]) == [0, 0]
assert tenRun([1, 2]) == [1, 2]
assert tenRun([1]) == [1]
assert tenRun([]) == []

assert pre4([1, 2, 4, 1]) == [1, 2]
assert pre4([3, 1, 4]) == [3, 1]
assert pre4([1, 4, 4]) == [1]
assert pre4([1, 4, 4, 2]) == [1]
assert pre4([1, 3, 4, 2, 4]) == [1, 3]
assert pre4([4, 4]) == []
assert pre4([3, 3, 4]) == [3, 3]
assert pre4([1, 2, 1, 4]) == [1, 2, 1]
assert pre4([2, 1, 4, 2]) == [2, 1]
assert pre4([2, 1, 2, 1, 4, 2]) == [2, 1, 2, 1]

assert post4([2, 4, 1, 2]) == [1, 2]
assert post4([4, 1, 4, 2]) == [2]
assert post4([4, 4, 1, 2, 3]) == [1, 2, 3]
assert post4([4, 2]) == [2]
assert post4([4, 4, 3]) == [3]
assert post4([4, 4]) == []
assert post4([4]) == []
assert post4([2, 4, 1, 4, 3, 2]) == [3, 2]
assert post4([4, 1, 4, 2, 2, 2]) == [2, 2, 2]
assert post4([3, 4, 3, 2]) == [3, 2]

assert notAlone([1, 2, 3], 2) == [1, 3, 3]
assert notAlone([1, 2, 3, 2, 5, 2], 2) == [1, 3, 3, 5, 5, 2]
assert notAlone([3, 4], 3) == [3, 4]
assert notAlone([3, 3], 3) == [3, 3]
assert notAlone([1, 3, 1, 2], 1) == [1, 3, 3, 2]
assert notAlone([3], 3) == [3]
assert notAlone([], 3) == []
assert notAlone([7, 1, 6], 1) == [7, 7, 6]
assert notAlone([1, 1, 1], 1) == [1, 1, 1]
assert notAlone([1, 1, 1, 2], 1) == [1, 1, 1, 2]

assert zeroFront([1, 0, 0, 1]) == [0, 0, 1, 1]
assert zeroFront([0, 1, 1, 0, 1]) == [0, 0, 1, 1, 1]
assert zeroFront([1, 0]) == [0, 1]
assert zeroFront([0, 1]) == [0, 1]
assert zeroFront([1, 1, 1, 0]) == [0, 1, 1, 1]
assert zeroFront([2, 2, 2, 2]) == [2, 2, 2, 2]
assert zeroFront([0, 0, 1, 0]) == [0, 0, 0, 1]
assert zeroFront([-1, 0, 0, -1, 0]) == [0, 0, 0, -1, -1]
assert zeroFront([0, -3, 0, -3]) == [0, 0, -3, -3]
assert zeroFront([]) == []
assert zeroFront([9, 9, 0, 9, 0, 9]) == [0, 0, 9, 9, 9, 9]

assert withoutTen([1, 10, 10, 2]) == [1, 2, 0, 0]
assert withoutTen([10, 2, 10]) == [2, 0, 0]
assert withoutTen([1, 99, 10]) == [1, 99, 0]
assert withoutTen([10, 13, 10, 14]) == [13, 14, 0, 0]
assert withoutTen([10, 13, 10, 14, 10]) == [13, 14, 0, 0, 0]
assert withoutTen([10, 10, 3]) == [3, 0, 0]
assert withoutTen([1]) == [1]
assert withoutTen([13, 1]) == [13, 1]
assert withoutTen([10]) == [0]
assert withoutTen([]) == []

assert zeroMax([0, 5, 0, 3]) == [5, 5, 3, 3]
assert zeroMax([0, 4, 0, 3]) == [3, 4, 3, 3]
assert zeroMax([0, 1, 0]) == [1, 1, 0]
assert zeroMax([0, 1, 5]) == [5, 1, 5]
assert zeroMax([0, 2, 0]) == [0, 2, 0]
assert zeroMax([1]) == [1]
assert zeroMax([0]) == [0]
assert zeroMax([]) == []
assert zeroMax([7, 0, 4, 3, 0, 2]) == [7, 3, 4, 3, 0, 2]
assert zeroMax([7, 0, 4, 3, 0, 1]) == [7, 3, 4, 3, 1, 1]
assert zeroMax([7, 0, 4, 3, 0, 0]) == [7, 3, 4, 3, 0, 0]
assert zeroMax([7, 0, 1, 0, 0, 7]) == [7, 7, 1, 7, 7, 7]

assert evenOdd([1, 0, 1, 0, 0, 1, 1]) == [0, 0, 0, 1, 1, 1, 1]
assert evenOdd([3, 3, 2]) == [2, 3, 3]
assert evenOdd([2, 2, 2]) == [2, 2, 2]
assert evenOdd([3, 2, 2]) == [2, 2, 3]
assert evenOdd([1, 1, 0, 1, 0]) == [0, 0, 1, 1, 1]
assert evenOdd([1]) == [1]
assert evenOdd([1, 2]) == [2, 1]
assert evenOdd([2, 1]) == [2, 1]
assert evenOdd([]) == []

assert fizzBuzz(1, 6) == ["1", "2", "Fizz", "4", "Buzz"]
assert fizzBuzz(1, 8) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7"]
assert fizzBuzz(1, 11) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz"]
assert fizzBuzz(1, 16) == ["1", "2", "Fizz", "4", "Buzz", "Fizz", "7", "8", "Fizz", "Buzz", "11", "Fizz", "13", "14", "FizzBuzz"]
assert fizzBuzz(1, 4) == ["1", "2", "Fizz"]
assert fizzBuzz(1, 2) == ["1"]
assert fizzBuzz(50, 56) == ["Buzz", "Fizz", "52", "53", "Fizz", "Buzz"]
assert fizzBuzz(15, 17) == ["FizzBuzz", "16"]
assert fizzBuzz(30, 36) == ["FizzBuzz", "31", "32", "Fizz", "34", "Buzz"]
assert fizzBuzz(1000, 1006) == ["Buzz", "1001", "Fizz", "1003", "1004", "FizzBuzz"]
assert fizzBuzz(99, 102) == ["Fizz", "Buzz", "101"]
assert fizzBuzz(14, 20) == ["14", "FizzBuzz", "16", "17", "Fizz", "19"]