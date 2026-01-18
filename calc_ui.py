from src import calc_logic
from src import calc_history
import os
import math

GREEN = "\033[1;32m"

#func to clean terminal
def clean_screen():
    os.system("clear")

#cleaning treminal and history of calculations
clean_screen()
calc_history.history_del()

#ui of calculator
while True:

    print(f"{GREEN}---RTX Calculator---\n1)choose options: + -  * /  ** %\n\n2)exit\n\n3)see history\n")

    choise = input("choise: ")
    if choise == "exit" or choise == "2":
        calc_history.history_del()
        clean_screen()
        break

    elif choise == "3" or choise == "see history":
        clean_screen()
        calc_history.history_watch()
        cont1 = input("press enter to continue...")
        clean_screen()

    else:
        first_num = input("enter first num: ")
        sec_num = input("enter sec num: ")
        f_num = round(math.pi, 4) if first_num == "pi" else first_num
        s_num = round(math.pi, 4) if sec_num == "pi" else sec_num
        print("")
        clean_screen()

        try:
            r = calc_logic.calculator(choise, float(f_num), float(s_num))
            r = round(r, 4)
            print("result:", r, "\n")
            calc_history.history_add(float(f_num), choise, float(s_num), r)
        except ZeroDivisionError as e:
            print(f"ZeroDivisionError: {e}\n")
        except ValueError as e:
            print(f"ValueError: {e}\n")
        except TypeError as e:
            print(f"TypeError: {e}\n")

        cont2 = input("press enter to continue...")
        clean_screen()