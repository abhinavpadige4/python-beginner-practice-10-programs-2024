"""
Program 10: Loop over dictionary to find keys with values above threshold
Concept: Dictionaries (access, iteration) + Loops
"""

def find_keys_above_threshold(scores_dict, threshold):
    """
    Find all keys in a dictionary where the value is above a given threshold.
    
    Args:
        scores_dict: Dictionary with keys and numeric values
        threshold: Numeric threshold value
        
    Returns:
        list: List of keys where values are above the threshold
    """
    result = []
    
    # Loop through dictionary items
    for key, value in scores_dict.items():
        if value > threshold:
            result.append(key)
    
    return result

def find_keys_above_threshold_v2(scores_dict, threshold):
    """
    Alternative implementation using list comprehension.
    
    Args:
        scores_dict: Dictionary with keys and numeric values
        threshold: Numeric threshold value
        
    Returns:
        list: List of keys where values are above the threshold
    """
    return [key for key, value in scores_dict.items() if value > threshold]

if __name__ == "__main__":
    # Test with dictionary of scores
    scores = {
        "Alice": 85,
        "Bob": 92,
        "Charlie": 78,
        "Diana": 96,
        "Eve": 83,
        "Frank": 79
    }
    
    threshold = 80
    
    print("Student Scores:")
    print("-" * 20)
    for name, score in scores.items():
        print(f"{name}: {score}")
    print()
    
    # Find students with scores above threshold
    result1 = find_keys_above_threshold(scores, threshold)
    result2 = find_keys_above_threshold_v2(scores, threshold)
    
    print(f"Students with scores above {threshold}:")
    print(f"Method 1 (loop): {result1}")
    print(f"Method 2 (list comprehension): {result2}")
    print()
    
    # Test with different threshold
    threshold2 = 90
    result3 = find_keys_above_threshold(scores, threshold2)
    print(f"Students with scores above {threshold2}: {result3}")
    print()
    
    # Test with no matches
    threshold3 = 100
    result4 = find_keys_above_threshold(scores, threshold3)
    print(f"Students with scores above {threshold3}: {result4} (no matches)")