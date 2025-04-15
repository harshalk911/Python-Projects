import FreeSimpleGUI as gui
from zip_extractor import extractor


gui.theme('DarkBlack')

label_1 = gui.Text("Select the file to Extract")
input_box = gui.Input()
choose_but1 = gui.FileBrowse("Choose", key='file')

label_2 = gui.Text("Select Destination Folder")
input_box2 = gui.Input()
choose_but2 = gui.FolderBrowse("Choose", key='folder')

extract_button = gui.Button("Extract",)
output_text = gui.Text('', key='output', text_color='Green')

window = gui.Window("Zip File Extractor",layout=[[label_1, input_box, choose_but1],
                                                 [label_2, input_box2, choose_but2],
                                                 [extract_button, output_text]])

while True:
    event, values = window.read()
    match event:
        case "Extract":
            try:
                filepath = values['file']
                dest_dir = values['folder']
                extractor(filepath, dest_dir)
                window['output'].update(value="File Extraction Complete!")
            except FileNotFoundError:
                gui.popup('Please Select the File First')
        case gui.WIN_CLOSED:
            break
window.close()