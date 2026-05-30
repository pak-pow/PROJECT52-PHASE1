# Week 7: Product Landing Page

**Category:** Frontend | **Status:** Completed

## About

This project introduced Tailwind CSS — a utility-first CSS framework — as a contrast to the hand-rolled vanilla CSS from earlier weeks. Building a polished, conversion-optimized product landing page is a real-world frontend task that tests layout skills, typography, responsive design, and visual hierarchy all at once.

The project uses a standard Tailwind build pipeline: `src/input.css` defines the Tailwind directives, and the compiled output is written to `src/output.css`. The `src/script.js` handles any interactive elements (such as mobile navigation toggles). The main markup lives in `index.html`.

## What It Does

A fully responsive product landing page built with Tailwind CSS, featuring a hero section, feature highlights, and a call-to-action — the standard anatomy of a professional marketing page.

## Learning Objectives

- Understanding utility-first CSS and the Tailwind workflow
- Setting up a Tailwind build pipeline with `npm`
- Designing responsive layouts using Tailwind's grid and flexbox utilities
- Understanding the difference between writing CSS by hand vs. using a utility framework

## Project Structure

```
week7_landing_page/
├── index.html              # Main landing page markup
├── package.json            # npm config and Tailwind dependency
├── tailwind.config.js      # Tailwind configuration
└── src/
    ├── input.css           # Tailwind directives (@tailwind base, etc.)
    ├── output.css          # Compiled CSS output (26KB)
    └── script.js           # Interactive element logic
```

## Tech Stack

- **Frontend:** HTML5, Tailwind CSS
- **Build Tool:** npm, Tailwind CLI
