# Main Program to run the User Interface.
'''This program allows a user to add/remove tasks to an external database,
they can also mark them as complete, check their progression and
view all current tasks within the database.
'''
# Import the Task_Manager_Class & Task_Class into the file.
from Task_Manager_Class import TaskManager
from Task_Class import TaskClass

# Initialise an instance of the Task_Manager class and Task_Class
# for use within the file.
task_manager = TaskManager('Task_Manager_Database.txt')
task_class = TaskClass('Task_Class_Database.txt')

# Welcome user to the application with greeting message.
print('Welcome to the Task Manager Application.')
print('Please make a selection from the list below.')

# Use a While True loop to run the main-menu until the application is Exited.
while True:
    print('1. Add a Task')
    print('2. Remove a Task')
    print('3. Mark a Task Complete')
    print('4. Check a Tasks Progression.')
    print('5. Get a Tasks ID')
    print('6. View all Tasks')
    print('7. Exit Application')
    choice = input('Enter Choice: ')

    if choice == '1':
        task_id = input('Enter Task ID (e.g #123): ')

        if len(task_id) > 4 or len(task_id) == 0 or task_id.isalpha():
            print('Enter a valid id, e.g #123')
            continue 
        description = input('Enter Task Description: ')
        
        if not isinstance(description, str):
            print('Enter a string value, e.g Clean Car')
            continue
        task_manager.add_task(task_id, description)

    elif choice == '2':
        task_id = input('Enter Task ID (e.g #123): ')

        if len(task_id) > 4 or len(task_id) == 0 or task_id.isalpha():
            print('Enter a valid id, e.g #123')
            continue 

        task_manager.remove_task(task_id)

    elif choice == '3':
        task_id = input('Enter Task ID (e.g #123): ')

        if len(task_id) > 4 or len(task_id) == 0 or task_id.isalpha():
            print('Enter a valid id, e.g #123')
            continue 

        task_class.mark_task_complete(task_id)

    elif choice == '4':
        task_id = input('Enter Task ID (e.g #123): ')

        if len(task_id) > 4 or len(task_id) == 0 or task_id.isalpha():
            print('Enter a valid id, e.g #123')
            continue 

        print(task_class.check_task_status(task_id))

    elif choice == '5':
        task_class.get_task_id()

    elif choice == '6':
        print(task_manager.view_tasks())

    elif choice == '7':
        print('Thanks for using the Task Manager Application!')
        break 

    else:
        print('Invalid entry, please make a choice (1-4).')