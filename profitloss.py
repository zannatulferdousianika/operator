b = float(input("Enter buying price: "))
s = float(input("Enter selling price: "))

if s > b :
    p = s - b
    print(f"You made a profit of {p} TAKA")
elif s == b :
    print("No profit! No loss")    
else :
    l = b -s 
    print(f"You made a loss of {l} TAKA")    