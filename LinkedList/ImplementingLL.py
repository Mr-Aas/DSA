class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        newNode = Node(data, None)
        if self.head is None:
            self.head = newNode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newNode

    def insert_at_beggining(self, data):
        newNode = Node(data, self.head)
        self.head = newNode

    def print(self):
        if self.head is None:
            print("linked list is empty")
            return
        itr = self.head
        lstr = ""
        while itr:
            lstr += str(itr.data) + "-->"
            itr = itr.next
        lstr += "None"
        print(lstr)

    def insertvalues(self, data):
        for item in data:
            self.insert_at_end(item)

    def Count(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        # print(count)
        return count

    def remove_at_index(self, index):
        if index >= self.Count() or index < 0:
            print("no such index exist")
            return
        if index == 0:
            self.head = self.head.next

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                print(f"{itr.next.data} has been removed ")
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index == 0:
            self.insert_at_beggining(data)
        if index < 0 or index > self.Count():
            print("invalid index")
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = Node(data,itr.next)
            itr =itr.next
            count+=1


l = LinkedList()
l.print()
l.insert_at_beggining(5)
l.print()
l.insert_at_beggining(15)
l.print()
l.insert_at_beggining(25)
l.print()
l.insert_at_end(45)
l.print()
l.insertvalues(["many", "years", "ago"])
l.print()
l.remove_at_index(10)
l.print()
l.remove_at_index(0)
l.print()
l.remove_at_index(4)
l.print()
l.insert_at(4,"centuries")
l.print()
# l.Count()
# l.print()
