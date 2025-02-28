todos = []

while True:
    user_action = input("typye add,show,edit,complete or exit")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for index,item in enumerate(todos):
                print(index,'-',item)
        case 'edit':
            number = input("Number of todos to edit")
            number = number-1
            new_todo = input("enter new todo: ")
            todos[number]=new_todo
        case 'complete':
            number = int(input("Number of todos to complete: "))
            todos.pop(number-1)
        case 'exit':
            break
        

print("Bye!")