# Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# Singly Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at the beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at the end
    def insert_at_end(self, data):
        new_node = Node(data)
        new_node.next = None

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next

        temp.next = new_node

    # Display linked list
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

    # Search for a value in the linked list
    def search(self, key):
        temp = self.head
        while temp:
            if temp.data == key:
                print(f"{key} Found in the list.")
                return True
            temp = temp.next
        print(f"{key} Not Found in the list.")
        return False


# Example usage
if __name__ == "__main__":
    ll = LinkedList()

    # Inserting nodes
    ll.insert_at_beginning(10)
    ll.insert_at_beginning(20)
    ll.insert_at_end(30)
    ll.insert_at_end(40)

    # Displaying the linked list
    print("Linked List Elements:")
    ll.display()

    # Searching for elements
    ll.search(30)   # Found
    ll.search(50)   # Not Found