import PthVar as Var


def Operate(numexpr):
    digits = numexpr.split(' ')
    for d in range(digits.__len__()):
        if digits[d].isnumeric():
            digits[d] = float(digits[d])
        elif digits[d] in Var.Vars:
            if Var.Vars.get(digits[d]).isnumeric():
                digits[d] = Var.Vars.get(digits[d])
            elif Var.Vars.get(digits[d]).isalnum():
                digits[d] = len(Var.Vars.get(digits[d]))
        elif digits[d] == '+':
            digits[d] = digits[d-1] + digits[d+1]
            digits.remove(digits[d-1])
            digits.remove(digits[d+1])
    return digits


print (Operate('4 + 5'))
