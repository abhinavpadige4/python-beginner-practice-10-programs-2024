"""
Program 7: Dictionary basics – create, access, update, delete a student record
Concept: Dictionaries (creation, access, update, deletion)
"""

def demonstrate_dictionary_basics():
    """Demonstrate basic dictionary operations with a student record."""
    
    # Create a student dictionary
    student = {
        "name": "Alice Johnson",
        "age": 20,
        "major": "Computer Science",
        "gpa": 3.8,
        "year": "Sophomore"
    }
    
    print("Initial student record:")
    print(student)
    print()
    
    # Access values
    print("Accessing values:")
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"GPA: {student['gpa']}")
    print()
    
    # Update values
    print("Updating values:")
    student["gpa"] = 3.9  # Update GPA
    student["year"] = "Junior"  # Update year
    print(f"After updates: {student}")
    print()
    
    # Add new key-value pair
    print("Adding new key-value pair:")
    student["email"] = "alice.johnson@email.com"
    print(f"After adding email: {student}")
    print()
    
    # Delete a key-value pair
    print("Deleting key-value pair:")
    del student["age"]  # Remove age
    print(f"After deleting age: {student}")
    print()
    
    # Check if key exists
    print("Checking key existence:")
    print(f"Has 'major' key: {'major' in student}")
    print(f"Has 'age' key: {'age' in student}")
    print()
    
    # Get all keys and values
    print("All keys:", list(student.keys()))
    print("All values:", list(student.values()))
    print("All items:", list(student.items()))

if __name__ == "__main__":
    demonstrate_dictionary_basics()