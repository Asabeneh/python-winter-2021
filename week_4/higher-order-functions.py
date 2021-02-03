


# print(make_square(3))

# def cube(func, n):
#     return func(n) * n

# print(cube(make_square, 4)) # 4 * 4 * 4


      # an absolute value function


def higher_order_function(type): # a higher order function returning a function
    def square(x):          # a square function
        return x ** 2
    def cube(x):            # a cube function
        return x ** 3
    def absolute(x):        # an absolute value function
        if x >= 0:
            return x
        else:
            return -(x)
    if type == 'square':
        return square
    elif type == 'cube':
        return cube
    elif type == 'absolute':
        return absolute
print(higher_order_function('absolute')(-10))

# map, filter, reduce







numbers = [0, 1, 2, 3, 4, 5] # [0, 1, 4, 9, 16, 25]
def modify_list (lst):
    new_lst = []
    for item in lst:
        new_lst.append(item * item)
    return new_lst
print(modify_list(numbers))


squares = map(lambda x:x**2, numbers)
print(list(squares))


countries = ['Finland','Sweden','Denmark','Norway','Iceland']
# [['FINLAND','FIN',7,['SWEDEN','SWE',6]], ....]

def modify_countries (lst):
    new_st = []
    for item in lst:
        new_st.append([item.upper(),item.upper()[0:3],len(item)])
    return new_st
print(modify_countries(countries))

def func (item):
    return [item.upper(),item.upper()[0:3],len(item)]

countires_2 = map(func, countries)
print(countries)
print(list(countires_2))

# Filter => 

def find_country_with_land (lst):
    new_lst = []
    for item in lst:
        if 'land' in item:
            new_lst.append(item)
    return new_lst
def find_country_without_land (lst):
    new_lst = []
    for item in lst:
        if 'land' not in item:
            new_lst.append(item)
    return new_lst

print(find_country_with_land(countries))
print(find_country_without_land(countries))

def filter_even_numbers (n):
    for i in range(n+1):
        if i % 2 == 0:
            print(i)

print(filter_even_numbers(20))


countries_3 = filter(lambda item: 'land' in item, countries)
print(list(countries_3))
countries_4 = filter(lambda item: 'land' not in item, countries)
print(list(countries_4))

# Reduce => manago + papaya + Guava => blender => smoothie, juice

from functools import reduce

nums = [2, 4, 6]

total = reduce(lambda acc, cur: acc + cur, nums)
print('what is the total here?', total)
prod = reduce(lambda acc, cur: acc * cur, nums, 1)
print(prod)

# acc = 0, cur = 2 => 2
# acc = 2, cur =4 => 6
# acc = 6 cur = 6 => 12
