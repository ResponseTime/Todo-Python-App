import plyer
import os
import datetime


class Tasks:
    data_dict = dict()

    def __init__(self):
        if os.path.exists("tasks.txt"):
            pass
        else:
            os.mkdir("tasks.txt")

    def load_data(self):
        with open("tasks.txt", "r") as f:
            while True:
                line = f.readline().rstrip('\n')
                if line == "":
                    break
                else:
                    Tasks.data_dict[line[:line.index(
                        ':')]] = line[line.index(':') + 1:]
        return Tasks.data_dict

    def add_task(self, task, date, time):
        pass


if __name__ == "__main__":
    test = Tasks()
    print(test.load_data())
