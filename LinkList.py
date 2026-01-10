a = float(input("Enter Price :  "))
d = float(input("Enter khareed Price :  "))
while(1):
    b = float(input("Enter weight :  "))
    if(b == 0):
        break;
    c = a * b
    e = b * d
    print("----------------------")
    print (c / 1000)
    print (e / 1000)
    print((c - e) / 1000)
    print("----------------------")
