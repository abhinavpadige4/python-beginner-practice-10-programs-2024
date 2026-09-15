"""
Program 8: Count word frequencies in a sentence using a dictionary
Concept: Dictionaries (creation, access, update) + Loops
"""

def count_word_frequencies(sentence):
    """
    Count the frequency of each word in a sentence using a dictionary.
    
    Args:
        sentence: Input string
        
    Returns:
        dict: Dictionary with words as keys and their frequencies as values
    """
    # Convert to lowercase and split into words
    words = sentence.lower().split()
    
    # Create empty dictionary to store word frequencies
    frequency = {}
    
    # Count each word
    for word in words:
        # Remove punctuation from the word
        word = word.strip('.,!?;:"()[]{}')
        
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    
    return frequency

def print_frequency_dict(frequency_dict):
    """Print the frequency dictionary in a readable format."""
    print("Word Frequencies:")
    print("-" * 20)
    for word, count in sorted(frequency_dict.items()):
        print(f"'{word}': {count}")

if __name__ == "__main__":
    # Test with input 'test test demo'
    test_sentence = "test test demo"
    result = count_word_frequencies(test_sentence)
    print(f"Input sentence: '{test_sentence}'")
    print_frequency_dict(result)
    print()
    
    # Additional test with more complex sentence
    complex_sentence = "The quick brown fox jumps over the lazy dog. The dog was really lazy!"
    result2 = count_word_frequencies(complex_sentence)
    print(f"Input sentence: '{complex_sentence}'")
    print_frequency_dict(result2)