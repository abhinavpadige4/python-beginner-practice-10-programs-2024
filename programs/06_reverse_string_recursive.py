"""
Program 6: Recursive string reversal
Concept: Recursion (base case, recursive step)
"""

def reverse_string(s):
    """
    Reverse a string using recursion.
    
    Args:
        s: Input string
        
    Returns:
        str: Reversed string
        
    Base case: Empty string or single character returns itself
    Recursive step: reverse_string(s) = reverse_string(s[1:]) + s[0]
    """
    # Base case
    if len(s) <= 1:
        return s
    
    # Recursive case
    return reverse_string(s[1:]) + s[0]

if __name__ == "__main__":
    # Test with input 'hello'
    test_string = "hello"
    reversed_string = reverse_string(test_string)
    print(f"Original: '{test_string}'")
    print(f"Reversed: '{reversed_string}'")
    
    # Additional test cases
    print(f"Reverse of 'Python': '{reverse_string('Python')}'")
    print(f"Reverse of 'a': '{reverse_string('a')}'")
    print(f"Reverse of '': '{reverse_string('')}'")