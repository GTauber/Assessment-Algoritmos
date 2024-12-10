class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
    def _hash(self, key):
        return hash(key) % self.size

    def insert(self, key, value):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return
        self.table[index].append([key, value])

    def search(self, key):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                return item[1]
        return None

    def remove(self, key):
        index = self._hash(key)
        for item in self.table[index]:
            if item[0] == key:
                self.table[index].remove(item)
                return True
        return False

table = HashTable(10)

table.insert("key1", "value1")
table.insert("key2", "value2")
table.insert("key3", "value3")

print("Associated value of 'key1':", table.search("key1"))
print("Associated value of 'key2':", table.search("key2"))

table.remove("key2")
print("value associated with key2 after removal:", table.search("key2"))
