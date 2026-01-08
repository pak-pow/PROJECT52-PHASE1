import argparse
import os
import json

from datetime import datetime

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "tasks.json")

class TaskManager:
    def __init__(self):
        self.task = self.load_data()
    
    def load_data(self):
        
        if not os.path.exists(DATA_FILE):
            return []
        
        try: 
            with open (DATA_FILE, "r") as file:
                data = json.load(file)
                return data
            
        except (json.JSONDecodeError, IOError):
            return []
    
    def save_data(self):
        with open(DATA_FILE, "w") as file:
            json.dump(self.task, file, indent=4)
    
    def add_task(self, title):
        
        new_id = self.task[-1]["id"] + 1 if self.task else 1
        
        task = {
            "id": len(self.task) + 1,
            "title": title,
            "status": "pending",
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.task.append(task)
        self.save_data()
        print(f"DATA SAVED: Task '{title}' with id '{task['id']}' added successfully.")
        
    
    def list_tasks(self):
        
        if not self.task:
            print("SYSTEM: No tasks found.")
            return
        
        print(f"{'ID':<5} {'Title':<30} {'Status':<10} {'Created At':<20}")
        print("-" * 70)
        
        for task in self.task:
            status = "✓" if task["completed"] else "○"
            print(f"{task['id']:<5} {task['title']:<30} {status:<10} {task['created_at']:<20}")
            
    def complete_task(self, task_id):
        
        found = False
        
        for task in self.task:
            if task["id"] == task_id:
                task["completed"] = True
                task["status"] = "completed"
                found = True
                
                print(f"DATA SAVED: Task with id '{task_id}' marked as completed.")
        
                break
        
        if found:
            self.save_data()
        
        else:
            print(f"ERROR: Task with id '{task_id}' not found.")
            
    def delete_task(self, task_id):
        
        task_to_remove = None
        
        for task in self.task:
            if task["id"] == task_id:
                task_to_remove = task
                break

        if task_to_remove:
            self.task.remove(task_to_remove)
            self.save_data()
            print(f"DATA SAVED: ID: '{task_id}' TITLE: '{task_to_remove['title']}' deleted successfully.")
        else:
            print(f"ERROR: Task with id '{task_id}' not found.")

def main():
    
    parser = argparse.ArgumentParser(description="Week2 : Task Master CLI")
    parser.add_argument("action", choices=["add", "list", "complete", "delete"], help="Action to perform on the task")
    
    parser.add_argument("--title", help="the title of the task for 'add' action")
    parser.add_argument("--id", type=int, help="Task ID for 'complete' or 'delete' action")
    
    arg = parser.parse_args()
    manager = TaskManager()
    
    if arg.action == "add":
        if arg.title:
            print(f"SYSTEM: Adding task {arg.title}")
            manager.add_task(arg.title)
            
        else: 
            print("ERROR: Title is required for 'add' action")
            
    elif arg.action == "list":
        print("SYSTEM: Listing all tasks")
        manager.list_tasks()
        
    elif arg.action == "complete":
        
        if arg.id:
            print(f"SYSTEM: Completing task with id {arg.id}")
            manager.complete_task(arg.id)
        
        else:
            print("ERROR: Task ID is required for 'complete' action")  
            
    elif arg.action == "delete":
        
        if arg.id:
            print(f"SYSTEM: Deleting task with id {arg.id}")
            manager.delete_task(arg.id)
        else:
            print("ERROR: Task ID is required for 'delete' action")

if __name__ == "__main__":
    main()