# Here I will Import and test the Task Manager Interface file.
'''This script import the TaskClass and TaskManager class to ensure their
methods perform as expected via use of the Unittest library.'''

import unittest
from Task_Manager_Class import TaskManager
from Task_Class import TaskClass

## ** UNIT-TESTING SECTION ** ##

class TestTaskManager(unittest.TestCase):
    '''Creating a class to test the Task_Manager and Task_Class objects.'''

    def setUp(self):
        '''Setup the test data for the functions to use.'''

        self.task_manager = TaskManager('Task_Manager_Database.txt')
        self.task_class = TaskClass('Task_Class_Database.txt')
        self.task_id = '#123'
        self.task_id_2 = '#321'
        self.description = 'Clean House'
        self.description_2 = 'Go Shopping'

    # Use-Case #1, function add_task should add a task id and description
    # to the self.task attribute.
    def test_add_task(self):
        '''tests the add task method.'''

        # Add a test task_id and description to the task manager.
        self.task_manager.add_task(self.task_id, self.description)

        # Open the file Task_Manager_Database.txt
        with open('Task_Manager_Database.txt', 'r') as file:

            # Read the contents, assert the task_id and description are inside.
            content = file.read()
            self.assertIn(self.task_id, content)
            self.assertIn(self.description, content)

    # Use-Case #2, function remove_task should take a task id and remove it
    # from the self.task attribute.
    def test_remove_task(self):
        '''tests the remove task method.'''

        # Add a test task_id and description to the database.
        self.task_manager.add_task(self.task_id_2, self.description_2)

        # Remove the task_id and description from the database.
        self.task_manager.remove_task(self.task_id_2)

        # Open the file Task_Manager_Database.txt.
        with open('Task_Manager_Database.txt', 'r') as file:
            content = file.read()
            
        # Assert the task_id and description aren't inside the file anymore.
        self.assertNotIn(self.task_id_2, content)
        self.assertNotIn(self.description_2, content)

    # Use-Case #3, function MarkTaskComplete should take the task_id and add it
    # to the self.complete attribute.
    def test_mark_task_complete(self):
        '''tests the mark task complete method.'''

        # Add a task_id and description to the task manager.
        self.task_manager.add_task(self.task_id, self.description)

        # Open the file Task_Class_Database.txt.
        with open('Task_Class_Database.txt', 'a') as file:

            # Write the task_id to the file.
            file.write(self.task_id)

        # Open the file Task_Manager_Database.txt.
        with open('Task_Manager_Database.txt', 'r') as file:

            # Read the contents of the file.
            content = file.read()

            # Assert the task_id and description are within the file.
            self.assertIn(self.task_id, content)
            self.assertIn(self.description, content)

            # With the Task_Class_Database.txt file open.
        with open('Task_Class_Database.txt', 'r') as file:

            # Read the content, assert the task_id and content are inside.
            content = file.read()
            self.assertIn(self.task_id, content)

    # Use-Case #4, function view_tasks should print out a formatted sentence
    # containing the task_id and description for each current task stored
    # within the self.task attribute.
    def test_view_tasks(self):
        '''tests the view all tasks method.'''

        # Assert user is informed Task Manager Empty whilst that is the case.
        with open('Task_Manager_Database.txt', 'w') as file:
            pass

        self.assertEqual('Task Manager Empty!', self.task_manager.view_tasks())

        # With Task_Class_Database.txt open as file.
        with open('Task_Manager_Database.txt', 'w+') as file:

            # write in the task_id and description.
            file.write(self.task_id + ' ' + self.description)

            # Assert view_tasks function returns formatted view of data to user. 
            expected_output = f'Task ID: {self.task_id}, Description: {self.description}'
        self.assertEqual(expected_output, self.task_manager.view_tasks())

    # Use-Case #5, function CheckTaskStatus should return a tasks status
    # if it exists.
    def test_check_task_status(self):
        '''tests the check task status method.'''

        # With Task_Manager_Database.txt file open.
        with open('Task_Manager_Database.txt', 'w') as file:

            # Write task_id and description to the file.
            file.write(self.task_id + ' ' + self.description)

            # With Task_Manager_Database.txt file open again.
        with open('Task_Manager_Database.txt', 'r') as file:

            # Assert task_id and description are now within the file.
            self.assertIn(self.task_id + ' ' + self.description, file)

            # With the Task_Class_Database.txt file open.
        with open('Task_Class_Database.txt', 'w') as file:

            # Write the task_id to the file.
            file.write(self.task_id)

              # With the Task_Class_Database.txt file open again.
        with open('Task_Class_Database.txt', 'r') as file:

            # Assert the task_id is within the file.
            self.assertIn(self.task_id, file)

# If the script is being run directly, commence the testing.
if __name__ == '__main__':
    unittest.main()