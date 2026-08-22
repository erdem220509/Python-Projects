# Day #3 — File-Based To-Do Manager 📝

A command-line To-Do Manager built with Python that stores tasks using file handling, allowing tasks to remain saved even after the program is closed.

## Features

* Add new tasks
* View all tasks
* Mark tasks as completed
* Delete tasks
* Save tasks to a text file
* Load previously saved tasks when the program starts
* Input validation for invalid task numbers
* Completed and incomplete task indicators

## Example

```text
=== TO-DO MANAGER ===

1. Add Task
2. View Tasks
3. Complete Task
4. Delete Task
5. Exit

Choose: 2

1: [✓] Learn file handling
2: [ ] Finish Python Day #3
3: [ ] Practice guitar
```

## Concepts Practiced

* File handling
* Reading and writing files
* `with open()`
* File modes (`r` and `w`)
* Persistent data
* Lists and dictionaries
* Functions
* Loops
* `enumerate()`
* Exception handling
* `FileNotFoundError`
* Input validation

## Data Storage

Tasks are stored in `tasks.txt` using a simple format:

```text
Learn file handling,True
Finish Python Day #3,False
Practice guitar,False
```

When the program starts, the file is read and converted back into Python dictionaries.

## How to Run

```bash
python filebasedtodolist.py
```

Part of my **Daily Python Projects** challenge.

**Day #3 ✅**
