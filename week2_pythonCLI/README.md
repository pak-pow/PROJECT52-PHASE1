# Week 2: Python CLI Task Manager

**Category:** Backend | **Status:** Completed

## About

The first Python project of Phase 1. Moving away from the browser entirely, this project is a command-line application that runs in the terminal. The goal was to learn how to build an interactive program that accepts user input, processes it through structured logic, and persists state between sessions using a JSON file.

The application logic lives in `src/taskmaster.py`. Tasks are saved to `data/tasks.json`, meaning the task list survives after the program closes. This is a foundational pattern — separating the program logic from its data storage — that reappears in more complex forms throughout the rest of Phase 1 and Phase 2.

## What It Does

A terminal-based task manager where users can add, view, complete, and delete tasks. All tasks are persisted to a local JSON file so they survive between sessions.

## Learning Objectives

- Building interactive command-line interfaces in Python
- Handling user input, loops, and conditional branching
- Reading and writing JSON files for lightweight data persistence
- Structuring a Python project with separate `src/` and `data/` directories

## Project Structure

```
week2_pythonCLI/
├── src/
│   └── taskmaster.py   # Main CLI application logic
└── data/
    └── tasks.json      # Persisted task data (JSON)
```

## Tech Stack

- **Language:** Python 3
- **Storage:** JSON file
