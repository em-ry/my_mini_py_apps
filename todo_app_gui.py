import FreeSimpleGUI as sg
import functions
import time
import os


# check if .txt file exists
if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

# create instances/widgets
clock = sg.Text("", key="clock")
label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todo_list",
                      enable_events=True, size=(45, 10))
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# create an instance of a window
window = sg.Window("My To-Do App",
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=("Helvetica", 15))

# display window instance and other instances
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%b %d, %y %H:%M:%S"))

    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todo_list"].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values["todo_list"][0]
                new_todo = values["todo"] + "\n"
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window["todo_list"].update(values=todos)
            except IndexError:
                sg.popup("Select an item first", font=("Helvetica", 15))

        case "Complete":
            try:
                todos_to_complete = values["todo_list"][0]
                todos = functions.get_todos()
                todos.remove(todos_to_complete)
                functions.write_todos(todos)
                window["todo_list"].update(values=todos)
                window["todo"].update(value="")
            except IndexError:
                sg.popup("Select an item first", font=("Helvetica", 15))

        case "Exit":
            break

        case "todo_list":
            window["todo"].update(value=values["todo_list"][0])

        case sg.WIN_CLOSED:
            break

window.close()
