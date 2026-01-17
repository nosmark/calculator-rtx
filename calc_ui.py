from src import calc_logic
import os
from src import calc_history
GREEN = "\033[1;32m"

def clean_screen():
    os.system("clear")

clean_screen()
calc_history.history_del()

while True:

    print(f"{GREEN}---RTX Calculator---\n1)choose options: + -  * /  ** %\nor\n2)exit\nor\n3)see history")

    choise = input("choise: ")
    if choise == "exit" or choise == "2":
        calc_history.history_del()
        clean_screen()
        break

    elif choise == "3" or choise == "see history":
        clean_screen()
        calc_history.history_watch()
        cont1 = input("press enter to continue...")

    else:
        first_num = input("enter first num: ")
        sec_num = input("enter sec num: ")
        print("")
        clean_screen()

        try:
            r = calc_logic.calculator(choise, int(first_num), int(sec_num))
            print("result:", r, "\n")
            calc_history.history_add(first_num, choise, sec_num, r)
        except:
            print("mewmewmew\n")

        cont2 = input("press enter to continue...")
        clean_screen()