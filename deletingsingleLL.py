# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Singly Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Function to add elements at the end
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:               # If the list is empty
            self.head = new_node
            return
        temp = self.head
        while temp.next:                    # Move to last node
            temp = temp.next
        temp.next = new_node                # Insert new node at end

    # Function to delete from beginning
    def delete_from_beginning(self):
        if self.head is None:
            print("List is empty!")
            return
        self.head = self.head.next          # Move head to next node
        print("Node deleted from beginning.")

    # Function to delete from end
    def delete_from_end(self):
        if self.head is None:
            print("List is empty!")
            return

        if self.head.next is None:          # If only one node
            self.head = None
            print("Last node deleted.")
            return

        temp = self.head
        while temp.next.next:               # Stop at second last node
            temp = temp.next
        temp.next = None
        print("Node deleted from end.")

    # Function to display the linked list
    def display(self):
        if self.head is None:
            print("List is empty!")
            return

        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


# --- Testing the Linked List ---
ll = LinkedList()
ll.insert(10)
ll.insert(20)
ll.insert(30)
ll.insert(40)

print("Original List:")
ll.display()

ll.delete_from_beginning()
print("After deleting from beginning:")
ll.display()

ll.delete_from_end()
print("After deleting from end:")
ll.display()