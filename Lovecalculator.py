# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name3=name1+name2
name= name3.lower()

Tcount= name.count("t")+name.count("r")+name.count("u")+name.count("e")
Lcount=name.count("l")+name.count("o")+name.count("v")+name.count("e")
LoveScore= int(str(Tcount)+str(Lcount))


if LoveScore<10 or LoveScore>90:
    print(f"Your score is {LoveScore}, you go together like coke and mentos.")
elif LoveScore>40 and LoveScore<50:
    print(f"Your score is {LoveScore}, you are alright together.")
else:
    print(f"Your score is {LoveScore}")
