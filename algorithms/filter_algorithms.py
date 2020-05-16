
# 1. Create a function that will take a list of numbers and return a new list of only the even numbers from the original list.

def filter_evens(nums: List[int]) -> List[int]:
    new_list = []

    for num in nums:
        if num % 2 == 0:
            new_list.append(num)
    return new_list
