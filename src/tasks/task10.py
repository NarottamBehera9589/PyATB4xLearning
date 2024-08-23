n = int(input("Enter Any Number:"))
result = 1

for i in range(1, n + 1):
    result *= i
print(f"The factorial of {n} is {result}")