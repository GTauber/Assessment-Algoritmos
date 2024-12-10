import os
import random
import string


def generate_random_filename():
    return ''.join(random.choices(string.ascii_lowercase, k=8)) + ".txt"


def create_nested_directories(base_path, depth=200, folder_name_length=3):
    current_path = base_path
    for i in range(1, depth + 1):
        folder_name = f"f{i:0{folder_name_length}}"
        current_path = os.path.join(current_path, folder_name)

        if len(current_path) > 255:
            print(f"Stop in {i} folders due to system limit")
            break

        os.makedirs(current_path, exist_ok=True)

        file_name = generate_random_filename()
        with open(os.path.join(current_path, file_name), 'w') as f:
            f.write(f"File inside {folder_name}")

    print(f"Depth {current_path}")


if __name__ == "__main__":
    base_directory = "nested_test"
    create_nested_directories(base_directory, depth=200, folder_name_length=2)
