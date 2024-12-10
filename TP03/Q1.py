import os

def list_dirs(path):
    try:
        for entry in os.scandir(path):
            if entry.is_dir(follow_symlinks=False):
                print(f"[FOLDER] {entry.path}")
                list_dirs(entry.path)
            else:
                print(f"[FILE] {entry.path}")
    except PermissionError:
        print(f"[NOT ENOUGH PERMISSION] {path}")


if __name__ == "__main__":
    list_dirs("../")

