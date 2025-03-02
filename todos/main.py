todos = []

while True:
    user_action = input("typye add,show,edit,complete or exit: ")
    user_action = user_action.strip()

    if 'add' in user_action:
        
            todo = input("Enter a todo: ") + "\n"
            with open('todos/todos.txt','r') as file:
                todos = file.readlines()
            
            todos.append(todo)

            with open('todos.txt','w') as file:
                file.writelines(todos)
    if 'show' in user_action:
            with open('todos.txt','r') as file:
                todos = file.readlines()
            
            #new_todos = [item.strip('\n') for item in todos]

            for index,item in enumerate(todos):
                item = item.strip('\n')
                row = f"{index+1}-{item}"
                print(row)
    if 'edit' in user_action:
            number = input("Number of todos to edit")
            number = number-1
            with open('todos.txt','r') as file:
                todos = file.readlines()
            
            new_todo = input("enter new todo: ")
            todos[number]=new_todo+'\n'
            with open('todos.txt','w') as file:
                file.writelines(todos)
            
    if 'complete' in  user_action:
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
    if 'exit' in user_action:
            break
        

print("Bye!")