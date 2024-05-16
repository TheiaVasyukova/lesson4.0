input = input("Введите радиус круга: ")

def calculate_circle_area(radius):
    area = math.pi * radius**2
    return area

radius = float(input("Введите радиус круга: "))

area = calculate_circle_area(radius)

print(f"Площадь круга: {area:.2f}")
print(f"Площадь круга с радиусом {radius} равна {area:.2f}")
