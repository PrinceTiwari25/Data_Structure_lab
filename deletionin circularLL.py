class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    # Function to insert nodes at the end
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.head.next = self.head  # Point to itself
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    # Function to display the list
    def display(self):
        if self.head is None:
            print("List is empty")
            return
        temp = self.head
        print("Circular Linked List:", end=" ")
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print("(back to head)")

    # Function to delete node from beginning
    def delete_begin(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return

        temp = self.head

        # If there is only one node
        if self.head.next == self.head:
            self.head = None
            print("Deleted the only node in the list.")
            return

        # Move to the last node
        last = self.head
        while last.next != self.head:
            last = last.next

        # Point last node to next of head
        last.next = self.head.next
        self.head = self.head.next
        print("Node deleted from beginning.")

    # Function to delete node from end
    def delete_end(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return

        # If only one node
        if self.head.next == self.head:
            self.head = None
            print("Deleted the only node in the list.")
            return

        # Traverse to second last node
        prev = None
        temp = self.head
        while temp.next != self.head:
            prev = temp
            temp = temp.next

        # 'temp' is last node; 'prev' is second last
        prev.next = self.head
        print("Node deleted from end.")


# ---------------------------
# Main Program Execution
# ---------------------------
cll = CircularLinkedList()

# Insert elements
cll.insert(10)
cll.insert(20)
cll.insert(30)
cll.insert(40)

print("Initial List:")
cll.display()

# Delete from beginning
cll.delete_begin()
cll.display()

# Delete from end
cll.delete_end()
cll.display()
