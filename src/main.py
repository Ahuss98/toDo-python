from todo import add_task,list_tasks, mark_done, delete_task

def show_menu():
    print("your todo list!")
    print("1. Add Task")
    print("2. List Task")
    print("3. Mark Done Task")
    print("4. Delete Task")
    print("5. EXIT")

def main():
    while True:
        show_menu()
        choice = input('Choose an option please: ')

        if choice == '1':
            task = input('Enter a task: ')
            add_task(task)
            print(f'{task} has been added')
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            try:
                index = int(input('what task would you like to mark as completed: ')) -1
                mark_done(index)
            except ValueError:
                print('please enter a valid task number')
        elif choice == '4':
            toDelete = int(input('provide the number of the task you want to delte: ')) -1
            delete_task(toDelete)
        elif choice == '5':
            print('see you later!')
            break
        else:
            print('invalid choice, try again')

if __name__ == '__main__':
    main()