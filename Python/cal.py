a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
c= str(input("Enter an operator: "))   
if c=='+':
    print(a+b)
elif c=='-':    
    print(a-b)
elif c=='*':
    print(a*b)
elif c=='/':
    print(a/b)
else:
    print("Invalid operator")