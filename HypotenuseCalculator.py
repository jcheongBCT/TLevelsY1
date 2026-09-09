import math

sideA = float(input("Side A: "))
sideB = float(input("Side B: "))

SideC = str(math.sqrt((sideA ** 2) + (sideB ** 2)))
if(isinstance(sideA, float) and isinstance(sideB, float)):
    print("Your hypotenuse is..." + SideC)
else:
    print("Incorrect, you have given me the wrong type!")
