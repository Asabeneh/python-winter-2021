# Function => built-in functions
# Custom function
# It is easy to reuse
# It makes code easy to read
# It easy to test code


def name_of_function ():
    print('print something form the function')

name_of_function()

def do_something ():
    print('Of course, I doing something, actually I am teaching here')

do_something()


def add_two_nums (a, b):
    return a + b
    

print(add_two_nums(2, 3))

def print_fullname (first_name, last_name):
    return first_name + ' ' + last_name

print(print_fullname('Asabeneh','Yetayeh'))
print(print_fullname('Paivi','Sonck'))


def sum_all_numbers(n):
    total = 0
    for i in range(n + 1):
        total +=  i
    return total
print(sum_all_numbers(5)) # => 0, 1, 2, 3, 4, 5
print(sum_all_numbers(100)) # => 0, 1, 2, 3, 4, 5

def add_all_evens (n):
    evens = 0;
    for i in range(0, n+1, 2):
        evens +=  i
    return f'The sum of all evens is {evens}'
print(add_all_evens(100))

# default parameters
# weight = mass * gravity

def calculate_weight(mass, gravity = 9.81):
    return f'The weight of the body is {round(mass * gravity, 1)} N'

print(calculate_weight(75))
print(calculate_weight(75, 1.62))


# I like you to develop a function what adds numbers

def add_numbers(*nums):
    total = 0
    for n in nums:
        total += n
    return total

print(add_numbers(1, 2, 3, 6, 9, 1000, 125))

def generate_groups (team,*args):
    print(team)
    print(args)
    for i in args:
        print(i)
generate_groups('python-winter','Asabeneh','Marc','Rafel','Baptist','Paivi')

# c = 2x + 4y

linear_equation = lambda x, y : 2 * x + 4 * y

print(linear_equation(1, 1))


