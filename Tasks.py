import plyer
import os
import datetime


class Tasks:

    def __init__(self):
        if os.path.exists("tasks.txt"):
            pass
        else:
            os.mkdir("tasks.txt")

    @staticmethod
    def load_data():
        if os.path.exists("tasks.txt"):
            data_dict = dict()
            with open("tasks.txt", "r") as f:
                while True:
                    line = f.readline().rstrip('\n')
                    if line == "":
                        break
                    else:
                        data_dict[line[:line.index(
                            ':')]] = line[line.index(':') + 1:]
            return data_dict
        else:
            print("No file init object of class Tasks")

    def add_task(self, task, dt):
        self.data = Tasks.load_data()
        self.datakeys = self.data.keys()
        if task in self.datakeys:
            print("Task already exists")
            print("Do you want to update the task ")
            self.choice = input("Enter y/n: ")
            if self.choice == "y":
                Tasks.update_task(self, task, dt)
            else:
                return
        else:
            self.data[task] = dt
            with open("tasks.txt", "w") as f:
                for key, value in self.data.items():
                    f.write(f"{key}:{value}\n")

    def update_task(self, task, dt):
        self.data = Tasks.load_data()
        print(self.data)
        self.datakeys = self.data.keys()
        if task not in self.datakeys:
            print("Task does not exists")
            print("Do you want to add the task ")
            self.choice = input("Enter y/n: ")
            if self.choice == "y":
                Tasks.add_task(self, task, dt)
            else:
                return
        else:
            self.data[task] = dt
            with open("tasks.txt", "w") as f:
                for key, value in self.data.items():
                    f.write(f"{key}:{value}\n")
