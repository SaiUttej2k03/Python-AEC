#Simple calculator
def operation(a,b,op):
    if(op=='+'):
        return a+b
    elif(op=='-'):
        return a-b
    elif(op=='*'):
        return a*b
    elif(op=='/'):
        if(a>b):
            return a/b
        else:
            print("Denominator is less than numerator")
    else:
        print("Option not availiable")

a=int(input("Enter the first value"))
b=int(input("Enter the second value"))
op=input("Enter the operation to be performed")
i=1

    
result=operation(a, b, op)
if result==None:
    print("Try again")
else:
    print("Result is :",result)


