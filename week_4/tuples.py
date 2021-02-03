# Tuples are immutables, non-modifiable
tp = tuple()
print(tp)
print(len(tp))
numbers = (3, 3, 1, 3, 2, 3)
print(numbers)
print(len(numbers))
print(numbers.count(3))

countries = ('Finland','Sweden','Denmark','Norway','Iceland', 'Estonia','Russia')
nordic_countries = countries[0:5]
print(nordic_countries)
non_nordic_countries = countries[-2:]
print(non_nordic_countries)

countries_list = list(countries)
print(countries_list)