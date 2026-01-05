import argparse
import sys

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

if __name__ == "__main__":
    main()