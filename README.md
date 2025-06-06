# toDo-python


for this project I will be creating a simple todo app in python, this will consist of 3 baisic files a main for the terminal inputs a todo file for the functions (which will be 5: load/save/add/list/delete) and a json file to hold the data of the todo app

## the load function
- load_tasks()
    - 1. checks if a file containing saved tasks exists
    - 2. if it does, read and return the tasks from the file
    - 3. if not return an empty list

## the save function
- save_tasks()
    - 1. takes a paremter named tasks (which would be the same as what load tasks returns)
    - 2. and dumps it into the json file
