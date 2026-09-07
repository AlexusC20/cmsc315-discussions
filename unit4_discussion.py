"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        self.value = value

        # to the left and right child nodes.
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.
        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """
        if node is None:
            return Node(value)

        # Smaller values into the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(node.left, value)

        # Larger values into the right subtree.
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """
        # None means the value is not in the tree.
        if node is None:
            return False

        # The value has been found.
        if value == node.value:
            return True

        # Search left for smaller values.
        if value < node.value:
            return self._search_recursive(node.left, value)

        # Search right for larger values.
        if value > node.value:
            return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """
        values = []
        self._inorder_recursive(self.root, values)
        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """
        if node is None:
            return

        # Visit the left subtree.
        self._inorder_recursive(node.left, values)

        # Visit the current node.
        values.append(node.value)

        #  # Visit the right subtree last.
        self._inorder_recursive(node.right, values)

def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")
    tree = BST()
    inserted_values = [50, 30, 70, 20, 40, 60, 80]

    for value in inserted_values:
        tree.insert(value)
    print("Values inserted:", inserted_values)
    print("TODO: Create a BST and insert multiple values.")

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    sorted_values = tree.inorder()
    print("In-order traversal:", sorted_values)

    print("TODO: Display and explain traversal results.")

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")
    existing_values = [40, 80]
    missing_values = [25, 90]

    for value in existing_values:
        print(f"Search for value {value}: {tree.search(value)}")
    # These values exist in the tree, so search returns True.

    for value in missing_values:
        print(f"Search for value {value}: {tree.search(value)}")
    # These values do not exist in the tree, so search returns False.
    print("TODO: Demonstrate BST searching.")

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")
    empty_tree = BST()

    # Search an empty tree.
    print("Search empty tree for 10:", empty_tree.search(10))

    # Traverse an empty tree.
    print("In-order traversal of empty tree:", empty_tree.inorder())

    # Insert duplicate values.
    tree.insert(50)
    print("After inserting duplicate 50:", tree.inorder())
    print("TODO: Demonstrate and explain an edge case.")



if __name__ == "__main__":
    main()
