import math

def Hello(name):
    print('Hello, %s!!!' % (name))

Hello('World')
Hello('Alice')
Hello('Dmitry')

#------------------------------------

def pretty_print(value, symbol='-', number_repeat=20):
    print(symbol*number_repeat)
    print('Value: %s' % value)
    print(symbol*number_repeat)

#------------------------------------

def rectangle_square(height, width):
    result = height * width
    return result

result1 = rectangle_square(10, 20)
pretty_print(result1)

#------------------------------------

def square_square(side):
    return rectangle_square(side, side)

pretty_print(square_square(50))

#------------------------------------

def add_and_multiply(x, y):
    result_add = x + y
    result_mult = x * y
    return  result_add, result_mult, x**y

result2, result3, result4 = add_and_multiply(2, 3)
pretty_print(result2)
pretty_print(result3)
pretty_print(result4, '*', 25)
#------------------------------------

#F=C*9/5+32
def cels2farn(degrees):
    return degrees*1.8 + 32
print("%.2f" % cels2farn(36.6))

def circle_square(radius):
    return math.pi*radius**2
print("%.2f" % circle_square(10))