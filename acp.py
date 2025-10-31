def add (a, b) :
    return a+b
def subtract(a,b):
    return a-b
def multi(a,b):
    return a*b
def division(a,b):
    return a/b
def calculator(x,y):
    operator = input("Enter any operator: \n +(Add)\n-(Subtract)\n*(Multi)\n/(Division)\n\n")
    if operator == "+" :
        return add(x,y)
    elif operator == "-" :
        return subtract(x,y)
    elif operator == "*" :
        return multi(x,y)
    elif operator == "/" :
        return division(x,y)
First = int(input("Input the 1st number: "))
Second = int(input("Input the 2nd number: "))
print(calculator(First, Second))
