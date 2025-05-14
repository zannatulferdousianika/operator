w = int(input("Enter the temparature in celsius: "))

if w>30 and w<45:
    print("It's summer")
elif w>22 and w<30:
    print("It's winter") 
elif w>25 and w<35:
    print("It's spring")
else:
    print("Put correct celsius...")           