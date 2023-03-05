import plyer
import os
import datetime
from Tasks import Tasks
import threading
import time


def f1():
    while True:
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


def f2():
    while True:
        data = Tasks.load_data()
        elems = []
        for i in list(data.values()):
            if str(i).split(" | ")[0] == datetime.datetime.now().strftime("%d/%m/%Y"):
                elems.append(str(i))
        for i in elems:
            if (str(i).split(" | ")[1] == datetime.datetime.now().strftime("%H:%M")):
                plyer.notification.notify(
                    title="Task",
                    message=list(data.keys())[list(data.values()).index(i)],
                    timeout=10
                )
                data.pop(list(data.keys())[list(data.values()).index(i)])
                with open("tasks.txt", "w") as f:
                    for key, value in data.items():
                        f.write(f"{key}:{value}\n")


if __name__ == "__main__":
    t1 = threading.Thread(target=f1)
    t2 = threading.Thread(target=f2)
    t1.start()
    t2.start()
