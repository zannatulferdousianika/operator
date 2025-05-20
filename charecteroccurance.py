s = input("Enter a sentence: ").lowe()
c = input("Please enter the charecter you want to find: ")

i = 0
count = 0
while i < len(s):
    if s[i] == c:
        count= count+1
    i = i + 1
print(f"Total occurance of {c} is {count}.")

