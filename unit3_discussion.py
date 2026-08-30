"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

INSTRUCTIONS:
This assignment focuses on understanding how lists behave when elements
are inserted, removed, and searched. You will analyze how Python lists
shift elements in memory and how different operations impact performance.
"""


def insert_at(lst, index, value):
    """
    TODO (Student):
    Insert a value into the list at the specified index.

    Requirements:
    - Use a list operation to insert the value.
    - Add comments explaining what happens to existing elements
      after an insertion occurs.
    - Use comments to explain how insertion performance may vary depending on
      where the insertion occurs.
    """

    # Insert the value at the required position.
    # Existing elements from that position onwards move one place to the right.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    TODO (Student):
    Remove and return the value at the specified index.

    Requirements:
    - Validate that the index exists.
    - Return the removed value.
    - Return None if the index is invalid.
    - Add comments explaining why index validation and safe deletion are important.
    """

    # Validate the index exists.
    # An IndexError when the requested position does not exist.
    if index < 0 or index >= len(lst):
        return None

    # Store value before removing it
    removed_value = lst[index]
    del lst[index]
    return removed_value

def search_value(lst, value):
    """
    TODO (Student):
    Search for a value within the list.

    Requirements:
    - Return the index if the value is found.
    - Return -1 if the value is not found.
    - Add comments explaining why this is a linear search and why it scans sequentially.
    """

    # This is a linear search because it checks items one at a time.
    # The list is scanned sequentially from the first element to the last.
    for index in range(len(lst)):
        if lst[index] == value:
            return index

    # Returning -1 indicates the value was not found
    return -1

def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # TODO (Student): INSERTION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Create a list containing several values.
    # 2. Display the original list.
    # 3. Test insertion at:
    #    - the beginning
    #    - the middle
    #    - the end
    # 4. Display the list after each insertion.
    # 5. Use comments to explain each step in the implementation.

    print("\n=== INSERTION TESTS ===")

    # Create a list containing several values.
    numbers = [10, 20, 30, 40]
    print("Original list: ", numbers)

    # Insert at the beginning of the list
    insert_at(numbers, 0, 5)
    print ("After inserting 5 at the beginning: ", numbers)

    # Insert in the middle of the list
    insert_at(numbers, 3, 25)
    print("After inserting 25 in the middle: ", numbers)

    # Insert at the end of the list
    insert_at(numbers, len(numbers), 50)
    print("After inserting 50 at the end: ", numbers)

    # ===============================
    # TODO (Student): DELETION TESTS
    # ===============================
    #
    # Requirements:
    # 1. Delete an item from:
    #    - the beginning
    #    - the middle
    #    - the end
    # 2. Display the removed value.
    # 3. Display the updated list after each deletion.
    # 4. Use comments to clearly explain what is happening in the output.

    print("\n=== DELETION TESTS ===")

    # Create a new list for deletion demonstrations.
    numbers = [10, 20, 30, 40, 50]
    print("Original list: ", numbers)

    # Delete the item at the beginning.
    removed = delete_at(numbers, 0)
    print("Removed value from the beginning: ", removed)
    print("Updated list: ", numbers)

    # Delete the item from the middle.
    removed = delete_at(numbers, 1)
    print("Removed value from the middle: ", removed)
    print("Updated list: ", numbers)

    # Delete the item from the end.
    removed = delete_at(numbers, len(numbers) -1)
    print("Removed value from the end: ", removed)
    print("Updated list: ", numbers)

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for a value that exists.
    # 2. Search for a value that does not exist.
    # 3. Display the search results with clear explanations.
    # 4. Use comments to explain each step.

    print("\n=== SEARCH TESTS ===")

    # Create a list to search.
    numbers = [10, 20, 30, 40, 50]
    print("List being searched: ", numbers)

    # Search for a value that exists
    result = search_value(numbers, 30)
    print("Searching for 30: found at index", result)

    # Search for a value that does not exist.
    result = search_value(numbers, 99)
    print("Searching for 99: returned", result, "because it was not found.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Delete using an invalid index
    # - Search for a missing value
    # - Insert into an empty list
    # - Delete from an empty list
    # - Use comments to explain each edge case.

    print("\n=== EDGE CASES ===")

    # Edge case 1: Attempt to delete using an invalid index.
    numbers = [10, 20, 30]
    removed = delete_at(numbers, 10)
    print("Attempted deletion at invalid index 10: ", removed)
    print("List remains unchanged: ", numbers)

    # Edge case 2: Search for a missing value.
    result = search_value(numbers, 100)
    print("Searching for missing value 100: ", result)

    # Edge case 3: Insert into an empty list.
    empty_list = []
    insert_at(empty_list, 0, 25)
    print("After inserting into an empty list: ", empty_list)

    # Edge case 4: Attempt to delete from an empty list.
    removed = delete_at(empty_list, 0)
    print("Removed value from the empty list: ", removed)
    print("List after deletion: ", empty_list)

if __name__ == "__main__":
    main()
