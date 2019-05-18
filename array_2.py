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