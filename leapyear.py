'''
If the year is evenly divisible by 4, go to step 2. Otherwise, go to step 5.
If the year is evenly divisible by 100, go to step 3. Otherwise, go to step 4.
If the year is evenly divisible by 400, go to step 4. Otherwise, go to step 5.
The year is a leap year (it has 366 days).
The year is not a leap year (it has 365 days).
'''

year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


if year%4 ==0:
    print("Leap year")

elif (year%100)==0:
    print("Not leap year")

elif (year%400)==0:
    print("Leap year.")
else:
    print("Not leap year.")