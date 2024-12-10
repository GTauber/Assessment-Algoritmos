class Queue:
    def __init__(self):
        self.queue = []

    def add_client(self, name):
        self.queue.append(name)
        print(f"Client {name} added to queue.")

    def atender_client(self):
        if not self.queue:
            print("Any client in queue to atender.")
            return None
        client = self.queue.pop(0)
        print(f"Atendendo client: {client}")
        return client

    def queue_size(self):
        size = len(self.queue)
        print(f"Number of clients in queue: {size}")
        return size

atendimento_queue = Queue()

atendimento_queue.add_client("Client 1")
atendimento_queue.add_client("Client 2")
atendimento_queue.add_client("Client 3")

atendimento_queue.atender_client()
atendimento_queue.atender_client()

atendimento_queue.queue_size()
