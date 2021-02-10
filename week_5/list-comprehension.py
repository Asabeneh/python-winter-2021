nums = [1, 2, 3, 4, 5] # what is type?
squares = [{i:[i**2, i ** 3]} for i in nums]
print(squares)

# print(list(map(lambda n: n ** 2, nums)))

# def make_square (n):
#     return n ** 2

# print(list(map(make_square, nums)))
# new_list = []

# for i in nums:
#     new_list.append(make_square(i))
# print(new_list)

countries = ['Finland','Sweden','Denmark','Norway','Iceland']
# [['Finlnad','FINLAND', 7,'FIN'], ...]
list_of_lists = [[country, country.upper(), len(country)] for country in countries]
print(list_of_lists)

print([(country, country.upper(), len(country)) for country in countries if 'land' in country])

# import mymodule

# print(mymodule)
# print(dir(mymodule))
# print(mymodule.make_square(3))
# print(mymodule.make_square.__doc__)
# print(mymodule.add_two_numbers(2, 3))
# print(mymodule.add_two_numbers.__doc__)
# print(mymodule.make_square_of_array_items(nums))

# from mymodule import make_square, add_two_numbers, make_square_of_array_items

from mymodule import *

print(make_square(2))
print(make_square(10))
print(add_two_numbers(999, 1))

from mymodule import make_square_of_array_items as list_squares
print(list_squares([10, 20, 30]))