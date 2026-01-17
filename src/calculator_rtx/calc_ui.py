import calc_logic

while True:
    print("---RTX Calculator---\n1)choose options: + -  * /  ** %\nor\n2)exit")

    choise = input("choise: ")
    if choise == "exit" or choise == "2":
        break
    else:
        first_num = input("enter first num: ")
        sec_num = input("enter sec num: ")
        try:
            print(calc_logic.calculator(choise, int(first_num), int(sec_num)), "\n")
        except:
            print("mewmewmew")