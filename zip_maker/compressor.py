from compressor_backend import make_archive
import FreeSimpleGUI as sg

# create (widget) instances
label1 = sg.Text("Select files to compress:")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("choose", key="files")

label2 = sg.Text("Select destination folder:")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose", key="folder")

label3 = sg.Text("Give name for the zip file:")
input_name = sg.InputText(tooltip="What's your zip file going to be called?", key="name")

compress_button = sg.Button("Compress")
exit_button = sg.Button("Exit")
output_label = sg.Text(key="output")

# create the window instance
window = sg.Window("File compressor",
                   layout=([[label1, input1, choose_button1],
                            [label2, input2, choose_button2],
                            [label3, input_name],
                            [compress_button, exit_button, output_label]]))

while True:
    event, values = window.read()

    match event:
        case "Compress":
            filepaths = values["files"].split(";")
            folder = values["folder"]
            zip_name = values["name"]
            make_archive(filepaths, folder, zip_name)
            window["output"].update(value="Compression completed, zip file created!")

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break

window.close()
