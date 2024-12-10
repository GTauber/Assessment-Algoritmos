def hanoi_tower(n, origin, destination, auxiliary):
    if n == 1:
        disk = origin.pop()
        destination.append(disk)
        print_state(origin, destination, auxiliary)
        return

    hanoi_tower(n - 1, origin, auxiliary, destination)

    disk = origin.pop()
    destination.append(disk)
    print_state(origin, destination, auxiliary)

    hanoi_tower(n - 1, auxiliary, destination, origin)


def print_state(origin, destination, auxiliary):
    print(f"Origin: {origin}")
    print(f"Destination: {destination}")
    print(f"Auxiliary: {auxiliary}")
    print("-" * 30)


if __name__ == "__main__":
    origin_pin = [3, 2, 1]
    destination_pin = []
    auxiliary_pin = []

    print("Initial State:")
    print_state(origin_pin, destination_pin, auxiliary_pin)
    print("Moves:")
    hanoi_tower(len(origin_pin), origin_pin, destination_pin, auxiliary_pin)
