"""
===========================================================
UNIT 7 DISCUSSION: SORTING ALGORITHMS (BUBBLE SORT VS MERGE SORT)
===========================================================

STUDENT INSTRUCTIONS:

This project explores two fundamental sorting algorithms:
- Bubble Sort (iterative, comparison-based)
- Merge Sort (recursive, divide-and-conquer)

Your goal is to demonstrate both your coding ability and your
understanding of algorithm efficiency and behavior.
"""


def bubble_sort(lst):
    """
    TODO (Student):
    Implement Bubble Sort.

    Requirements:
    - Create a copy of the original list.
    - Compare adjacent elements.
    - Swap elements when they are out of order.
    - Continue until the list is sorted.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # Create a copy of the original list
    sorted_list = lst.copy()

    # Continue making passes through the list
    for pass_num in range(len(sorted_list) - 1):
        swapped = False

        # Compare adjacent elements
        for index in range(len(sorted_list) - 1 - pass_num):
            if sorted_list[index] > sorted_list[index + 1]:
                sorted_list[index], sorted_list[index + 1] = (sorted_list[index + 1], sorted_list[index],)
                swapped = True

        # Stop early if no swaps occurred.
        if not swapped:
            break

    return sorted_list

def merge_sort(lst):
    """
    TODO (Student):
    Implement Merge Sort.

    Requirements:
    - Use recursion.
    - Divide the list into smaller halves.
    - Sort each half recursively.
    - Merge the sorted halves together.
    - Return the sorted list.
    - Add meaningful comments.

    """
    # Lists with zero or one item are already sorted
    if len(lst) <= 1:
        return lst.copy()

    # Find the middle index
    middle = len(lst) // 2

    # Divide teh list into two halves
    left_half = lst[:middle]
    right_half = lst[middle:]

    # Recursively sort each half
    sorted_left = merge_sort(left_half)
    sorted_right = merge_sort(right_half)

    # Merge the sorted halves
    return merge(sorted_left, sorted_right)


def merge(left, right):
    """
    TODO (Student):
    Implement the merge step used by Merge Sort.

    Requirements:
    - Compare values from the left and right lists.
    - Build a new sorted result list.
    - Append any remaining values.
    - Return the merged sorted list.
    - Add meaningful comments.
    """
    result = []

    left_index = 0
    right_index = 0

    # Compare values from both lists
    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    # Add any remaining values from the left list
    result.extend(left[left_index:])

    # Add any remaining values from the right list
    result.extend(right[right_index:])

    return result

def main():
    print("=== UNIT 7: SORTING ALGORITHMS ===")

    # ===============================
    # TODO (Student): DATASET #1
    # ===============================
    #
    # Requirements:
    # 1. Create an unsorted list containing at least 7 values.
    # 2. Display the original list.
    # 3. Sort the list using Bubble Sort.
    # 4. Sort the same list using Merge Sort.
    # 5. Clearly label and display all results.

    dataset_1 = [64, 25, 12, 22, 11, 90, 34]

    print("\n=== DATASET #1 ===")
    print("Original list:", dataset_1)
    print("TODO: Create an unsorted dataset and test both sorting algorithms.")

    bubble_result_1 = bubble_sort(dataset_1)
    merge_result_1 = merge_sort(dataset_1)

    print("Bubble sort result:", bubble_result_1)
    print("Merge sort result:", merge_result_1)
    print("Results match:", bubble_result_1 == merge_result_1)

    # ===============================
    # TODO (Student): DATASET #2
    # ===============================
    #
    # Requirements:
    # 1. Create a second dataset.
    # 2. Use different values than Dataset #1.
    # 3. Sort using both algorithms.
    # 4. Compare the results.

    dataset_2 = [5, 3, 8, 3, 9, 1, 7, 2]

    print("\n=== DATASET #2 ===")
    print("Original list:", dataset_2)
    print("TODO: Create a second dataset and compare sorting results.")

    bubble_result_2 = bubble_sort(dataset_2)
    merge_result_2 = merge_sort(dataset_2)

    print("Bubble sort result:", bubble_result_2)
    print("Merge sort result:", merge_result_2)
    print("Results match:", bubble_result_2 == merge_result_2)

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least two edge cases.
    #
    # Example ideas:
    # - Empty list
    # - Already sorted list
    # - Reverse-sorted list
    # - List with duplicate values
    # - Single-element list
    #
    # Explain what happens in each case.

    print("\n=== EDGE CASE TESTS ===")
    print("TODO: Demonstrate and explain edge cases.")

    # Edge case 1: Empty list
    empty_list =[]
    print("\nEmpty list:")
    print("Original:", empty_list)
    print("Bubble sort:", bubble_sort(empty_list))
    print("Merge sort:", merge_sort(empty_list))
    print("An empty ;ist is already sorted.")

    # Edge case 2: Already sorted list
    sorted_list = [1, 2, 3, 4, 5]
    print("\nAlready sorted list:")
    print("Original:", sorted_list)
    print("Bubble sort:", bubble_sort(sorted_list))
    print("Merge sort:", merge_sort(sorted_list))
    print("The algorithms leave the values in sorted order.")

    # Edge case 3: Duplicate values
    duplicate_list = [4, 2, 4, 1, 2]
    print("\nList with duplicate values:")
    print("Original:", duplicate_list)
    print("Bubble sort:", bubble_sort(duplicate_list))
    print("Merge sort:", merge_sort(duplicate_list))
    print("Duplicate values are preserved and sorted correctly.")

    # Confirm the original lists were not changed.
    print("\nOriginal Dataset #1 after sorting:", dataset_1)
    print("Original Dataset #2 after sorting:", dataset_2)


if __name__ == "__main__":
    main()