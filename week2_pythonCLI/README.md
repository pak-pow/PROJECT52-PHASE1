# 🐍 Week 02: Python CLI Task Manager

A lightweight, command-line based task management tool built with Python 3.
Engineered as part of **Project 52**.

## 🚀 Features
* **Persistence:** Tasks are saved to `data/tasks.json` automatically.
* **CRUD Operations:** Create, Read, Update, and Delete tasks.
* **Track Status:** Mark tasks as pending or complete.

## 🛠️ Installation
1.  Ensure you have Python 3 installed.
2.  Clone this repository.
3.  Navigate to the source folder:
    ```bash
    cd src
    ```

## 🎮 Usage Guide

### 1. Add a Task
```bash
python taskmaster.py add --title "Buy Groceries"

```

### 2. List All Tasks

```bash
python taskmaster.py list

```

*Displays a table of IDs, Status, and Titles.*

### 3. Complete a Task

```bash
python taskmaster.py complete --id 1

```

### 4. Edit a Task (Fix Typos)

```bash
python taskmaster.py edit --id 1 --title "Buy Organic Groceries"

```

### 5. Delete a Task

```bash
python taskmaster.py delete --id 1

```

## 📂 Project Structure

* `src/taskmaster.py`: The Logic Core (Entry Point).
* `data/tasks.json`: The Database (Auto-generated).
