class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begin(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            print(f"insert at begin {newNode.data}")
            return
        # print("adding element here")
        newNode.next = self.head
        self.head = newNode
        print(f"insert at begin {newNode.data}")

    def insert_at_end(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            print(f"inserted at end{newNode.data}")
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = newNode
        print(f"inserted at end{itr.next.data}")
        # print("inserted at end")

    def Count(self):
        count = 0
        itr = self.head
        while itr is not None:
            count += 1
            itr = itr.next
        return count

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head
        string = ""
        while itr is not None:
            string += f"{itr.data}" + "--->"
            itr = itr.next
        string += "None"
        print(string)

    def insert_at(self, index, data):
        # newNode = Node(data)
        if index < 0 or index > self.Count() - 1:
            print("index out of range")
            return
        if index == 0:
            self.insert_at_begin(data)
        # if index == self.Count() - 1:
            # self.insert_at_end(data)
        itr = self.head
        counter = 0
        while itr:
            if counter == index -1 :
                itr.next = Node(data, itr.next) 

                return
            counter += 1
            itr = itr.next
        print(f"inserted {itr.next.data} at {index}")

    def current_Head_position(self):
        print(f"head is at {self.head.data}")
    def remove_at(self , index):
        if self.head is None:
            print("list  is empty")
            return
        if index <0 or index > self.Count() - 1:
            print("index out of range")
            return
        if index ==0:
            self.head = self.head.next
        itr = self.head
        counter = 0
        while itr:
            if counter == index -1:
                print(f"removed {itr.next.data}")
                itr.next = itr.next.next
                return
            counter +=1
            itr = itr.next
        return
    def remove(self, data):
        tester = self.head.next
        replacer = self.head
        if replacer.data == data:
            self.remove_at(0)
            return
        # counter = 0
        while tester:
            if tester.data == data:
                replacer.next = replacer.next.next
                return

            tester= tester.next  
            replacer = replacer.next

        print("no such value exists")
        return
        

l1 = LinkedList()
l1.print()
l1.insert_at_begin(15)
l1.print()
l1.insert_at_begin(34)
l1.print()
l1.insert_at_end(13)
l1.print()
l1.insert_at(2, "hello")
l1.print()
l1.insert_at(2, "new")
l1.print()
# l1.remove_at(2)
l1.remove(34)
l1.print() 
# l1.current_Head_position()
l1.remove("new")
l1.print() 
l1.remove("aas")
# l1.print() 
# print(l1.Count())
# l1.current_Head_position()
