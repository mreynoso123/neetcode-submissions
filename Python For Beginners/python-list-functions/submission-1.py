from typing import List # this is used to add type hints for List type

def get_sum(nums: List[int]) -> int:
    total_sum = 0
    for num in nums:
        total_sum += num
    return total_sum

def get_min(nums: List[int]) -> int:
    current_min = nums[0]
    for num in nums:
        if num < current_min:
            current_min = num
    return current_min

def get_max(nums: List[int]) -> int:
    current_max = nums[0]
    for num in nums:
        if num > current_max:
            current_max = num
    return current_max

# do not modify below this line
print(get_sum([1, 2, 3, 4, 5]))
print(get_sum([5, 4, 5, 6]))

print(get_min([7, 3, 4, 5]))
print(get_min([5, 4, 5, 6]))

print(get_max([7, 3, 4, 5]))
print(get_max([5, 4, 5, 6]))
