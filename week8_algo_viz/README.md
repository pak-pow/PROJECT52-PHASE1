# Week 8: Algorithm Visualizer

**Category:** Frontend | **Status:** Completed

## About

Algorithms are abstract by nature. The best way to truly understand how a sorting or pathfinding algorithm works is to watch it run, step by step. This project translates complex algorithmic logic into real-time visual animations rendered directly in the browser.

The entire application is a single Python file (`main.py`) which, despite being a "frontend" project conceptually, uses Python's `tkinter` library to render a desktop GUI. Each algorithm is implemented from scratch and visualized with animated bar charts or grid animations, stepping through the actual execution with a configurable delay so the user can watch each comparison and swap happen in real time.

## What It Does

A desktop GUI application that visualizes sorting and pathfinding algorithms in real time. Users can select an algorithm, set the speed, and watch the step-by-step execution animated on screen.

## Learning Objectives

- Implementing sorting and pathfinding algorithms from scratch
- Building a desktop GUI with Python's `tkinter`
- Translating algorithmic state into visual representations
- Understanding time complexity by observing algorithm behavior directly

## Project Structure

```
week8_algo_viz/
└── main.py     # Full application: GUI setup, algorithm implementations, and animation logic (10KB)
```

## Tech Stack

- **Language:** Python 3
- **GUI:** tkinter (Python standard library)
