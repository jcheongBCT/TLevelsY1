import math

SideA = float(input("Enter side A: "))
SideB = float(input("Enter side B: "))

answer = (SideA ** 2) + (SideB ** 2)
answer = math.sqrt(answer)
print("The answer is...")
print(answer)