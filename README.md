# Student Management System — Python

A command-line application for student, Built enrirely in Python using in-memory list.
---
## Overview

The system managament permit, register student, cosult student, found student, show list student, change data student and delete data student.

All data is stored in-memory using Python list and dictionaries  — no external database or framework is required.

## Modules

### `main.py`
Entry point of the application. Runs a `while` loop that renders the main menu and routes user input to the appropriate module function.

### `students.py`
Defines all in-memory data structures:
- `register_student` — list that saved data student.
- `student_show` — for that show list student.
- `student_found` —  for that travel the list and show the espesific student.
- `student_change` — with id student ask a new data and add of the list students.
- `student_delete` — with id student delet the student of the list.

## Authors

Developed by:
* [Andres Quintero](https://github.com/TheplexyBoy)
