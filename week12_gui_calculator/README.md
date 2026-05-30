# Week 12: GUI Calculator

**Category:** Desktop Application | **Status:** Completed

## About

The final project of Phase 1 and the most polished desktop application in the entire phase. This is a fully functional GUI calculator built with Python and `tkinter`, then compiled into a standalone Windows executable using `PyInstaller`.

The compiled application lives in the `dist/` directory — a self-contained `.exe` that runs on any Windows machine without requiring Python to be installed. The `main.spec` file is the PyInstaller configuration that defines how the build is packaged. This project bridges the gap between writing a Python script and shipping a real, distributable desktop application.

## What It Does

A fully functional desktop calculator with a graphical interface. Supports standard arithmetic operations, keyboard input, and is packaged as a standalone Windows executable via PyInstaller.

## Learning Objectives

- Building a complete desktop GUI with Python `tkinter`
- Handling keyboard and button input events
- Implementing a calculation engine with proper operator precedence
- Packaging a Python application into a standalone executable with `PyInstaller`

## Project Structure

```
week12_gui_calculator/
├── main.py             # Calculator application source code
├── main.spec           # PyInstaller build configuration
├── build/              # PyInstaller intermediate build artifacts
└── dist/               # Compiled standalone executable
```

## Tech Stack

- **Language:** Python 3
- **GUI:** tkinter (Python standard library)
- **Build:** PyInstaller
