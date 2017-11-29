a = 10
b = 20

is_not_zero = b != 0

def is_not_zero(value):
    return  value != 0
    # if value != 0:
    #     return True
    # else:
    #     return False

def is_zero(value):
    return value != 0
    # if value == 0:
    #     return True
    # else:
    #     return False

if is_not_zero(b):
    result = a/b
    print("Result:", result)
    print("Result: %f.2" % result)
else:
    print("Zero division error")

s = 'Mark Zukerberg'
if s[0] == 'M' or s[0] == 'm':
    print(" 'm' is the first letter")

x = 10
if x >= 5 and x <= 20:
    print('INSIDE')
else:
    print('OUTSIDE')

def is_millenial(year_of_birth):
    # if year_of_birth > 1981 and year_of_birth <= 2000:
    #     return  True
    # else:
    #     return False
    return year_of_birth > 1981 and year_of_birth <= 2000

if is_millenial(4242):
    print("I'm millenial!")
else:
    print("I'm NOT millenial!")
#1 вариант
def is_even(value):
    if value % 2 == 0:
        print('even')
    else:
        print('not even')

is_even(5)
#2 вариант(лучший вариант)
def is_even_v2(value):
    return value % 2 == 0
#3 вариант
if is_even(5):
    print('even')
else:
    print('not even')

def is_leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

print(is_leap_year(2100))
print(is_leap_year(2000))
