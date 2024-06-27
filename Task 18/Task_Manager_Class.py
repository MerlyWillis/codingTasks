# Logic behind the Task_Manager Class.
'''This module creates the logic for the TaskManager class, this is
responsible for holding the methods to add, remove and view tasks.'''
# Create a new class called Task_Manager.
class TaskManager():
    '''Define a TaskManager class to hold the following methods.'''
    # Initialise an attribute to store  tasks in a dictionary.
    def __init__(self, filename):
        self.file = filename


    # Define a method to add tasks to the dictionary attribute.
    def add_task(self, task_id, description):
        '''Define a method to add tasks to the self.task attribute.'''

        # Open the Task_Manager_Database.txt file.
        with open('Task_Manager_Database.txt', 'a') as file:

            # Write the tasks_id and description to the file.
            file.write(task_id + ' ' + description + '\n')

            # Inform user the write operation was successful.
            print('Task successfully added to database!')


    # Define a method to remove tasks from the dictionary attribute.
    def remove_task(self, task_id):
        '''Define a method to remove tasks from the self.task attribute.'''

        # Set a variable task_removed to boolean value 'False'.
        task_removed = False
        
        # Read all lines from the file.
        with open('Task_Manager_Database.txt', 'r') as file:
            content = file.readlines()
        
        # Filter out the lines containing the task_id.
        new_content = []
        for line in content:
            if task_id not in line.split(' '):
                new_content.append(line)
            else:
                task_removed = True
        
        # Write the filtered content back to the file.
        with open('Task_Manager_Database.txt', 'w') as file:
            file.writelines(new_content)
        
        # Print appropriate message based on whether the task was removed.
        if task_removed:
            print('Task removed from Task Manager!')
        else:
            print('Task not in Task Manager!')


    def view_tasks(self):
        '''Define a method to view all tasks currently stored within 
        the self.task attribute.'''

        # Open the file Task_Manager_Database.txt.
        with open('Task_Manager_Database.txt', 'r') as file:

            # Set variable 'content' to the file's lines read.
            content = file.readlines()

            # If content is empty, inform user Task Manager is empty.
            if not content:
                return 'Task Manager Empty!'
            
            # Else, process each line, split it into the first part (task_id) and the rest
            # (description) and collect results in a list.
            else:
                result = []
                for line in content:
                    parts = line.split(maxsplit=1)
                    if len(parts) < 2:
                        continue
                    first_word = parts[0]
                    second_word = parts[1].strip()
                    result.append(f'Task ID: {first_word}, Description: {second_word}')
                return '\n'.join(result) if result else 'Task Manager Empty!'