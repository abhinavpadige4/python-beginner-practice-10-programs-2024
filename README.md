# Python Beginner Practice: 10 Programs

This repository contains 10 Python practice programs designed for beginners to learn and practice:
- Loops (for/while, nested loops)
- Recursion (base case, recursive step)
- Dictionaries (creation, access, update, deletion, nesting)

## Programs Included

### 1. **01_print_numbers.py** - Simple for-loop to print numbers 1 to 10
**Concept:** Loops (for loop)
- Demonstrates basic for loop syntax with range()
- Prints numbers 1 through 10, each on a new line

### 2. **02_sum_while.py** - While-loop to compute sum of a list of integers
**Concept:** Loops (while loop)
- Uses while loop to iterate through list elements
- Accumulates sum using index-based access
- Test case: [5, 10, 15] → 30

### 3. **03_multiplication_table.py** - Nested for-loops to print a multiplication table (1-10)
**Concept:** Loops (nested for loops)
- Demonstrates nested loop structure
- Prints 10x10 multiplication table with proper formatting
- Shows how outer loop controls rows, inner loop controls columns

### 4. **04_factorial_recursive.py** - Recursive factorial function
**Concept:** Recursion (base case, recursive step)
- Implements factorial using recursion: n! = n × (n-1)!
- Base case: factorial(0) = 1
- Recursive step: factorial(n) = n × factorial(n-1)
- Test case: factorial(5) = 120

### 5. **05_fibonacci_recursive.py** - Recursive Fibonacci (nth term)
**Concept:** Recursion (base case, recursive step)
- Calculates nth Fibonacci number recursively
- Base cases: fibonacci(0) = 0, fibonacci(1) = 1
- Recursive step: fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)
- Test case: fibonacci(7) = 13

### 6. **06_reverse_string_recursive.py** - Recursive string reversal
**Concept:** Recursion (base case, recursive step)
- Reverses string using recursion
- Base case: string length ≤ 1 returns itself
- Recursive step: reverse_string(s) = reverse_string(s[1:]) + s[0]
- Test case: "hello" → "olleh"

### 7. **07_dictionary_basics.py** - Dictionary basics: create, access, update, delete a student record
**Concept:** Dictionaries (creation, access, update, deletion)
- Demonstrates creating dictionary with student information
- Shows accessing values using keys
- Covers updating existing values
- Illustrates adding new key-value pairs
- Shows deleting key-value pairs with del
- Includes key existence checks

### 8. **08_word_frequency.py** - Count word frequencies in a sentence using a dictionary
**Concept:** Dictionaries (creation, access, update) + Loops
- Counts occurrences of each word in a sentence
- Handles case insensitivity and basic punctuation
- Uses dictionary to store word → frequency mappings
- Test case: "test test demo" → {'test': 2, 'demo': 1}

### 9. **09_nested_dict_inventory.py** - Nest dictionaries: inventory of products with price and stock
**Concept:** Dictionaries (nesting, access, update)
- Creates nested dictionary structure for product inventory
- Each product contains price, stock, and category information
- Demonstrates accessing nested values
- Shows updating inventory after sales
- Illustrates adding new products to inventory
- Calculates total inventory value

### 10. **10_dict_loop_threshold.py** - Loop over dictionary to find keys with values above threshold
**Concept:** Dictionaries (access, iteration) + Loops
- Iterates through dictionary to find keys meeting condition
- Returns list of keys where values exceed specified threshold
- Includes both traditional loop and list comprehension approaches
- Test case: Find students with scores > 80

## How to Run

Each program is a standalone Python file. To run any program:

```bash
python programs/01_print_numbers.py
```

Replace `01_print_numbers.py` with the program number you want to run.

To run all programs sequentially:
```bash
for i in {01..10}; do
    echo "Running program $i:"
    python programs/${i}_*.py
    echo "---"
done
```

## Requirements

- Python 3.8+

## Learning Objectives

By completing these exercises, you will:
- Master basic loop constructs (for and while loops)
- Understand nested loops for pattern generation
- Learn recursion with base cases and recursive steps
- Practice dictionary operations and nested dictionary structures
- Develop problem-solving skills through practical coding exercises
- Learn to combine multiple concepts (loops + dictionaries, recursion + strings)

## Author

Created for beginner Python learners to build foundational programming skills.