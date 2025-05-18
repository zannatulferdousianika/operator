while True:
    n = input("Enter a number or 'exit' to quit: ")
    if n.lower() == 'exit':
        print("Thanks for using.")
        break

    else:
        n = int(n)
        if n % 2 == 0:
           print(f"{n} is even")
        else: 
           print(f"{n} is odd")
   