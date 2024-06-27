# Logic behind the Task_Class.
'''This module creates the logic for the TaskClass, which is
responsible for marking tasks complete, checking their status
and returning the id.'''
# Create a new class called Task_Class.
class TaskClass():
    '''Define a TaskClass to hold the following methods.'''
    def __init__(self, filename):
        self.file = filename


    # Define a method to Mark Tasks Complete.
    def mark_task_complete(self, task_id):
        '''Define a method to Mark Tasks Complete.'''

        # Open the Task_Manager_Database.txt file.
        with open('Task_Manager_Database.txt', 'r') as file:
            # If task_id not found in the file inform user.
            content = file.read()

            if task_id not in content:
                print('Task not in Task Manager!')
            # If task_id is in the file write it to the Task_Class_Database.txt file
            # and inform the user.

            else:
                with open('Task_Class_Database.txt', 'a') as file:
                    file.write(task_id + '\n')
                    print('Task Marked as Complete!')


    # Define a method to Check the progression of a task.
    def check_task_status(self, task_id):
        '''Define a method to Check a Tasks Status.'''

        # Open the Task_Manager_Database.txt file.
        with open('Task_Manager_Database.txt', 'r') as file, \
            open('Task_Class_Database.txt', 'r') as file_2:
            content = file.read()
            content_2 = file_2.read()

            # If task_id is in both files inform user taks is complete.
            if task_id in content and task_id in content_2:
                return ('Task Status Complete.')
            
            # If task_id is in one file and not the other inform user task is pending.
            elif task_id in content and task_id not in content_2:
                return ('Task Status Pending!')
            
            # If task_id isn't in either file inform user task doesn't exist.
            else:
                return ('Task doesn\'t exist!')


    def get_task_id(self):
        '''Define a method to Get the ID of a Task.'''

        # Print message to user.
        print('List of all current stored tasks...')

        # Open the Task_Manager_Database.txt file to read the data.
        with open('Task_Manager_Database.txt', 'r') as file:

            # If Task_Manager empty, inform user.
            content = file.readlines()
            if not content:
                print('Task Manager Empty!')

            # for each line, read the data, split it into the first word (task_id)
            # and the rest (description) and print out a formatted string back to user.
            else:
                for line in content:
                    parts = line.split(maxsplit=1)
                    if len(parts) < 2:
                        continue
                    first_word = parts[0]
                    second_word = parts[1]
                    print(f'Task ID: {first_word}, Description: {second_word}')
