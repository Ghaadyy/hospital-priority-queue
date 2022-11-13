class Node:
    def __init__(self, name, priority):
        # Intializes the properties needed for the patient.
        self.name = name
        self.priority = priority
        self.next = None

    def __str__(self):
        # Allows the object to have a string representation when we print it.
        return f"Patient: {self.name} Priority: {self.priority}"


class PriorityQueue:
    def __init__(self):
        self.head = None
        self.queue = None

    # Checks if the queue is empty, If there no head property means it is empty.
    def isEmpty(self):
        return self.head == None

    def push(self, item, priority):
        # Creates the new Patient Node.
        newNode = Node(item, priority)

        if not self.queue:
            self.head = newNode
            self.queue = newNode
            return

        if self.head.priority == newNode.priority:
            temp = self.head.next
            self.head.next = newNode
            newNode.next = temp
            return

        if self.head.priority < newNode.priority:
            newNode.next = self.head
            self.head = newNode
            return

        previous = None
        current = self.head

        while ((current is not None) and newNode.priority < current.priority):
            previous = current
            current = current.next

        if current is not None:
            previous.next = newNode
            newNode.next = current
        else:
            self.queue.next = newNode
            self.queue = newNode

    def pop(self):
        # Checks if the queue is empty and stops the pop() action.
        if self.isEmpty():
            print('Queue is empty')
            return
        # We save the data we want to remove to return the processed patient.
        temp = self.head
        # We set the new head to the next patient in queue.
        self.head = self.head.next
        if self.head == None:
            # If the head of the queue is none we should set the last element i.e. the self.queue to None.
            self.queue = None
        return temp.name  # We return the processed patient's name.

    def peek(self):
        # We return the patient's name that is next in queue.
        return self.head

    def printQueue(self):
        # Prints the Patient Queue in a special format.
        current = self.head
        print("=================================\n")
        print(current)
        while current.next is not None:
            current = current.next
            print(current)
        print("\n=================================")


"""
Here is the main program that prints out the patients
and allows the user to add / process patients depending
on their priority.
"""

print("=================================\n")
print("Welcome to the ER Check-In System")
print("Please note that patients are processed from highest to lowest priority.")
print("\n=================================")

choice = ""
patientQueue = PriorityQueue()  # We create the patient queue.

while choice != 'q':
    if patientQueue.isEmpty():
        print("\nPatient queue is empty.")
    else:
        patientQueue.printQueue()

    choice = str(
        input("(N) New Patient\n(P) Process patient\n(Q) Quit\nChoice: "))
    choice = choice.lower()

    if choice == 'n':
        name = str(input("Name? "))
        priority = int(input("Priority? "))
        patientQueue.push(name, priority)  # We add the patient to the queue.

    elif choice == 'p':
        patientQueue.pop()  # We remove the patient from the queue.

    print("")
