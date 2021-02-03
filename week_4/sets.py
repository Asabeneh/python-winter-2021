# empty set

empty_set = set()
print(empty_set)
print(type(empty_set))

set_1 = {0, 1, 2}
print(len(set_1))
set_1.add(3)
print(set_1)
fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.add('lime')
print(fruits)
for fruit in fruits:
    print(fruit.upper())

print('orange' in fruits)
print('apple' in fruits)
fruits.update(['Avocado','Papaya','Watermelon'])

print(fruits)
fruits.remove('Watermelon')
print(fruits)

if 'Apple' in fruits:
    fruits.remove('Apple')

fruits.discard('Papayasssss')

print(fruits)

countries = {'Finland','Sweden','Denmark','Norway','Iceland'}

countries_list = list(countries)

numbers = [2, 4, 5, 6, 7, 8, 2, 4, 4]
langauges = ['Finnish','Finnish','Finnish','Swedish','Swedish','Swedish','English','US']

numbers_set = set(numbers)
print(numbers_set)
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 contents are added to st1
print(st1)
st1.update({'item 10'})
print(st1)