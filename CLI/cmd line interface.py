menu = """
welcome to list!
-a to add
-r to remove an item
-s to show list
"""
print(menu)
todo = []
user_input = None
while True:
    user_input = input("CMD>: ")
    cmd = user_input[0:4]
    option = user_input[5:7]
    item = user_input[8:]

    if cmd == "list":
        if option == "-a":
            todo.append(item)
        elif option == "-r":
            todo.pop(int(item))
        elif option == "-s":
            for i, item in enumerate(todo):
                print(i, item)
        else:
            print("invalid option")
    elif cmd == "exit" or cmd == "quit":
        break
    else:
        print("invalid command")





























