import FreeSimpleGUI as sg
import functions

# create instances
label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todo_list",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")

# create an instance of a window
window = sg.Window("My To-Do App",
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=("Helvetica", 15))
# display window and other instances
while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values["todo"])
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window["todo_list"].update(values=todos)

        case "Edit":
            todo_to_edit = values["todo_list"][0]
            new_todo = values["todo"]

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todo_list"].update(values=todos)

        case "todo_list":
            window["todo"].update(value=values["todo_list"][0])

        case sg.WIN_CLOSED:
            break

print("Hello")
window.close()
