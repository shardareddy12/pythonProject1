

def add(a,b):
  return(a+b)

def subtract(a,b):
  return(a-b)

def multiplication(a,b):
  return(a*b)

def divide(a,b):
  return(a/b)

operations={
  "+": add,
  "-": subtract,
  "*":multiplication,
  "/":divide }

num1= int(input("what's the 1st number?"))

for key in operations:
  print(key)

oprtn=input("which operation do you want to do?")
num2= int(input("what's the next number?"))
function= operations[oprtn]
first_operation=function(num1,num2)
print(f"{num1}{oprtn}{num2}={first_operation}")

continue_stat= True
while continue_stat:
  continue_statement=input(f"Type 'Y' if you continue calculating/n    with {first_operation} or type 'N'")
  if continue_statement=='Y':
    function= operations[oprtn]
    first_operation=function(num1,num2)
    print(f"{num1}{oprtn}{num2}={first_operation}")

    num3=int(input("what's the next number?"))
    oprtn=input("which operation do you want to do?")
    function2= operations[oprtn]
    another_operation=function2(first_operation,num3)
    print(f"{first_operation}{oprtn}{num3}={another_operation}")
  else:
    continue_stat=False