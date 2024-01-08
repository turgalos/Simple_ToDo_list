def get_todos(filepath="todos.txt"):
    """ Read a text file and return list of todos """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """Write a todo list to a file"""
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)

# jesli functions.py zostanie wywołane samodzielnie
if __name__ == "__main__":
    print("HALKOOOOOOOOO")