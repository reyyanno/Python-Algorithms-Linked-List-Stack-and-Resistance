# simple singly linked list

# node class to store a number and the next node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# linked list class
class LinkedList:
    def __init__(self):
        self.head = None

    # add a new item at the beginning
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    # remove and return the first item
    def pop(self):
        if self.head is None:
            return None
        removed = self.head.value
        self.head = self.head.next
        return removed

    # show the first item (no remove)
    def top(self):
        if self.head is None:
            return None
        return self.head.value

    # count number of items in the list
    def length(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    # check if the list is empty
    def is_empty(self):
        return self.head is None

    # check if a value exists
    def find(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            current = current.next
        return False

    # remove a specific value from the list
    def remove(self, value):
        current = self.head
        previous = None
        while current is not None:
            if current.value == value:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next
                return True
            previous = current
            current = current.next
        return False

# create the list
my_list = LinkedList()

# read numbers from file and add to the list
with open("integers.txt", "r") as file:
    for line in file:
        number = int(line.strip())
        my_list.push(number)

# test examples
print("list length:", my_list.length())
print("top element:", my_list.top())
print("is 100 in the list?", my_list.find(100))
print("remove 100:", my_list.remove(100))
print("is the list empty?", my_list.is_empty())
