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
