import math

while True:
    print("\n Welcome to RTX Calculator\nchoose option:\n1)make operation\n2)exit")
    
    descision = int(input(""))
    if descision == 1:
        first_num = float(input("enter first number: "))
        oper = input("enter operation: ")
        sec_num = float(input("enter second number: "))

        if oper == "+":
            print(f"summ is {first_num + sec_num}")
        elif oper == "-":
            print(f"diff is {first_num - sec_num}")
        elif oper == "*":
            print(f"prod is {first_num * sec_num}")
        elif oper == "/":
            if sec_num == 0:
                print("can't divide by 0!")
            else:
                print(f"quot is {first_num / sec_num}")
        elif oper == "**":
            print(f"power is {first_num ** sec_num}")
        elif oper == "%":
            print(f"reminder is {first_num % sec_num}")
        else:
            print("wrong operation")
    elif descision == 2:
        break
    else:
        print("no such option!")