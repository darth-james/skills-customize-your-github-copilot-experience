# 📘 Assignment: Command-Line Task Tracker

## 🎯 Objective

Build a small command-line task tracker that lets a user add, view, and complete tasks. Use Python's built-in `json` module to keep the task list between program runs.

## 📝 Tasks

### 🛠️ Create and Manage Tasks

#### Description
Complete the task-management functions in `starter-code.py`. Run the program with `python starter-code.py` and use its menu to try adding, viewing, and completing tasks.

#### Requirements
Completed program should:

- Store each task as a dictionary with a `title` and a `done` value
- Add a task when the user enters a non-empty title
- Display tasks with numbers and a clear completed or not-completed status
- Show a helpful message when there are no tasks
- Mark a task as complete when its number is selected, and handle invalid task numbers

### 🛠️ Save Tasks Between Runs

#### Description
Finish `load_tasks()` and `save_tasks()` using Python's standard-library `json` module. Store the data in `tasks.json` in the same folder as the program.

#### Requirements
Completed program should:

- Load the task list from `tasks.json` when the program starts
- Start with an empty list when `tasks.json` does not exist yet
- Save task changes after adding a task or marking one complete
- Keep saved tasks and their completion status when the program is run again
