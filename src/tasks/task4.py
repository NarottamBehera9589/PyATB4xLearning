# Write a Python program to calculate the area of a circle given its radius using the formula  area=π×r^2 ( Take pie as 3.14)
radius = float(input("Enter the radius of the circle: "))
pi = 3.14
area = pi * (radius ** 2)
print(f"The area of the circle with radius {radius} is: {area}")