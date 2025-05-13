r = str(input("Do you have any medical records?: YES, NO: " )).lower()

if r == "yes":
   p = float(input("Enter your attendence percentage: "))
   if p >= 60:
     print("You are eligable for the exam")
   else:
    print("You are not eligible for the exam, even with medical records.")



elif r == "no":
    p = float(input("Enter your attendence percentage: "))
    if p >= 75:
     print("Your are eligable for exam.")
    else:    
     print("You are not eligible for the exam due to low attendance.")
