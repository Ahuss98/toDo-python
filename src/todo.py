import json
from pathlib import Path

DATA_FILE = Path("data/tasks.json")


def load_tasks():
    if DATA_FILE.exists():
        with open(DATA_FILE,'r') as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(DATA_FILE,'w') as f:
        json.dump(tasks,f,indent=2)

def add_task(task):
    tasks = load_tasks()
    tasks.append({'task': task, 'done': False})
    save_tasks(tasks)

def list_tasks():
    tasks = load_tasks()
    for i,task in enumerate(tasks,1):
        status = 'DONE' if task['done'] else 'NOT DONE'
        print(f"{i}. {task['task']}: {status}")


def mark_done(index):
    tasks = load_tasks()
    if index >= 0 and index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)
    else:
        print('Invalid Task number')

def delete_task(index):
    tasks = load_tasks()
    removed = tasks.pop(index)
    print(f'you deleted {removed}')
    save_tasks(tasks)
