import os

current_directory = os.getcwd()
directory_files = os.listdir()
filepath = os.path.join(current_directory, 'handling_exceptions.py')
exception_stats = os.stat(filepath)
print('My working directory:', current_directory)
print('My files: ', directory_files)
print('My exceptions file:', exception_stats)