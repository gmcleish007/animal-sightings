FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Opens up data file to obtain existing list of todos """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return(todos_local)

def write_todos(todos_arg, filepath=FILEPATH):
    """ Opens up data file and re-writes updated data """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)

if __name__ == "__main__":
    print("Helloooooooo")