import plyer
import os
import datetime
from Tasks import Tasks


if __name__ == "__main__":
    test = Tasks()
    choice = int(input(
        "Enter 1 to add task and 2 to update task 3 to show the data: "))
    match choice:
        case 1:
            task = input("Enter the task: ")
            dt = input("Enter the date: ")
            test.add_task(task, dt)
        case 2:
            task = input("Enter the task: ")
            dt = input("Enter the date: ")
            test.update_task(task, dt)
        case 3:
            print(test.load_data())
        case _:
            print("Invalid choice")
