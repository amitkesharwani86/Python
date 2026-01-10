def fabo(a,b,c,sum):
    if(a==0):
        return sum
    else:
        d=b+c
        print(" , ",d,end="")
        b=c
        c=d
        return fabo(a-1,b,c,sum+d)
    
a=int(input("enter no. of terms"))
b=0
c=1
sum=1
print(b," , ",c,end="")
d=fabo(a-2,b,c,sum)
print("\nSum of series is ",d)