# dictionary
person_dct = {
    "name": "Asabeneh",
    "country": "Finland",
    "city": "Helsinki",
    "skills": ["JavaScrip", "React", "Python"],
    'natinality':'Ethiopian'
}

print(type(person_dct))

import json
#  person_json = '''{
#     "name": "Asabeneh",
#     "country": "Finland",
#     "city": "Helsinki",
#     "skills": ["JavaScrip", "React", "Python"],
#     'natinality':'Ethiopian'
# }'''

person_json = json.dumps(person_dct,indent=4)

with open('json_example.json', 'w', encoding='utf-8') as f:
    json.dump(person_dct, f, ensure_ascii=False, indent=4)
print(person_json)
print(type(person_json))
