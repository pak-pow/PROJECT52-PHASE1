# Week 9: Form Validator

**Category:** Frontend | **Status:** Completed

## About

Forms are the primary way users give data to an application, and validation is the first line of defense against bad data. This project focuses exclusively on client-side form validation — checking input in real time, before anything is ever sent to a server.

The logic lives entirely in `validator.js`. It handles email format checking, password strength rules, required field validation, and real-time error messaging that updates as the user types. The approach is pure Vanilla JavaScript with no libraries, building a solid understanding of how validation frameworks work under the hood.

## What It Does

A multi-field HTML form with complete client-side validation: real-time error messages, field formatting rules, password strength checking, and submission gating until all fields are valid.

## Learning Objectives

- Writing regular expressions for input pattern matching (email, phone formats)
- Real-time validation using `input` and `blur` event listeners
- DOM manipulation to show and clear error messages dynamically
- Understanding the difference between client-side and server-side validation

## Project Structure

```
week9_form_validator/
├── index.html          # Form markup
├── validator.js        # All validation logic
└── style.css           # Form styling and error state styles
```

## Tech Stack

- **Frontend:** HTML5, CSS3, Vanilla JavaScript
