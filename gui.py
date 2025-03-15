import FreeSimpleGUI as sg
import functions

# create instances
label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter a todo")
add_button = sg.Button("Add")

# create an instance of a window
window = sg.Window("My To-Do App", layout=[[label], [input_box, add_button]])
# display window and other instances
window.read()
print("Hello")
window.close()
