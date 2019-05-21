def maxSpan(nums):
    spans = []
    for num in set(nums):
        spans.append(len(nums) - list(reversed(nums)).index(num) - nums.index(num))
    return max(spans) if spans else 0

def fix34(nums):
    fours = [x[0] for x in enumerate(nums) if x[1] == 4]
    for idx in range(len(nums)):
        if nums[idx] == 3:
            nums[fours[0]] = nums[idx + 1]
            fours = fours[1:]
            nums[idx + 1] = 4
    return nums

def fix45(nums):
    for idx, val in enumerate(nums):
        if val == 4:
            temp = nums[idx + 1]
            nums[idx + 1] = 5
            for i in range(len(nums)):
                if nums[i] == 5 and nums[i - 1] != 4:
                    nums[i] = temp
                    break
    return nums

def canBalance(nums):
    l_sum = 0
    r_sum = sum(nums)
    for idx in range(len(nums)):
        if l_sum == r_sum:
            return True
        else:
            l_sum += nums[idx]
            r_sum -= nums[idx]
    return False

def linearIn(inner, outer):
    return not linearIn_helper(inner, outer)

def linearIn_helper(inner, outer):
    return (linearIn_helper(inner[1:], outer) if inner[0] != outer[0] else linearIn_helper(inner[1:], outer[1:])) if inner and outer else outer

def squareUp(num):
    return sum([y[:num - x] + list(range(x, 0, -1)) for x, y in enumerate([[0]*num]*num, start=1)], [])

def seriesUp(num):
    return sum([list(range(1, x[0] + 2)) for x in enumerate([[]]*num)], [])

def maxMirror(nums):
    max_size = 0
    for idx in range(len(nums)):
        p_matches = 0
        r_idx = len(nums) - 1
        while idx <= r_idx:
            if nums[idx + p_matches] == nums[r_idx]:
                p_matches += 1
            else:
                p_matches = 0
            r_idx -= 1
            max_size = max(max_size, p_matches)
    return max_size

def countClumps(nums):
    clumps = 0
    index = 0
    while index < len(nums):
        temp = nums[index]
        count = 0
        while index < len(nums) and temp == nums[index]:
            count += 1
            index += 1
        clumps += (1 if count > 1 else 0)
    return clumps


assert maxSpan([1, 2, 1, 1, 3]) == 4
assert maxSpan([1, 4, 2, 1, 4, 1, 4]) == 6
assert maxSpan([1, 4, 2, 1, 4, 4, 4]) == 6
assert maxSpan([3, 3, 3]) == 3
assert maxSpan([3, 9, 3]) == 3
assert maxSpan([3, 9, 9]) == 2
assert maxSpan([3, 9]) == 1
assert maxSpan([3, 3]) == 2
assert maxSpan([]) == 0
assert maxSpan([1]) == 1

assert fix34([1, 3, 1, 4]) == [1, 3, 4, 1]
assert fix34([1, 3, 1, 4, 4, 3, 1]) == [1, 3, 4, 1, 1, 3, 4]
assert fix34([3, 2, 2, 4]) == [3, 4, 2, 2]
assert fix34([3, 2, 3, 2, 4, 4]) == [3, 4, 3, 4, 2, 2]
assert fix34([2, 3, 2, 3, 2, 4, 4]) == [2, 3, 4, 3, 4, 2, 2]
assert fix34([5, 3, 5, 4, 5, 4, 5, 4, 3, 5, 3, 5]) == [5, 3, 4, 5, 5, 5, 5, 5, 3, 4, 3, 4]
assert fix34([3, 1, 4]) == [3, 4, 1]
assert fix34([3, 4, 1]) == [3, 4, 1]
assert fix34([1, 1, 1]) == [1, 1, 1]
assert fix34([1]) == [1]
assert fix34([]) == []
assert fix34([7, 3, 7, 7, 4]) == [7, 3, 4, 7, 7]
assert fix34([3, 1, 4, 3, 1, 4]) == [3, 4, 1, 3, 4, 1]
assert fix34([3, 1, 1, 3, 4, 4]) == [3, 4, 1, 3, 4, 1]

assert fix45([1, 2, 3, 5, 4, 3, 2, 4, 6, 5]) == [1, 2, 3, 3, 4, 5, 2, 4, 5, 6]
assert fix45([5, 4, 3, 4, 8, 5, 6, 4, 7, 5]) == [3, 4, 5, 4, 5, 8, 6, 4, 5, 7]
assert fix45([5, 4, 9, 4, 9, 5]) == [9, 4, 5, 4, 5, 9]
assert fix45([1, 4, 1, 5]) == [1, 4, 5, 1]
assert fix45([1, 4, 1, 5, 5, 4, 1]) == [1, 4, 5, 1, 1, 4, 5]
assert fix45([4, 9, 4, 9, 5, 5, 4, 9, 5]) == [4, 5, 4, 5, 9, 9, 4, 5, 9]
assert fix45([5, 5, 4, 1, 4, 1]) == [1, 1, 4, 5, 4, 5]
assert fix45([4, 2, 2, 5]) == [4, 5, 2, 2]
assert fix45([4, 2, 4, 2, 5, 5]) == [4, 5, 4, 5, 2, 2]
assert fix45([1, 1, 1]) == [1, 1, 1]
assert fix45([4, 5]) == [4, 5]
assert fix45([5, 4, 1]) == [1, 4, 5]
assert fix45([]) == []
assert fix45([5, 4, 5, 4, 1]) == [1, 4, 5, 4, 5]
assert fix45([4, 5, 4, 1, 5]) == [4, 5, 4, 5, 1]
assert fix45([3, 4, 5]) == [3, 4, 5]
assert fix45([4, 1, 5]) == [4, 5, 1]
assert fix45([5, 4, 1]) == [1, 4, 5]
assert fix45([2, 4, 2, 5]) == [2, 4, 5, 2]

