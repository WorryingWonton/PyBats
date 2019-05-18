# https://codingbat.com/java/Recursion-2
def groupSum(start, nums, target):
    if start == len(nums):
        return target == 0
    if groupSum(start + 1, nums, target - nums[start]):
        return True
    else:
        return groupSum(start + 1, nums, target)

def groupSum6(start, nums, target):
    if start == len(nums):
        return target == 0
    if groupSum6(start + 1, nums, target - nums[start]):
        return True
    else:
        return groupSum6(start + 1, nums, target - (nums[start] if nums[start] == 6 else 0))

def groupNoAdj(start, nums, target):
    if start >= len(nums):
        return target == 0
    if groupNoAdj(start + 2, nums, target - nums[start]):
        return True
    else:
        return groupNoAdj(start + 1, nums, target)

def groupSum5(start, nums, target):
    if start == len(nums):
        return target == 0
    if groupSum5(start + 1, nums, target - (0 if not nums[start - 1] % 5 and nums[start] == 1 else nums[start])):
        return True
    else:
        return groupSum5(start + 1, nums, target - (nums[start] if not nums[start] % 5 else 0))

def groupSumClump(start, nums, target):
    if start >= len(nums):
        return target == 0
    sum = nums[start]
    while start < len(nums) - 1 and nums[start] == nums[start + 1]:
        sum += nums[start]
        start += 1
    if groupSumClump(start + 1, nums, target - sum):
        return True
    else:
        return groupSumClump(start + 1, nums, target)

def splitArray(nums):
    return splitArrayHelper(0, 0, 0, nums)

def splitArrayHelper(start, l_sum, r_sum, nums):
    if start == len(nums):
        return l_sum == r_sum and l_sum + r_sum == sum(nums)
    if splitArrayHelper(start + 1, l_sum + nums[start], r_sum, nums):
        return True
    if splitArrayHelper(start + 1, l_sum, r_sum + nums[start], nums):
        return True
    else:
        return splitArrayHelper(start + 1, l_sum, r_sum, nums)

def splitOdd10(nums):
    return splitOdd10Helper(0, 0, 0, nums)

def splitOdd10Helper(start, ten_sum, odd_sum, nums):
    if start == len(nums):
        return (not ten_sum % 10 and odd_sum % 2) and ten_sum + odd_sum == sum(nums)
    if splitOdd10Helper(start + 1, ten_sum + nums[start], odd_sum, nums):
        return True
    if splitOdd10Helper(start + 1, ten_sum, odd_sum + nums[start], nums):
        return True
    else:
        return splitOdd10Helper(start + 1, ten_sum, odd_sum, nums)

def split53(nums):
    return split53Helper(0, 0, 0, nums)

def split53Helper(start, three_sum, five_sum, nums):
    if start == len(nums):
        return three_sum == five_sum and three_sum + five_sum == sum(nums)
    if split53Helper(start + 1, three_sum + (nums[start] if nums[start] % 5 else 0), five_sum, nums):
        return True
    if split53Helper(start + 1, three_sum, five_sum + (nums[start] if nums[start] % 3 else 0), nums):
        return True
    else:
        return split53Helper(start + 1, three_sum, five_sum, nums)


assert groupSum(0, [2, 4, 8], 10) == True
assert groupSum(0, [2, 4, 8], 14) == True
assert groupSum(0, [2, 4, 8], 9) == False
assert groupSum(0, [2, 4, 8], 8) == True
assert groupSum(1, [2, 4, 8], 8) == True
assert groupSum(1, [2, 4, 8], 2) == False
assert groupSum(0, [1], 1) == True
assert groupSum(0, [9], 1) == False
assert groupSum(1, [9], 0) == True
assert groupSum(0, [], 0) == True
assert groupSum(0, [10, 2, 2, 5], 17) == True
assert groupSum(0, [10, 2, 2, 5], 15) == True
assert groupSum(0, [10, 2, 2, 5], 9) == True

assert groupSum6(0, [5, 6, 2], 8) == True
assert groupSum6(0, [5, 6, 2], 9) == False
assert groupSum6(0, [5, 6, 2], 7) == False
assert groupSum6(0, [1], 1) == True
assert groupSum6(0, [9], 1) == False
assert groupSum6(0, [], 0) == True
assert groupSum6(0, [3, 2, 4, 6], 8) == True
assert groupSum6(0, [6, 2, 4, 3], 8) == True
assert groupSum6(0, [5, 2, 4, 6], 9) == False
assert groupSum6(0, [6, 2, 4, 5], 9) == False
assert groupSum6(0, [3, 2, 4, 6], 3) == False
assert groupSum6(0, [1, 6, 2, 6, 4], 12) == True
assert groupSum6(0, [1, 6, 2, 6, 4], 13) == True
assert groupSum6(0, [1, 6, 2, 6, 4], 4) == False
assert groupSum6(0, [1, 6, 2, 6, 4], 9) == False
assert groupSum6(0, [1, 6, 2, 6, 5], 14) == True
assert groupSum6(0, [1, 6, 2, 6, 5], 15) == True
assert groupSum6(0, [1, 6, 2, 6, 5], 16) == False

