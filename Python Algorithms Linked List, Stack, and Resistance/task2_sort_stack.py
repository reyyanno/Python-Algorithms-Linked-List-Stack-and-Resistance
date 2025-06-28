# sorting a stack using another temporary stack

class Stack:
    def __init__(self):
        self.items = []

    # add item to top
    def push(self, item):
        self.items.append(item)

    # remove and return top item
    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    # return top item without removing
    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    # check if stack is empty
    def is_empty(self):
        return len(self.items) == 0

    # size of the stack
    def size(self):
        return len(self.items)

    # print the stack for testing
    def print_stack(self):
        print("stack (top to bottom):")
        for item in reversed(self.items):
            print(item)

# sort elements using one temporary stack
def sort_stack(original_stack):
    temp_stack = Stack()

    while not original_stack.is_empty():
        current = original_stack.pop()

        # move bigger items back to original stack
        while not temp_stack.is_empty() and temp_stack.peek() > current:
            original_stack.push(temp_stack.pop())

        temp_stack.push(current)

    return temp_stack

# test with example values
if __name__ == "__main__":
    s = Stack()

    # add some values to the stack
    values = [5, 1, 4, 2, 3]
    for v in values:
        s.push(v)

    print("before sorting:")
    s.print_stack()

    sorted_stack = sort_stack(s)

    print("\nafter sorting:")
    sorted_stack.print_stack()
