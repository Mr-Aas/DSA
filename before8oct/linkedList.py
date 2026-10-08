class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linkedList:
    def __init__(self):
        self.head = None

    def insert_at_beggining(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):

        itr = self.head

        string = ""
        while itr:
            string += f"{itr.data}" + "-->"
            itr = itr.next
        print(string)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_data(self, lot_data):
        self.head = None

        for data in lot_data:
            # self.head = Node(data, self.head)
            self.insert_at_end(data)

    def get_length(self):
        counter = 0

        itr = self.head
        while itr:
            counter += 1
            itr = itr.next
        return counter

    def remove_from(self, index):
        if index < 0 or index > self.get_length():
            raise IndexError("no element present at this index")
        if index == 0:
            self.head = self.head.next

        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break

            count += 1
            itr = itr.next

    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("not possible to insert here")
        if index == 0:
            self.insert_at_beggining(data)
        itr = self.head

        count = 0
        while itr:
            if count == index - 1:
                itr.next = Node(data, itr.next)
            count += 1
            itr = itr.next


ll = linkedList()
# ll.insert_at_beggining("first")
# ll.insert_at_beggining("second")
# ll.insert_at_end("third")
# ll.insert_at_beggining("forth")
# ll.print()
ll.insert_data(["dada", "abbu", "aasu", "ladla"])

ll.print()
print(ll.get_length())

ll.remove_from(0)
ll.print()
ll.remove_from(2)
ll.print()
# ll.remove_from(20)
ll.insert_at(2, "betta")
ll.print()
ll.insert_at(0, "asger")
ll.print()
# ll.insert_at(0, "asgar")
# ll.insert_at(5, "parpotta")
# ll.insert_at(1,"anas")

# ___________built without seeing__________


# class Node:
#     def __init__(self, data=None, Next=None):
#         self.data = data
#         self.next = Next


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def insert_at_end(self, data):
#         self.next = Node(data)

#     def __str__(self,data):
#         itr = ""
        
        
        


# newlink = LinkedList()
# newlink.insert_at_end(121)

# print(newlink)
