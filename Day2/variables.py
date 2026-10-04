# Day 2: 30 Days of python programming

first_name = "Kyle"
last_name = "Wilver"
full_name = "Kyle Wilver"
country = "Canada"
city = "Montreal"
age = 20
year = 2026
is_married = False
is_true = True
is_light_on = True
x,y,z = 1,2,3

print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

print("First name lenght: ",len(first_name))
print("Last name lenght: ",len(last_name))

num_one = 5
num_two = 4

total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two
remainder = num_one % num_two
exp = num_one ** num_two
floor_division = num_one // num_two

# Circle
import math

radius = 30
area_of_circle = math.pi * (radius ** 2)
print("The area of the circle if the radius is ", radius, "is ", area_of_circle, ".")

circum_of_circle = 2 * math.pi * radius
print("The circumference of the circle if the radius is ", radius, "is ", circum_of_circle, ".")

radius = float(input("Choose the radius of the circle: "))
area_of_circle = math.pi * (radius ** 2)
circum_of_circle = 2 * math.pi * radius 

print("The area of the circle if the radius is ", radius, "is ", area_of_circle, ".")
print("The circumference of the circle if the radius is ", radius, "is ", circum_of_circle, ".")

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
country = input("Enter your country: ")
age = int(input("Enter your age: "))

print("Hello", first_name, last_name, ". You are curently", age, "and from", country, ".")