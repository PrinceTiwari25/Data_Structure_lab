class Queue:
    def __init__(self):
        self.queue = []

    # Insert element at the rear
    def insert_rear(self, item):
        self.queue.append(item)
        print(f"Inserted {item} at rear.")

    # Insert element at the front
    def insert_front(self, item):
        self.queue.insert(0, item)
        print(f"Inserted {item} at front.")

    # Delete element from the front
    def delete_front(self):
        if not self.queue:
            print("Queue is empty. Cannot delete from front.")
        else:
            item = self.queue.pop(0)
            print(f"Deleted {item} from front.")

    # Delete element from the rear
    def delete_rear(self):
        if not self.queue:
            print("Queue is empty. Cannot delete from rear.")
        else:
            item = self.queue.pop()
            print(f"Deleted {item} from rear.")

    # Display queue
    def display(self):
        if not self.queue:
            print("Queue is empty.")
        else:
            print("Queue:", self.queue)


# Example usage
q = Queue()
q.insert_rear(10)
q.insert_rear(20)
q.insert_front(5)
q.insert_front(2)
q.display()

q.delete_front()
q.display()

q.delete_rear()
q.display()
