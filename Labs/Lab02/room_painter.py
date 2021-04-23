COVERAGE = 100

length = float(input("Enter the length of the room in feet : "))
width = float(input("Enter the width of the room in feet : "))
height = float(input("Enter the height of the room in feet : "))
coats = int(input("Enter the number of coats : "))

surface_area = 2 * (length * height) + 2 * (width * height) + (length * width)
coverage_needed = surface_area * coats
cans_of_paint_required = coverage_needed/COVERAGE

print("You need {} cans of paint".format(cans_of_paint_required))