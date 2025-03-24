import FreeSimpleGUI as sg
from extractor_backend import extract_archive

# create widgets
label1 = sg.Text("Select files to extract:")
input1 = sg.Input()
choose_button1 = sg.FileBrowse("Choose", key="archive")

label2 = sg.Text("Select dest. folder:")
input2 = sg.Input(tooltip="Select where zip file will be extracted to")
choose_button2 = sg.FolderBrowse("Choose", key="folder")

extract_button = sg.Button("Extract")
exit_button = sg.Button("Exit")
output_label = sg.Text(key="output")

# create the window instance
window = sg.Window("Archive Extractor",
                   layout=([[label1, input1, choose_button1],
                            [label2, input2, choose_button2],
                            [extract_button, exit_button, output_label]]))

while True:
    event, values = window.read()

    match event:
        case "Extract":
            try:
                archive_path = values["archive"]
                dest_folder = values["folder"]
                extract_archive(archive_path, dest_folder)
                window["output"].update(value="Extraction Complete!")
            except FileNotFoundError:
                sg.popup("Please select a zip file and destination folder!")

        case "Exit":
            break

        case sg.WIN_CLOSED:
            break

window.close()
