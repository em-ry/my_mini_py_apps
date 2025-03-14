import functions
import time


now = time.strftime("%b %d, %y %H:%M:%S")
print("It is", now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ").strip()
    if user_action.startswith("add"):
        todo = user_action[4:] + "\n"

        todos = functions.get_todos()

        todos.append(todo)

        functions.write_todos(todos)

    elif user_action.startswith("show"):
        todos = functions.get_todos("todos.txt")

        for index, item in enumerate(todos):
            item = item.strip("\n")
            row = f"{index + 1}-{item}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[-1])
            new_todos = input("Enter new todos: ")

            todos = functions.get_todos()
            # add \n to edited todos
            todos[number - 1] = new_todos + "\n"

            # send edited list back to file
            functions.write_todos(todos)
        except ValueError:
            print("Command is not Valid!")

    elif user_action.startswith("complete"):
        try:
            completed_todo = int(user_action[9:])
            # Open and retrieve file contents
            todos = functions.get_todos()

            removed_todo = todos.pop(completed_todo - 1)
            print(f"The todo item'{removed_todo[:-1]}'has been successfully removed.")

            functions.write_todos(todos)
        except ValueError:
            print("Command is not Valid!")
        except IndexError:
            print("Command line is not valid!")

    elif user_action.startswith("exit"):
        break

    else:
        print("Command is invalid!")
