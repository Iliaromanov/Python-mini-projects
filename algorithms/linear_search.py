from typing import List

# 1. Search a list of ints for a particular integer. Return the index location, -1 if not found.

def find_num(nums: List[int], target: int) -> int:
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1


# 2. Search a list of ints for the last occurance of a particular integer. -1 if not found.

def find_last_num(nums: List[int], target: int) -> int:
    max_i = -1
    i = 0

    while i < len(nums):
        if nums[i] == target:
            if i > max_i:
                max_i = i
        i += 1
    return max_i


# 3. Search a list of ints for every occurance of a particular integer. Return a list of every index number. Empty list if not found. 

def find_all_occurences(nums: List[int], target: int) -> List[int]:
    new_list = []

    for i, num in enumerate(nums):
        if num == target:
            new_list.append(i)
    return new_list


# 4. Search a list of strings for words that start with a substring. Return the first occurance index.

def find_string(words: List[str], target: str) -> int:
    for i, word in enumerate(words):
        if word[:len(target)] == target:
            return i
        
        
# 5. Search a list of strings for words that start with a substring. Return list of all the strings (not the index positions).

def find_all_strings(words: List[str], target: str) -> List[str]:
    targets_found = []

    for word in words:
        if word[:len(target)] == target:
            targets_found.append(word)

    return targets_found 
