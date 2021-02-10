
import math
import random

print(math.pow(2, 3))
print(2 ** 3)
print(math.sqrt(4))
print(math.sqrt(3))
print(math.sqrt(2))
print(round(9.81))
print(math.ceil(9.81))

print(math.ceil(3.14))
print('what is here', round(3.141111111, 4))
print(math.floor(3.14))
print(math.floor(9.81))
print(dir)

print(dir(random))

print(math.floor(random.random() * 11)) # 0 to 0.9999999 * 10 => 9.9999
# If I ask to generate a number 0 to 10-> 10.999


def random_num_gen(n):
    factor = n + 1
    return math.floor(random.random() * factor)

print(random_num_gen(10))

import webbrowser

url_lists = [
    'http://www.python.org',
    'https://www.linkedin.com/in/asabeneh/',
    'https://twitter.com/Asabeneh',
    'https://github.com/Asabeneh',
]

print(dir(webbrowser))

for url in url_lists:
    webbrowser.open_new_tab(url)
