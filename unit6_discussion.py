"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================

INSTRUCTIONS:
In this activity, you will work with Python dictionaries
to simulate the behavior of a hash table.

You will modify the provided starter code to demonstrate
common operations and explain key concepts.

Follow all TODO prompts in the code and ensure your output
clearly communicates what your program is doing at each step.

----------------------------------------------------
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # TODO (Student): CREATE A HASH TABLE
    # ===============================
    #
    # Requirements:
    # 1. Create an empty dictionary.
    # 2. Add at least 5 key-value pairs.
    # 3. Add comments explaining how a dictionary
    #    behaves like a hash table.
    # 4. Display the contents of the dictionary.

    # Create empty dictionary.
    student_grades = {}

    # Add at least 5 key value pairs.
    student_grades["Aleshia"] = 92
    student_grades["Brian"] = 85
    student_grades["Celine"] = 78
    student_grades["Darian"] = 96
    student_grades["Eli"] = 88

    print("\n=== INSERT OPERATIONS ===")
    print("Dictionary after inserting key-value pairs:")
    print(student_grades)
    print("TODO: Create a dictionary and add multiple key-value pairs.")

    # ===============================
    # TODO (Student): LOOKUP OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Retrieve at least two existing keys.
    # 2. Clearly display the lookup results.
    # 3. Add meaningful comments to explain how the lookup works.

    # Look up key allows python to use its hash value.

    print("\n=== LOOKUP OPERATIONS ===")

    alice_grade = student_grades["Aleshia"]
    charlie_grade = student_grades["Celine"]

    print("Aleshia's grade:", alice_grade)
    print("Celine's grade:", charlie_grade)
    print("TODO: Demonstrate successful key lookups.")

    # ===============================
    # TODO (Student): UPDATE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Update the value associated with an existing key.
    # 2. Display the dictionary before and after the update.
    # 3. Use comments to explain what happens when an existing key is assigned
    #    a new value.

    print("\n=== UPDATE OPERATIONS ===")
    print("TODO: Demonstrate updating an existing key.")
    print("Before updating Brian's grade:")
    print(student_grades)

    # Assign new value to existing key updates its value.
    # Key "Brian" remains in dictionary, but the grade changes.
    student_grades["Brian"]= 90

    print("After updating Brian's grade:")
    print(student_grades)

    # ===============================
    # TODO (Student): DELETE OPERATIONS
    # ===============================
    #
    # Requirements:
    # 1. Delete at least one key-value pair.
    # 2. Display the dictionary before and after deletion.
    # 3. Use comments to explain what happens when a key is removed.

    print("\n=== DELETE OPERATIONS ===")
    print("TODO: Demonstrate deleting a key-value pair.")
    print("Before deleting Darian's grade:")
    print(student_grades)

    # Pop() method removes key-value pair for "Darian".
    # Associated value returned by pop().

    removed_grade = student_grades.pop("Darian")

    print("Removed Darian's grade:", removed_grade)
    print("After deleting Darian:")
    print(student_grades)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Lookup a missing key
    # - Delete a missing key safely
    # - Update a missing key
    # - Use an empty dictionary
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASES ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge case 1: Looking up a missing key.
    missing_grade = student_grades.get("Fran")

    if missing_grade is None:
        print("Fran was not found in the dictionary.")
    else:
        print("Fran's grade:", missing_grade)

    # Edge case 2: Deleting a missing key safely.
    removed_value = student_grades.pop("George", None)

    if removed_value is None:
        print("George was not found, so nothing was deleted.")

    # Edge case 3: Adding a new key with an update operation.
    student_grades["Fran"] = 75
    print("Fran was added with a grade of", student_grades["Fran"])

    print("\nFinal Dictonary:")
    print(student_grades)

if __name__ == "__main__":
    main()
    