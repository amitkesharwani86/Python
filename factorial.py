def fact(a):
    if a == 0:
        return 1
    else:
        return a * fact(a-1)
    
b=int(input("Enter a number:- "))
print("Factorial of ",b," is",fact(b))