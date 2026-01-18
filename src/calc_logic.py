import math

def calculator(choise, first_num, sec_num):


    if choise == "+":
        return first_num + sec_num
    elif choise == "-":
        return first_num - sec_num
    elif choise == "*":
        return first_num * sec_num
    elif choise == "/":
        return first_num / sec_num
    elif choise == "**":
        return first_num ** sec_num
    elif choise == "%":
        return first_num % sec_num
    elif choise == "root":
        return sec_num ** (1 / first_num)