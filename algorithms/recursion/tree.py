from pathlib import Path


def list_directories(path, i=0):
    path = Path(path)

    for item in path.iterdir():
        if item.is_dir():
            print(f'{" " * i}{item.name}/')
            list_directories(item, i + 4)
        else:
            print(f'{" " * i}{item.name}')


list_directories(".")
