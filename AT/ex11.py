class Queue:
    def __init__(self):
        self.queue = []

    def add_client(self, name):
        self.queue.append(name)
        print(f"Client {name} added to queue.")

    def atender_client(self):
        if not self.queue:
            print("No client in queue to atender.")
            return None
        client = self.queue.pop(0)
        print(f"Atendendo client: {client}")
        return client

    def queue_size(self):
        size = len(self.queue)
        print(f"Number of clients in queue: {size}")
        return size


def simulate_client_service():
    client_queue = Queue()

    client_queue.add_client("Alice")
    client_queue.add_client("Bob")
    client_queue.add_client("Charlie")
    client_queue.add_client("Diana")

    client_queue.atender_client()
    client_queue.atender_client()

    client_queue.queue_size()

    client_queue.add_client("Eve")
    client_queue.add_client("Frank")

    client_queue.atender_client()
    client_queue.atender_client()
    client_queue.atender_client()

    client_queue.queue_size()

    client_queue.atender_client()

    client_queue.atender_client()


if __name__ == "__main__":
    simulate_client_service()
