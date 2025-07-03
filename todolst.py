todo=[]
def add(task):
    todo.append([task, "Not Done"])
    print("Task added successfully")
    disp()
def dele(n):
    if 0 < n <= len(todo):
        del todo[n-1]
        print("Task deleted successfully")
    else:
        print("Invalid task number.")
    disp()
def mark(n):
    if 0 < n <= len(todo):
        todo[n-1][1] = "Done"
    else:
        print("Invalid task number.")
    disp()
def disp():
    print("\n\n--ToDo List--")
    for i in range(len(todo)):
        print(i+1,".",todo[i][0],"|",todo[i][1])
ch=0
while True:
    print("\n\n1.Add Task\n2.Delete Task\n3.Mark as read\n4.Exit")
    ch=int(input("Enter choice: "))
    if ch==1:
        t=input("Enter the task: ")
        add(t)
    elif ch==2:
        try:
            n = int(input("Enter the task number to delete: "))
            dele(n)
        except ValueError:
            print("Please enter a valid number.")
    elif ch==3:
        try:
            n = int(input("Enter the task number to mark as done: "))
            mark(n)
        except ValueError:
            print("Please enter a valid number.")
    elif ch==4:
        print("Thank You!")
        break
    else:
        print("enter correct option")
    
