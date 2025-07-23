# Codex.io Project 
# Area Calculator

'''
Create a program that calculates the area of one of the following shapes
1. Square
2. Rectangle
3. Triangle
4. Circle

The program should present a menu for the user to choose which shape to calculate,
then ask them for the appropriate values (sides, length, width, etc)

It should calculate the area and print it out
'''

from math import pi

print(
    '''
    Pick a shape to calculate the area of: 
    1. Square
    2. Rectangle
    3. Triangle
    4. Circle
    '''
)

s = int(input("Enter a number between 1-4: "))

if s == 1:
    n = int(input("Select a number for side of square: "))
    a = n**2
    print("The area is: ", a)

elif s == 2:
    l = int(input("Select a number for length of rectangle: "))
    w = int(input("Select a number for width of rectangle: "))
    a = l*w
    print("The area is: ", a)

elif s == 3:
    b = int(input("Select a number for base of triangle: "))
    h = int(input("Select a number for height of triangle: "))
    a = (b*h)/2
    print("The area is: ", a)

elif s == 4:
    r = int(input("Select a number for radius of circle: "))
    a = pi * r**2
    print("The area is: ", a)

else:
    print("Not available")
