import figure
myline = figure.line(10,20)
width, height=myline.get_length()
try:
    rectangle = figure.area_rectangle(width, height)
    print(rectangle)
except ValueError:
    print("please input positive number for width and height")

try:
    right_triangle=figure.area_right_triangle(width, height)
    print(right_triangle)
except ValueError:
    print("please input positive number for width and height")

try:
    ecllipse=figure.area_ecllipse(width, height)
    print(ecllipse)
except ValueError:
    print("please input positive number for width and height")
