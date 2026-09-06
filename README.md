# ToDoList

A to-do list with a Tkinter GUI. Type a task, press Add, click one in the list and press Delete.

I wrote it in January 2023, on the same day as BudgetApp, while learning Tkinter. The tasks live in a plain list of strings and every change clears the Listbox and refills it from that list.

## Run it

    python ToDoList.py

## Rough edges

- Only the button adds a task. Enter in the box does nothing.
- Add with an empty box adds an empty task, and the box isn't cleared after a real one.
- The scrollbar is packed to the right edge of the window rather than to the list, so it sits at the edge instead of beside what it scrolls.
- Nothing is saved between runs.
