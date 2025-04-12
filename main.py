import functions

while True:
    user_prompts = input("Please type add, show, edit, complete or exit: ")
    user_prompts = user_prompts.strip()

    if user_prompts.startswith('add'):
        todo = user_prompts[4:]

        todos = functions.get_todos('todo.txt')

        todos.append(todo + '\n')

        functions.write_todos('todo.txt', todos)

    elif user_prompts.startswith('show'):

        todos = functions.get_todos('todo.txt')

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row.title())

    elif user_prompts.startswith('edit'):
        try:
            number = int(user_prompts[5:])
            number = number - 1

            todos = functions.get_todos('todo.txt')

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'

            functions.write_todos('todo.txt', todos)

        except ValueError:
            print("Enter a Valid Number")
        continue

    elif user_prompts.startswith('complete'):
        try:
            number = int(user_prompts[9:])

            todos = functions.get_todos('todo.txt')

            index = number - 1
            todos_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todos('todo.txt', todos)

            message = f"TO DO '{todos_to_remove}' has been removed"
            print(message)

        except IndexError:
            print("There is no item with that number")

        except ValueError:
            print("Enter a Valid Number")
        continue

    elif user_prompts.startswith('exit'):
        break
    else:
        print("Type a Valid Command!")

print("Bye!")

