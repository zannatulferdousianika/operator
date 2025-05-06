kg = int(input("Enter your weight: " ))
feet = int(input("Enter you height(feet): "))
inch = int(input("Enter you height(inch): "))

meter = (feet*12+inch)*0.0254
bmi = kg/meter**2

print("Your BMI is: ", round(bmi,2))

if bmi < 18.5:
    print("You are underweight.You need to gain some weight!!")

elif  18.5 <= bmi <= 24.9:
    print("You are normal.Keep it up") 

elif 25 <= bmi <= 29.9:
    print("You are overweighted.You need to loose some weight!!") 

elif 30 <= bmi <= 34.9:
    print("You are obease.You need to loose some weight!!")    
else:
    print("you are extremly obease.. Do to doctor ASAP")          