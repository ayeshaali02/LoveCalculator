

print("Welcome to the Love Calculator!")

name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

lower_name1=name1.lower()
lower_name2=name2.lower()

lower_name=lower_name1+lower_name2
t=int(lower_name.count("t"))
r=int(lower_name.count("r"))
u=int(lower_name.count("u"))
e=int(lower_name.count("e"))

total1=t+r+u+e

l=int(lower_name.count("l"))
o=int(lower_name.count("o"))
v=int(lower_name.count("v"))
e=int(lower_name.count("e"))

total2=l+o+v+e

total=int(str(total1)+str(total2))

if total<=10 or total>=90:
    print(f"Your score is {total}, you go together like coke and mentos.")
elif 40 <= total <= 50:
    print(f"Your score is {total}, you are alright together.")
else:
    print(f"Your score is {total}, you can work on it.")
