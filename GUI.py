import functions
import FreeSimpleGUI as gui
import time


gui.theme('DarkBlack')
clock = gui.Text('', key='clock')
label = gui.Text("Type in a To-Do")
input_box = gui.Input(tooltip='Enter To-Do:', key='todo')
add_button = gui.Button('Add')
list_box = gui.Listbox(values=functions.get_todos(), key='todos',
                       enable_events=True, size=(45, 10))

edit_button = gui.Button('Edit')
complete_button = gui.Button('Complete')
exit_button = gui.Button("Exit")
output_text = gui.Text(key='output', text_color='Green')

window = gui.Window("My To-Do App",
                    layout=[[clock],
                            [label],
                            [input_box, add_button],
                            [list_box,edit_button,complete_button],
                            [exit_button, output_text]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=100)
    window['clock'].update(value=time.strftime("%b %d, %Y %H:%M:%S"))

    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'].title() + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update('')
            window['output'].update("New To-Do is Added!")

        case 'Edit':
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']
                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update('')
                window['output'].update("To-Do is Edited!")
            except IndexError:
                gui.popup(custom_text="Please Select an Item First!", title="Warning")

        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update('')
                window['output'].update("To-Do is Completed!")
            except IndexError:
                gui.popup(custom_text="Please Select an Item First!", title="Warning")

        case 'Exit':
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case gui.WIN_CLOSED:
            break



