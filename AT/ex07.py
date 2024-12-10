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

def has_duplicates(lst):
    ht = HashTable(len(lst) * 2)
    for element in lst:
        if ht.search(element) is not None:
            return True
        else:
            ht.insert(element, True)
    return False

data = [1, 2, 3, 4, 5, 3]
print(has_duplicates(data))
