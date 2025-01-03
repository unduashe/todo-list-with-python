import csv

todos = []
stop = False

def get_todos():
    global todos
    return todos

def add_one_task(title):
    # your code here
    todos.append([title])
    pass

def print_list():
    global todos
    if len(todos) == 0:
        print("0 items left in ToDo list")
    else:
        for index, item in enumerate(todos, start=1):
            print(f"{index}. {item[0]}")
    pass

def delete_task(number_to_delete):
    # your code here
    if number_to_delete.isnumeric() and int(number_to_delete) <= len(todos):
        deleted_task = todos[int(number_to_delete) - 1]
        todos.pop(int(number_to_delete) - 1)
        print(f"{deleted_task} deleted")
    else:
        print("the item you are trying to delete doesn't exist, please verify the number of the item to delete")
    pass

def save_todos():
    # your code here
    try:
        with open('todos.csv', 'w', newline='') as todosfile:
            writer = csv.writer(todosfile)
            writer.writerows(todos)
    except Exception as e:
        print(f"No se ha podido guardar el archivo: {e}")
    pass

    
def load_todos():
    # your code here
    try:
        with open('todos.csv', 'r') as todosfile:
            reader = csv.reader(todosfile)
            for line in reader:
                todos.append([line])
    except Exception as e:
        print(f"No se ha podido importar el archivo: {e}")
    pass

# Below this code will only run if the entry file running was app.py
if __name__ == '__main__':
    while stop == False:
        print("""
    Choose an option: 
        1. Add one task
        2. Delete a task
        3. Print the current list of tasks
        4. Save todo's to todos.csv
        5. Load todo's from todos.csv
        6. Exit
    """)
        response = input()
        if response == "6":
            stop = True
        elif response == "3":
            print_list()
        elif response == "2":
            print("What task number you want to delete?")
            number_to_delete = input()
            delete_task(number_to_delete)
        elif response == "1":
            print("What is your task title?")
            title = input()
            add_one_task(title)
        elif response == "4":
            print("Saving todo's...")
            save_todos()
        elif response == "5":
            print("Loading todo's...")
            load_todos()
        else:
            print("Invalid response, asking again...")