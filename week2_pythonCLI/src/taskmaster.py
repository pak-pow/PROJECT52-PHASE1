import argparse
import os
import json

from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "tasks.json")

class TaskManager:
    def __init__(self):
        pass
    
    def load_data(self):
        pass
    
    def save_data(self):
        pass
    
    def list_tasks(self):
        pass
    
def main():
    
    parser = argparse.ArgumentParser(description="Week2 : Task Master CLI")
    parser.add_argument("action", choices=["add", "list", "complete"], help="Action to perform on the task")
    parser.add_argument("--title", help="the title of the task for 'add' action")
    
    arg = parser.parse_args()
    
    if arg.action == "add":
        if arg.title:
            print(f"SYSTEM: Adding task {arg.title}")
            
        else: 
            print("ERROR: Title is required for 'add' action")
            
    elif arg.action == "list":
        print("SYSTEM: Listing all tasks")
        
    elif arg.action == "complete":
        print("SYSTEM: Completing a task")

if __name__ == "__main__":
    main()