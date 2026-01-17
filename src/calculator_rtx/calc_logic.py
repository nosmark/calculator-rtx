def calculator(choise, first_num, sec_num):

    if choise == "+":
        return first_num + sec_num
    elif choise == "-":
        return first_num - sec_num
    elif choise == "*":
        return first_num * sec_num
    elif choise == "/":
        if sec_num == 0:
            return("error, can deny by zero")
        else:
            return first_num / sec_num
    elif choise == "**":
        return first_num ** sec_num
    elif choise == "%":
        return first_num % sec_num
    else:
        return("no such operation!")