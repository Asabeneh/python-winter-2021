# On this file we will talk about data types
''' 
Numbers(integer, float, complex)
String
List
Tuple
Set
Dictionary
'''
# Number data type
print(3)
print(type(3))
print(3.14)
print(type(3.14))
print(1 + 1j)
print(type(1 + 1j))

# Strins => any form of text under single, or double, or multiple quotation

first_name = 'Asabeneh'
last_name = 'Yetayeh'
full_name = first_name + ' ' + last_name
print(full_name)
print(first_name, type(first_name))
print('4', type('4'))

sentence = 'I love Python because it allows me to change anything in mind to a product. Is that not awesome?'
print(sentence)

print(len(first_name))
print(len(sentence))
print(sentence.split())
print(len(sentence.split()))
print(first_name.lower())
print(first_name.upper())
print(sentence.upper())
print(sentence.title())

# List -> a collection of different data types

names = ['Barck', 'Donald', 'Cliton']
print(names)
print(len(names))
whole_numbers = [0, 1, 2, 3, 4, 5, 6]
print(whole_numbers)
even_numbers = [0, 2, 4, 6, 8]
print(even_numbers)
print(len(even_numbers))

mix_of_data = [38, 3.14, 9.81, 1 + 1j , 'Donlad J. Trump', 'Mango', [0, 2, 4, 6]]
print(len(mix_of_data))

countries = ['Finland' ,'Sweden','Denmark', 'Nowray', 'Iceland','Estonia']
print(countries[0])
print(countries[0].upper())
print(countries[4].upper())

lastIndex = len(countries) - 1
print(countries[lastIndex].upper())
print(countries[-1].upper())
print(countries)
countries[0] = 'Suomi'
print(countries)
countries[3] = 'Greenland'
print(countries)
# List methods => append, extend, slicing

num1 = [1, 2, 3]
num2 = [4, 5, 6]
# contatenation
numbers = num1 + num2
print(numbers)
# Slicing
nordic_countries = countries[0:5]
last_country = countries[-1]
print(last_country)
print(nordic_countries)

scandic_countries = countries[1:5]
print(scandic_countries)

shopping_list = ['Sugar','Coffee','Milk','Meat','Mango','Potato','Tomato']
