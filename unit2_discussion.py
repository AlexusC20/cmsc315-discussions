"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

You will complete, modify, and extend the starter code while
explaining key concepts through comments and improved output.
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        self.items = []
        # Hint: A Python list can be used to store stack values.

    def push(self, value):
        # TODO (Student): Add value to the stack.
        self.items.append(value)
        # Add a short comment explaining why this operation supports LIFO behavior.
        pass

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        if self.is_empty():
            return None
        return self.items.pop()
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?


    def peek(self):
        # TODO (Student): Return the top value without removing it.
        if self.is_empty():
            return None
        return self.items[-1]
        # Add a comment explaining what peek does.


    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        self.items = deque()
        # Hint: collections.deque is useful for efficient queue operations.
        pass

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        self.items.append(value)
        # Add a short comment explaining why this operation supports FIFO behavior.
        pass

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        if self.is_empty():
            return None
        return self.items.popleft()
        # Explain or improve empty-queue handling.


    def front(self):
        # TODO (Student): Return the front value without removing it.
        if self.is_empty():
            return None
        return self.items[0]
        # Add a comment explaining what front returns.

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0

def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.


print("\n=== STACK DEMO ===")

stack = Stack()

#Demonstrate LIFO behavior
stack.push("First")
stack.push("Second")
stack.push("Third")

print("Popping:", stack.pop()) #Third
print("Popping:", stack.pop()) #Second
print("Popping:", stack.pop()) #First

print("TODO: Create a Stack object, demonstrate LIFO behavior,")

# Test popping from empty stack
print("Popping from an empty stack", stack.pop()) #None

# Test peeking at an empty stack
print("Peeking at an empty stack", stack.peek()) #None

# Verify a single-item stack becomes empty after removal.
stack.push("Only item")
print("Stack before removal:", stack.is_empty()) #False

stack.pop()

print("Stack after removal:", stack.is_empty()) #True

# ===============================
# TODO (Student): QUEUE DEMO
# ===============================
# Requirements:
# 1. Create a Queue object.
# 2. Add at least 4 values to the queue.
# 3. Improve the print statements so they clearly explain what is happening.
# 4. Demonstrate FIFO behavior.
# 5. Show what happens when dequeue() is used on an empty queue.
#
# Edge Cases:
# 6. Show what happens when front() is used on an empty queue.
# 7. Create a queue with only one item, remove it,
#    and verify the queue is empty afterward.

print("\n=== QUEUE DEMO ===")

queue = Queue()

# Demonstrate FIFO behavior
queue.enqueue("First")
queue.enqueue("Second")
queue.enqueue("Third")

print("Dequeuing:", queue.dequeue()) # First
print("Dequeuing:", queue.dequeue()) # Second
print("Dequeuing:", queue.dequeue()) # Third

print("TODO: Create a Queue object, demonstrate FIFO behavior,")

# Test dequeuing from an empty queue
print("Dequeuing from an empty queue:", queue.dequeue()) # None

# Test viewing the front of an empty queue
print("Viewing front of empty queue:", queue.front())

# Verify a single-item queue becomes empty after removal
queue.enqueue("Only item")
print("Queue before removal:", queue.is_empty()) # False

queue.dequeue()

print("Queue after removal:", queue.is_empty()) # True

if __name__ == "__main__":
    main()
