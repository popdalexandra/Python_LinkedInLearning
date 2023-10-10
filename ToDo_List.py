import sys

file_name = "todo.txt"
todos = []

# Read File
try:
    file = open(file_name, "r")
    todos = file.readlines()
    file.close()
except:
    pass

print(todos)

# Add ToDo
if len(sys.argv) >= 3 and sys.argv[1].lower() == "add":
    todos.append(f"{sys.argv[2]}\n")
print(todos)

# Remove ToDo
if len(sys.argv) >= 3 and sys.argv[1].lower() == "remove":
    try:
        index_to_delete = int(sys.argv[2])
        if index_to_delete > 0 :
            index_to_delete  -= 1
            del(todos[index_to_delete])
        else:
            print("Wrong number")
            sys.exit(1)
    except Exception as e:
        print(e)
        sys.exit(1) 

print(todos)

# Save File
file = open(file_name, "w")
file.writelines(todos)
file.close()

# Print List
if len(todos) == 0:
    print("You have no todos :)")
else:
    print("\n Here's your ToDo List:\n")
    for x in range(len(todos)):
        print(f"{ x + 1 }. {todos[x]}", end = "") # end = "" - ca sa nu adauge linii noi


# Print Commands
print("\n*********\n")
print(f"To view ToDos:\n{sys.argv[0]}")
print(f"To add a ToDo:\n{sys.argv[0]}")
print(f"To remove or complete ToDo:\n{sys.argv[0]}")