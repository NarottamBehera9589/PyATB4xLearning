"""
Create a program , take 2 inputs from the user num1, num2 and give them
max
pow num1 to num2
sub, mul, sum, div.
Format your out with f{""}
"""
num1 = int(input("Enter the First inputs:"))
num2 = int(input("Enter the second inputs:"))
max_num = max(num1,num2)
power = num1**num2
addition = num1+num2
substraction = num1-num2
multipication = num1*num2
division = num1/num2

print(f"max of {num1} and {num2} is: {max_num}")
print(f"power of {num1} and {num2} is: {power}")
print(f"Addition of {num1} and {num2} is: {addition}")
print(f"substraction of {num1} and {num2} is: {substraction}")
print(f"multipication of {num1} and {num2} is: {multipication}")
print(f"division of {num1} and {num2} is: {division}")
