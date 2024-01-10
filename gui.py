import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass

sg.theme("Black")

empty_line = sg.Text('')
clock = sg.Text('', key="clock")
label = sg.Text("TYPE IN A TO-DO:")
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")
add_button = sg.Button("ADD")
#add_button = sg.Button(image_size=(100, 40), image_source="add.png", mouseover_colors="lightgray", tooltip="Add Todo", key="ADD")
list_box = sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45, 10])
edit_button = sg.Button("EDIT")
complete_button = sg.Button("COMPLETE")
#complete_button = sg.Button(image_size=(100, 40),  image_source="complete.png", mouseover_colors="lightgray", tooltip="Complete", key="COMPLETE")

exit_button = sg.Button("EXIT")

window = sg.Window('To-Do App',
                   layout=[[clock],
                           [empty_line],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                           [exit_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%d %b %Y %H:%M:%S"))

    #print(1, event)
    #print(2, values)
    #print(3, values['todos']) #if exist

    match event:
        case "ADD":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "EDIT":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)

                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))

        case "COMPLETE":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first", font=("Helvetica", 20))

        case "EXIT":
            break

        case "todos":
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break

window.close()
