"""Laboratorio 8 - CLI del gestor de tareas."""

import sys
from todo_manager import read_todo_file, write_todo_file

try:
    if len(sys.argv) < 2:
        raise IndexError("Insufficient arguments provided!")

    if sys.argv[1] == "--help":
        print("""Usage: python main.py <file_path> <command> [arguments]...
Commands:
  add "task"    - Add a task to the list.
  remove "task" - Remove a task from the list.
  view          - Display all tasks.
Examples:
  python main.py tasks.txt add "Buy groceries"
  python main.py tasks.txt remove "Do laundry"
  python main.py tasks.txt view
  python main.py tasks.txt add "Call mom" remove "Take out trash" view""")
        sys.exit()

    file_path = sys.argv[1]
    tasks = read_todo_file(file_path)
    if len(sys.argv) == 2:
        pass
    else:
        i = 2
        modified = False

        while i < len(sys.argv):
            command = sys.argv[i]

            if command == "view":
                if not tasks:
                    write_todo_file(file_path, tasks)

                print("Tasks:")
                for task in tasks:
                    print(task)

                i += 1

            elif command == "add":
                try:
                    task = sys.argv[i + 1]
                except IndexError:
                    raise IndexError('Task description required for "add".')

                tasks.append(task)
                print(f'Task "{task}" added.')
                modified = True
                i += 2

            elif command == "remove":
                try:
                    task = sys.argv[i + 1]
                except IndexError:
                    raise IndexError('Task description required for "remove".')

                if task in tasks:
                    tasks.remove(task)
                    print(f'Task "{task}" removed.')
                    modified = True
                else:
                    print(f'Task "{task}" not found.')

                i += 2

            else:
                raise ValueError("Command not found!")
        if modified:
            write_todo_file(file_path, tasks)

except IndexError as e:
    print(e)

except ValueError as e:
    print(e)