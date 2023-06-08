Hi, User!

To run this test task follow this simple steps:
* checkout
* install requirements
* 'manage.py migrate' to create database structure
* 'manage.py tasksetup' to fill database with test data
* 'manage.py taskrun' to find unique IDs of producers of products linked to
  given contract through credit requests

Sources of the solution here /cft/test_task/management/commands/taskrun.py