assert canBalance([1, 1, 1, 2, 1]) == True
assert canBalance([2, 1, 1, 2, 1]) == False
assert canBalance([10, 10]) == True
assert canBalance([10, 0, 1, -1, 10]) == True
assert canBalance([1, 1, 1, 1, 4]) == True
assert canBalance([2, 1, 1, 1, 4]) == False
assert canBalance([2, 3, 4, 1, 2]) == False
assert canBalance([1, 2, 3, 1, 0, 2, 3]) == True
assert canBalance([1, 2, 3, 1, 0, 1, 3]) == False
assert canBalance([1]) == False
assert canBalance([1, 1, 1, 2, 1]) == True

assert linearIn([1, 2, 4, 6], [2, 4]) == True
assert linearIn([1, 2, 4, 6], [2, 3, 4]) == False
assert linearIn([1, 2, 4, 4, 6], [2, 4]) == True
assert linearIn([2, 2, 4, 4, 6, 6], [2, 4]) == True
assert linearIn([2, 2, 2, 2, 2], [2, 2]) == True
assert linearIn([2, 2, 2, 2, 2], [2, 4]) == False
assert linearIn([2, 2, 2, 2, 4], [2, 4]) == True
assert linearIn([1, 2, 3], [2]) == True
assert linearIn([1, 2, 3], [-1]) == False
assert linearIn([1, 2, 3], []) == True
assert linearIn([-1, 0, 3, 3, 3, 10, 12], [-1, 0, 3, 12]) == True
assert linearIn([-1, 0, 3, 3, 3, 10, 12], [0, 3, 12, 14]) == False
assert linearIn([-1, 0, 3, 3, 3, 10, 12], [-1, 10, 11]) == False

assert squareUp(3) == [0, 0, 1, 0, 2, 1, 3, 2, 1]
assert squareUp(2) == [0, 1, 2, 1]
assert squareUp(4) == [0, 0, 0, 1, 0, 0, 2, 1, 0, 3, 2, 1, 4, 3, 2, 1]
assert squareUp(1) == [1]
assert squareUp(0) == []
assert squareUp(6) == [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 1, 0, 0, 0, 3, 2, 1, 0, 0, 4, 3, 2, 1, 0, 5, 4, 3, 2, 1, 6, 5, 4, 3, 2, 1]

assert seriesUp(3) == [1, 1, 2, 1, 2, 3]
assert seriesUp(4) == [1, 1, 2, 1, 2, 3, 1, 2, 3, 4]
assert seriesUp(2) == [1, 1, 2]
assert seriesUp(1) == [1]
assert seriesUp(0) == []
assert seriesUp(6) == [1, 1, 2, 1, 2, 3, 1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6]

assert maxMirror([1, 2, 3, 8, 9, 3, 2, 1]) == 3
assert maxMirror([1, 2, 1, 4]) == 3
assert maxMirror([7, 1, 2, 9, 7, 2, 1]) == 2
assert maxMirror([21, 22, 9, 8, 7, 6, 23, 24, 6, 7, 8, 9, 25, 7, 8, 9]) == 4
assert maxMirror([1, 2, 1, 20, 21, 1, 2, 1, 2, 23, 24, 2, 1, 2, 1, 25]) == 4
assert maxMirror([1, 2, 3, 2, 1]) == 5
assert maxMirror([1, 2, 3, 3, 8]) == 2
assert maxMirror([1, 2, 7, 8, 1, 7, 2]) == 2
assert maxMirror([1, 1, 1]) == 3
assert maxMirror([1]) == 1
assert maxMirror([]) == 0
assert maxMirror([9, 1, 1, 4, 2, 1, 1, 1]) == 3
assert maxMirror([5, 9, 9, 4, 5, 4, 9, 9, 2]) == 7
assert maxMirror([5, 9, 9, 6, 5, 4, 9, 9, 2]) == 2
assert maxMirror([5, 9, 1, 6, 5, 4, 1, 9, 5]) == 3

assert countClumps([1, 2, 2, 3, 4, 4]) == 2
assert countClumps([1, 1, 2, 1, 1]) == 2
assert countClumps([1, 1, 1, 1, 1]) == 1
assert countClumps([1, 2, 3]) == 0
assert countClumps([2, 2, 1, 1, 1, 2, 1, 1, 2, 2]) == 4
assert countClumps([0, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2]) == 4
assert countClumps([0, 0, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2]) == 5
assert countClumps([0, 0, 0, 2, 2, 1, 1, 1, 2, 1, 1, 2, 2]) == 5
assert countClumps([]) == 0