lower = int(input("Enter lower range: "))
upper = int(input("Enter upper range: "))
print(f"Prime number between {lower} and {upper}: ")


for n in range(lower,upper+1):
    if n > 1:
        for i in range(2,n):
            if n%i == 0:
                break 
        else:
             print(n)