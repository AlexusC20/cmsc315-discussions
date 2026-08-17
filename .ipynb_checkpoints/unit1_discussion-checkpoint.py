"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    def __init__(self, name, is_done=False):
        # instance variables (at least two)
        self.name= name
        self.is_done= is_done

    def display_info(self):
        status = "Done" if self.is_done else "Not done"
        info = f"[{ParentClass.category}] {self.name} - {status}"
        print(info)
        return info


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    # New class variable
    priority_levels = ["Low", "Medium", "Hight"]

    def __init__(self, name, is_done=False, due_date=None, priority="Medium"):
    # New instance variable
    super().__init__(name, is_done)

    self.due_date = due_date
    self.priority = priority

    def mark_done(self):
        # new method
        self.is_done = True

    def display_info(self):
        # Override parent's method
        status = "Done" if self.is_done else "Not done"
        info = f"[{self.priority}] {self.name} (due: {self.due_date}) - {status}"
        print(info)
        return info


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")
    # Create at least two objects of the child class
    obj1 = ChildClass("Buy milk", is_done=False, due_date="2026-08-20", priority="High")
    obj2 = ChildClass("Read book", is_done=True, due_date="2026-08-25", priority="Low")

    # Access class variable through the class itself
    print("Class access (ChildClass.priority_levels):", ChildClass.priority_levels)

    # Access the same class variable through an object
    print("Object access (obj1.priority_levels):", obj1.priority_levels)

    # Add a new attribute to only one object after it is created
    obj1.extra_note = "Remember to check discounts."

    # Display each object's namespace using __dict__
    print("\nobj1 __dict__:", obj1.__dict__)
    print("obj2 __dict__:", obj2.__dict__)

    # Display information about the class namespace
    print("\nChildClass __dict__ (class namespace):")
    print(ChildClass.__dict__)
    print("TODO: Implement namespace demonstration")


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")
    # Original object with nested mutable data
    original = {
        "title": "My Todo",
        "tags": ["work", "urgent"],
        "meta": {"priority": "High"}
    }

    # Shallow copy: creates a new top-level dict,
    # but nested objects (like lists/dicts inside) are shared by reference.
    shallow = copy.copy(original)

    # Deep copy: creates a new top-level dict AND recursively copies nested objects,
    # so nothing is shared by reference.
    deep = copy.deepcopy(original)

    print("Before modification:")
    print("Original:", original)
    print("Shallow copy:", shallow)
    print("Deep copy:", deep)

    # Modify the original object's nested data
    original["tags"].append("today")
    original["meta"]["priority"] = "Low"

    print("\nAfter modifying original nested data:")
    print("Original:", original)
    print("Shallow copy:", shallow)
    print("Deep copy:", deep)

    print("\nExplanation:")
    print("- Shallow copy shares nested references with the original, so it changes when original's nested data changes.")
    print("- Deep copy does not share nested references, so it stays unchanged when original's nested data changes.")
    print("TODO: Implement shallow copy and deep copy demonstration")


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")
    print("\nTODO: Create and test your parent object")
    parent_obj = ParentClass("Parent todo", is_done=False)
    parent_obj.display_info()  # demonstrates parent method usage

    print("\nTODO: Create and test your child object")
    child_obj = ChildClass("Child todo", is_done=False, due_date="2026-08-20", priority="High")
    child_obj.display_info()  # overridden method (child version)
    child_obj.mark_done()     # new child method
    child_obj.display_info()  # show updated status after inheritance

    demonstrate_namespaces()
    demonstrate_copying()


    print("\nTODO: Create and test your parent object")

    print("\nTODO: Create and test your child object")



if __name__ == "__main__":
    main()