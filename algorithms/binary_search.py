
from typing import List

def binary_search(nums: List[int], target: int) -> int:
    nums.sort()

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        result = nums[mid]

        if result == target:
            return mid
        elif result > target:
            right = mid -1
        elif result < target:
            left = mid + 1
    
    return -1
