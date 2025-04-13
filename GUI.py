from re import Match

import functions
import FreeSimpleGUI as gui

label = gui.Text("Type in a To-Do")
input_box = gui.Input(tooltip='Enter To-Do:', key='todo')
add_button = gui.Button('Add')
list_box = gui.Listbox(values=functions.get_todos(), key='todos',
                       enable_events=True, size=(45, 10))

edit_button = gui.Button('Edit')

complete_button = gui.Button('Complete')

window = gui.Window("My To-Do App",
                    layout=[[label],[input_box, add_button],[list_box,edit_button,complete_button]],
                    font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'].title() + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'Complete':
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            index = todos.index(todo_to_complete)
            todos.pop(index)
            functions.write_todos(todos)
            window['todos'].update(values=todos)

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case gui.WIN_CLOSED:
            break



