u = int(input("Enter your consumed unit: "))

if u <= 100:
    bill = u*1.5
elif u <= 200:
    bill = (100 * 1.5)+(u - 100)*4.5
elif u <= 300:
    bill = (100 * 1.5)+(100 * 4.5)+(u - 200)*6
else:       
 bill = (100 * 1.5)+(100 * 4.5)+(100 * 6)+(u-200)*8

print("Final bill", bill)