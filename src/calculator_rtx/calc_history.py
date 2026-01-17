import csv
import os

FILE_PATH = "data/history.csv"

def history_add(first_num, operation, sec_num, result):
    if not os.path.exists("data"):
        os.makedirs("data")

    with open("data/history.csv", "a", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([first_num, operation, sec_num, result])


def history_watch():
    if not os.path.exists("data"):
        os.makedirs("data")    
    if not os.path.exists("data") or os.path.getsize("data/history.csv") == 0:
        print("no history yet\n")
    with open("data/history.csv", "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        for r in reader:
            if r:
                print(f"{r[0]} {r[1]} {r[2]} = {r[3]}")



def history_del():
    with open("data/history.csv", "w", newline="") as csvfile:
        pass