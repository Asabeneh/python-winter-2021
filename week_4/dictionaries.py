# dictionary is a collection of  key value 
empty_dct = {} # dict()
empty_dct_2 = dict()
from pprint import pprint

print(len(empty_dct))

country = {
    'name':'Finland',
    'city':'Helsinki',
    'population':60000000,
    'languages':['Suomi','Swedish','Sami'],
    'universities':['HU','Aalto U','...']
}
country['number_lakes'] = 188000

print('The length of the country', len(country))
print('The name of the country', country['name'])
print('The city of the country', country['city'])
print('The population of the country', country['population'])
print('The languages', len(country['languages']))
print(country)

country['languages'].append('Russia')
country['population'] = 5700000
pprint(country)
country.pop('number_lakes')
pprint(country)

person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
    }

print(len(person))
print(person['first_name'])
person['nationality'] = 'Ethiopian'

if 'nationality' in person:
    print(person['nationality'])

print(person.get('first_name'))
print(person.get('nationality'))

items = list(person.items())
pprint(items)
for key, value in items:
    print(key, value)


keys = list(person.keys())
print(keys)
values = list(person.values())
print(values)