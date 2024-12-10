import time

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


class Profile:
    def __init__(self, username, details):
        self.username = username
        self.details = details


class SequentialList:
    def __init__(self):
        self.list = []

    def insert(self, username, details):
        self.list.append(Profile(username, details))

    def retrieve(self, username):
        for profile in self.list:
            if profile.username == username:
                return profile.details
        return None


def main():
    data_size = 1_000_000
    user_data = [("user" + str(i), f"details{i}") for i in range(data_size)]
    target_user = "user999999"

    print("== Teste da HashTable ==")
    hash_table = HashTable(size=10_000)

    start = time.time()
    for username, details in user_data:
        hash_table.insert(username, details)
    hash_insert_time = time.time() - start

    start = time.time()
    hash_table_result = hash_table.search(target_user)
    hash_search_time = time.time() - start

    print(f"Tempo de inserção na HashTable: {hash_insert_time:.6f}s")
    print(f"Tempo de busca na HashTable: {hash_search_time:.6f}s")
    print(f"Resultado da busca: {hash_table_result}\n")

    print("== Teste da Lista Sequencial ==")
    sequential_list = SequentialList()

    start = time.time()
    for username, details in user_data:
        sequential_list.insert(username, details)
    list_insert_time = time.time() - start

    start = time.time()
    list_result = sequential_list.retrieve(target_user)
    list_search_time = time.time() - start

    print(f"Tempo de inserção na Lista Sequencial: {list_insert_time:.6f}s")
    print(f"Tempo de busca na Lista Sequencial: {list_search_time:.6f}s")
    print(f"Resultado da busca: {list_result}\n")

    print("== Comparação Final ==")
    print(f"Tempo de inserção: HashTable é {'mais rápida' if hash_insert_time < list_insert_time else 'mais lenta'}")
    print(f"Tempo de busca: HashTable é {'mais rápida' if hash_search_time < list_search_time else 'mais lenta'}")

if __name__ == "__main__":
    main()
