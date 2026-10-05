import math

radius = float(input("Choose the radius of the circle: "))
area_of_circle = math.pi * (radius ** 2)
circum_of_circle = 2 * math.pi * radius 

print("The area of the circle if the radius is ", radius, "is ", area_of_circle, ".")
print("The circumference of the circle if the radius is ", radius, "is ", circum_of_circle, ".")