assert groupNoAdj(0, [2, 5, 10, 4], 12) == True
assert groupNoAdj(0, [2, 5, 10, 4], 14) == False
assert groupNoAdj(0, [2, 5, 10, 4], 7) == False
assert groupNoAdj(0, [2, 5, 10, 4, 2], 7) == True
assert groupNoAdj(0, [2, 5, 10, 4], 9) == True
assert groupNoAdj(0, [10, 2, 2, 3, 3], 15) == True
assert groupNoAdj(0, [10, 2, 2, 3, 3], 7) == False
assert groupNoAdj(0, [], 0) == True
assert groupNoAdj(0, [1], 1) == True
assert groupNoAdj(0, [9], 1) == False
assert groupNoAdj(0, [9], 0) == True
assert groupNoAdj(0, [5, 10, 4, 1], 11) == True

assert groupSum5(0, [2, 5, 10, 4], 19) == True
assert groupSum5(0, [2, 5, 10, 4], 17) == True
assert groupSum5(0, [2, 5, 10, 4], 12) == False
assert groupSum5(0, [2, 5, 4, 10], 12) == False
assert groupSum5(0, [3, 5, 4], 4) == False
assert groupSum5(0, [3, 5, 1], 5) == True
assert groupSum5(0, [1, 3, 5], 5) == True
assert groupSum5(0, [3, 5, 1], 9) == False
assert groupSum5(0, [5, 1, 3, 5, 1], 10) == True
assert groupSum5(0, [2, 5, 10, 4], 7) == False
assert groupSum5(0, [2, 5, 10, 4], 15) == True
assert groupSum5(0, [2, 5, 10, 4], 11) == False
assert groupSum5(0, [1], 1) == True
assert groupSum5(0, [9], 1) == False
assert groupSum5(0, [9], 0) == True
assert groupSum5(0, [], 0) == True

assert groupSumClump(0, [2, 4, 8], 10) == True
assert groupSumClump(0, [1, 2, 4, 8, 1], 14) == True
assert groupSumClump(0, [2, 4, 4, 8], 14) == False
assert groupSumClump(0, [8, 2, 2, 1], 9) == True
assert groupSumClump(0, [8, 2, 2, 1], 11) == False
assert groupSumClump(0, [1], 1) == True
assert groupSumClump(0, [9], 1) == False

assert splitArray([2, 2]) == True
assert splitArray([2, 3]) == False
assert splitArray([5, 2, 3]) == True
assert splitArray([5, 2, 2]) == False
assert splitArray([1, 1, 1, 1, 1, 1]) == True
assert splitArray([1, 1, 1, 1, 1]) == False
assert splitArray([]) == True
assert splitArray([1]) == False
assert splitArray([3, 5]) == False
assert splitArray([5, 3, 2]) == True
assert splitArray([2, 2, 10, 10, 1, 1]) == True
assert splitArray([1, 2, 2, 10, 10, 1, 1]) == False
assert splitArray([1, 2, 3, 10, 10, 1, 1]) == True

assert splitOdd10([5, 5, 5]) == True
assert splitOdd10([5, 5, 6]) == False
assert splitOdd10([5, 5, 6, 1]) == True
assert splitOdd10([6, 5, 5, 1]) == True
assert splitOdd10([6, 5, 5, 1, 10]) == True
assert splitOdd10([6, 5, 5, 5, 1]) == False
assert splitOdd10([1]) == True
assert splitOdd10([]) == False
assert splitOdd10([10, 7, 5, 5]) == True
assert splitOdd10([10, 0, 5, 5]) == False
assert splitOdd10([10, 7, 5, 5, 2]) == True
assert splitOdd10([10, 7, 5, 5, 1]) == False

assert split53([1, 1]) == True
assert split53([1, 1, 1]) == False
assert split53([2, 4, 2]) == True
assert split53([2, 2, 2, 1]) == False
assert split53([3, 3, 5, 1]) == True
assert split53([3, 5, 8]) == False
assert split53([2, 4, 6]) == True
assert split53([3, 5, 6, 10, 3, 3]) == True