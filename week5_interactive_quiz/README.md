# Week 5: Interactive Quiz App

**Category:** Frontend | **Status:** Completed

## About

This project marks the point where JavaScript moves from simple DOM tweaks to managing real application state. A quiz app requires tracking the current question, the user's score, time limits, and which answers have been selected — all in memory, without any backend.

The entire application runs in the browser across three files. `index.html` defines the quiz shell, `style.css` handles the layout and feedback styling (correct/wrong highlights), and `script.js` contains all the logic: question rendering, answer validation, score tracking, and progression through the quiz.

## What It Does

A browser-based interactive quiz with multiple-choice questions, real-time score tracking, answer feedback, and a results summary screen at the end.

## Learning Objectives

- Managing application state in JavaScript without a framework
- Dynamic DOM rendering: generating question and answer elements from a data array
- Event handling for user interactions (answer selection, next question)
- Conditional logic for scoring and feedback

## Project Structure

```
week5_interactive_quiz/
├── index.html      # Quiz UI shell
├── script.js       # All quiz logic: state, rendering, scoring
└── style.css       # Styling and answer feedback states
```

## Tech Stack

- **Frontend:** HTML5, CSS3, Vanilla JavaScript
