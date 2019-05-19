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
        if num != nums2[idx] and nums2[idx] in range(num - 2, num + 3):
            count += 1
    return count

def has77(nums):
    has_77 = False
    for idx in range(len(nums)):
        if nums[idx] == 7 and (nums[idx + 1:idx + 2] == [7] or nums[idx + 2:idx + 3] == [7]):
            has_77 = True
    return has_77


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