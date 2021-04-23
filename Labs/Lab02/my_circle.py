PI = 3.14159
radius = 0

radius = float(input("Enter the radius of a circle and press enter : "))

circumference = 2 * PI * radius
area = PI * radius * radius
print("Circumference :", circumference)
print("Area :", area)

double_radius = 2 * radius

double_circumference = 2 * PI * double_radius
double_area = PI * double_radius * double_radius

print("Circumference for double_radius", double_circumference)
print("Area for double_radius", double_area)
print()
print("Circumference increases by {} times".format(double_circumference/circumference))
print("Area increases by {} times".format(double_area/area))