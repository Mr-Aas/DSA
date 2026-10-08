class hashTable:
    def __init__(self):
        self.maxlength = 100
        self.container = [None for i in range(self.maxlength)]

    def get_hash(self, key):
        h = 0
        for ch in key:
            h += ord(ch)
        return h % 100

    def addItem(self, key, value):
        # def __setitem__(self, key): will support table["key"] = "value" method

        h = self.get_hash(key)
        self.container[h] = value

    def getitem(self, key):
        # def __getitem__(self, key): will support table["key"] method
        h = self.get_hash(key)
        return self.container[h]

    def delete(self, key):
        h = self.get_hash(key)
        self.container[h] = None


table = hashTable()
# print(table.get_hash("hello"))
# print(table.get_hash("hello"))
table.addItem("name", "aas mohd")
table.addItem("name2", "aasu")
table.addItem("name3", "aas")
print(table.getitem("name3"))
print(table.getitem("name2"))
print(table.getitem("name"))
print(table.container)
