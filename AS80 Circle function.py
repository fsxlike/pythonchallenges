pi = 3.14159265359
radius = int(input('What is the radius of your circle in cm?'))

def area():
    print('The area of the circle is',(radius ** 2) * pi,'cm^2')

area()

def circumference():
    print('The circumference of the circle is',(2 * radius) * pi,'cm')

circumference()
