import FreeSimpleGUI as gui

label1 = gui.Text("Select Files to Compress:")
input_box1 = gui.Input()
choose_button1 = gui.FilesBrowse("Choose")

label2 = gui.Text("Select Destination Folder:")
input_box2 = gui.Input()
choose_button2 = gui.FolderBrowse("Choose")

compressor_button = gui.Button("Compressor")

window = gui.Window("File Compressor",[[label1, input_box1, choose_button1],
                                       [label2, input_box2, choose_button2],
                                       [compressor_button]])
window.read()
window.close()