todos = []

while True:
    user_action = input("typye add,show,edit,complete or exit: ")
    user_action = user_action.strip()

    match user_action:
        case 'add':
            todo = input("Enter a todo: ") + "\n"
            with open('todos/todos.txt','r') as file:
                todos = file.readlines()
            
            todos.append(todo)

            with open('todos.txt','w') as file:
                file.writelines(todos)
        case 'show':
            with open('todos.txt','r') as file:
                todos = file.readlines()
            
            #new_todos = [item.strip('\n') for item in todos]

            for index,item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index+1}-{item}"
                print(row)
        case 'edit':
            number = input("Number of todos to edit")
            number = number-1
            with open('todos.txt','r') as file:
                todos = file.readlines()
            
            new_todo = input("enter new todo: ")
            todos[number]=new_todo+'\n'
            with open('todos.txt','w') as file:
                file.writelines(todos)
            
        case 'complete':
            number = int(input("Number of todos to complete: "))
            with open('todos.txt','r') as file:
                todos = file.readlines()
            index= number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(number-1)
            with open('todos.txt','w') as file:
                file.writelines(todos)
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        case 'exit':
            break
        

print("Bye!")