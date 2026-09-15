"""
Program 4: Recursive factorial function
Concept: Recursion (base case, recursive step)
"""

def factorial(n):
    """
    Calculate factorial of a number using recursion.
    
    Args:
        n: Non-negative integer
        
    Returns:
        int: Factorial of n (n!)
        
    Base case: factorial(0) = 1
    Recursive step: factorial(n) = n * factorial(n-1)
    """
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Recursive case
    return n * factorial(n - 1)

if __name__ == "__main__":
    # Test with factorial of 5
    num = 5
    result = factorial(num)
    print(f"Factorial of {num} is {result}")
    
    # Additional test cases
    print(f"Factorial of 0 is {factorial(0)}")
    print(f"Factorial of 3 is {factorial(3)}")