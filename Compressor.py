import FreeSimpleGUI as gui
from zip_creator import compress_file



label1 = gui.Text("Select Files to Compress:")
input_box1 = gui.Input()
choose_button1 = gui.FilesBrowse("Choose", key="files")

label2 = gui.Text("Select Destination Folder:")
input_box2 = gui.Input()
choose_button2 = gui.FolderBrowse("Choose", key="folder")

compressor_button = gui.Button("Compressor")
output_label = gui.Text(key="output", text_color='Green')

window = gui.Window("File Compressor",[[label1, input_box1, choose_button1],
                                       [label2, input_box2, choose_button2],
                                       [compressor_button, output_label]],font=('Helvetica', 20))

while True:
    event, value = window.read()
    print(event, value)
    match event:
        case 'Compressor':
            filepath = value["files"].split(";")
            folder = value["folder"]
            compress_file(filepath, folder)
            window["output"].update("Files are Compressed Successfully!")
        case gui.WIN_CLOSED:
            break

window.close()