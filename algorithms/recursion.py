def bunnyEars(n: int) -> int:
    """We have a number of bunnies and each bunny has two big
    floppy ears. We want to compute the total number of ears
    across all the bunnies recursively
    (without loops or multiplication).
    bunnyEars(0) → 0
    bunnyEars(1) → 2
    bunnyEars(2) → 4
    """
    
    if n == 0:
        return 0

    return 2 + bunnyEars(n - 1)


def factorial(n: int) -> int:
    """
    Given n of 1 or more, return the factorial of n, 
    which is n * (n-1) * (n-2) ... 1. 
    Compute the result recursively (without loops).
    factorial(1) → 1
    factorial(2) → 2
    factorial(3) → 6
    """
    if n == 1:
        return 1

    return n * factorial(n - 1)


def fibonacci(n: int) -> int:
    """
    The fibonacci sequence is a famous bit of mathematics,
    and it happens to have a recursive definition.
    The first two values in the sequence are 0 and 1
    (essentially 2 base cases). Each subsequent value 
    is the sum of the previous two values, so the whole
    sequence is: 0, 1, 1, 2, 3, 5, 8, 13, 21 and so on. 
    
    Define a recursive fibonacci(n) method that returns the 
    nth fibonacci number, with n=0 representing the start of 
    the sequence.
    fibonacci(0) → 0
    fibonacci(1) → 1
    fibonacci(2) → 1
    """
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def bunnyEars2(n: int) -> int:
    """    
    We have bunnies standing in a line, numbered 1, 2, ... The odd bunnies (1, 3, ..) have the normal 2 ears. The even bunnies (2, 4, ..) have 3 ears, because they each have a raised foot. Recursively return the number of "ears" in the bunny line 1, 2, ... n (without loops or multiplication).
    bunnyEars2(0) → 0
    bunnyEars2(1) → 2
    bunnyEars2(2) → 5
    """

    if n == 0:
        return 0

    if n % 2 == 0:
        return 3 + bunnyEars2(n-1)
    else:
        return 2 + bunnyEars2(n-1)
    
    
def triangle(n: int) -> int:
    """"
    We have triangle made of blocks. The topmost row has 1 block, the next row down has 2 blocks, the next row has 3 blocks, and so on. Compute recursively (no loops or multiplication) the total number of blocks in such a triangle with the given number of rows.
    triangle(0) → 0
    triangle(1) → 1
    triangle(2) → 3
    """  

    if n == 0:
        return 0
    
    return n + triangle(n-1)
