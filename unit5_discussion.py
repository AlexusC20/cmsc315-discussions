"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

INSTRUCTIONS:
In this assignment, you will implement and analyze two
fundamental search algorithms: linear search and binary search.

You will demonstrate your understanding by modifying the
provided code, running experiments on different dataset sizes,
and clearly explaining your results through code comments
and program output.
"""


def linear_search(lst, target):
    """
    TODO (Student):
    Implement a linear search algorithm.

    Requirements:
    - Search the list from beginning to end.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining why linear search
      has O(n) time complexity.
    """
    for index in range(len(lst)):
        if lst[index] == target:
            return index

    return -1

def binary_search(lst, target):
    """
    TODO (Student):
    Implement a binary search algorithm.

    Requirements:
    - Assume the list is already sorted.
    - Repeatedly reduce the search space by half.
    - Return the index if the target is found.
    - Return -1 if the target is not found.
    - Add comments explaining how each iteration
      reduces the search space.
    """
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif target < lst[mid]:
            right = mid - 1
        else:
            left = mid + 1
    return -1

def main():
    print("The program is running.")
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # TODO (Student): SMALL DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a small sorted dataset.
    # 2. Test both linear search and binary search.
    # 3. Search for:
    #    - a value that exists
    #    - a value that does not exist
    # 4. Use comments to clearly explain the results.

    print("\n=== SMALL DATASET TEST ===")

    # List is sorted as required for binary search.
    small_data = [3, 7, 12, 18, 25, 31, 42]

    existing_value = 18
    missing_value = 20

    print("Dataset: ", small_data)

    # Both algorithms should find 18 at index 3.
    linear_result = linear_search(small_data, existing_value)
    binary_result = binary_search(small_data, existing_value)

    print(f"\nSearching for {existing_value}:")
    print("Linear search index: ", linear_result)
    print("Binary search index: ", binary_result)

    # Both algorithms should return -1 because 20 is not in the list.
    linear_result = linear_search(small_data, missing_value)
    binary_result = binary_search(small_data, missing_value)

    print(f"\nSearching for {missing_value}:")
    print("Linear search index: ", linear_result)
    print("Binary search index: ", binary_result)

    # ===============================
    # TODO (Student): LARGE DATASET
    # ===============================
    #
    # Requirements:
    # 1. Create a much larger sorted dataset.
    # 2. Test both search algorithms.
    # 3. Compare the results.
    # 4. Use comments to explain why binary search becomes more
    #    efficient as datasets grow larger.

    print("\n=== LARGE DATASET TEST ===")

    # Range creates a sorted list containing values from 0 to 999,999.
    large_data = list(range(1_000_000))

    existing_value = 987_654
    missing_value = 1_000_000

    print("Large dataset contains", len(large_data), "Values.")

    linear_result = linear_search(large_data, existing_value)
    binary_result = binary_search(large_data, existing_value)

    print(f"\nSearching for {existing_value}:")
    print("Linear search index: ", linear_result)
    print("Binary search index: ", binary_result)

    linear_result = linear_search(large_data, missing_value)
    binary_result = binary_search(large_data, missing_value)

    print(f"\nSearching for {missing_value}:")
    print("Linear search index: ", linear_result)
    print("Binary search index: ", binary_result)


    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Single-element list
    # - Value not present
    # - Value at the first position
    # - Value at the last position
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")

    # Edge case 1: Empty list.
    empty_list = []

    print("\nEmpty list:")
    print("Linear search:", linear_search(empty_list, 10))
    print("Binary search:", binary_search(empty_list, 10))

    # Edge case 2: single element list containing target.
    single_item_list = [50]

    print("\nSingle-element list containing the target: ")
    print("Linear search:", linear_search(single_item_list, 50))
    print("Binary search:", binary_search(single_item_list, 50))

    # Edge case 3: single-element list not containing the target.
    print("\nSingle-element list not containing the target: ")
    print("Linear search:", linear_search(single_item_list, 25))
    print("Binary search:", binary_search(single_item_list, 25))

    # Edge case 4: Searching for the first and last values.
    edge_list = [10, 20, 30, 40, 50]

    print("\nFirst value:")
    print("Linear search:", linear_search(edge_list, 10))
    print("Binary search:", binary_search(edge_list, 10))
    print("\nSecond value:")
    print("Linear search:", linear_search(edge_list, 50))
    print("Binary search:", binary_search(edge_list, 50))

if __name__ == "__main__":
    main()
