from typing import List

# 1. Search a list of ints for a particular integer. Return the index location, -1 if not found.

def find_num(nums: List[int], target: int) -> int:
  for i, num in enumerate(nums):
      if num == target:
          return i
  return -1
