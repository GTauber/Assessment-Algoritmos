import os

def list_files_recursively(directory):
    files = []
    for item in os.listdir(directory):
        item_path = os.path.join(directory, item)
        if os.path.isdir(item_path):
            files.extend(list_files_recursively(item_path))
        elif os.path.isfile(item_path):
            files.append(item_path)
    return files

if __name__ == "__main__":
    base_directory = "nested_test"

    all_files = list_files_recursively(base_directory)
    print(f"Total files found: {len(all_files)}")

    for file_path in all_files:
        print(file_path)
