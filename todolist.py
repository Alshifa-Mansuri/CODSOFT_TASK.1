# TO-DO LIST command line application
# Define a function to display the menu
def show_menu():
    print("1.Add Task")
    print("2.View Task")
    print("3.Remove Task")
    print("4.Update Task")
    print("5.exit")
# Main function 
def main():
    tasks = []
    while True :
        show_menu()
        choice = input("choose on option:") 
        if choice =='1':
             task = input("Enter task:") 
             tasks.append(task)
             print("Task added!")
        elif choice =='2':
            print("\n-- Task List --")
            for i, task in enumerate(tasks):
                print(f"{i + 1}.{task}")
            print("----------------\n")
        elif choice =="3":  
            task = input("Remove task :")
            if task in tasks :
                tasks.remove(task)
        elif choice =='4':
            old_task = input("Enter task to update:")
            if old_task in tasks:
                new_task = input("Enter new task:")
                index = tasks.index(old_task)
                tasks[index] = new_task
                print("Task updated!")        
        elif choice =='5':
            print("Existing...")
            break
        else :                 
              print("Involid option, try again.")
if  __name__ =="__main__":
    main()              