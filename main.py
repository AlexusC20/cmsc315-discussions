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

class ChildClass(ParentClass):
    # New class variable
    priority_levels = ["Low", "Medium", "High"]

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

# demonstration of the classes
if __name__ == "__main__":
    main() 
def main():
    # Create an instance of the parent class
    parent_instance = ParentClass("Parent Task", is_done=False)
    parent_instance.display_info()

    # Create an instance of the child class
    child_instance = ChildClass("Child Task", is_done=False, due_date="2026-08-20", priority="High")
    child_instance.display_info()

    # Mark the child task as done and display info again
    child_instance.mark_done()
    child_instance.display_info()

