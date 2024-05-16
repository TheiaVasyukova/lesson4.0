import math

def calculate_circle_area(radius):
    area = math.pi * radius**2
    return area

radius = float(input("Введите радиус круга: "))

area = calculate_circle_area(radius)