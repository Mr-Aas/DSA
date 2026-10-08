# from collections import deque

# class Queue:
#     def __init__(self):
#         self.queue = deque()

#     def enque(self, value):
#         self.queue.append(value)

#     def deque(self):
#         if len(self.queue) > 0:
#             return self.queue.popleft()
#         raise IndexError("deque from empty queue")

#     def __str__(self):
#         return str(list(self.queue))

# # Testing the Queue
# q = Queue()
# print(q)         # Output: []
# q.enque(34)
# print(q)         # Output: [34]
# q.enque(23)
# print(q)         # Output: [34, 23]
# q.deque()
# print(q)         # Output: [23]


# ______________queqe without seeing__________

from collections import deque


class queue:
    def __init__(self):
        self.data = deque()

    def insert(self, data):
        self.data.append(data)

    def pop(self):
        self.data.pop()

    def __str__(self):
        return str(self.data)


newque = queue()
newque.insert(23)
newque.insert(2234)
newque.insert(233324234)
print(newque)
newque.pop()
print(newque)
