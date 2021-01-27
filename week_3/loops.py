

# For Loop

## What is loop -> Loop is the way to automate repetitive task
## It make us more product and allows to write a clean code



# Print all numbers from 0 to 100 x
# Print only even numbers 0 to 100 x
# Print only odd numbers 0 to 100 x
# sum all numbers 0 to 100
# Sum all even numbers 0 to 100
# sum all odd numbers 0 to 100

# for n in range (101):
#     print(n)

# for n in range (101):
#     if n % 2 == 0:
#         print(n)

# for n in range (0, 101, 2):
#     print(n)

# for i in range(101):
#     if i % 2 !=0:
#         print(f'${i} is an odd number')

# for i in range(1, 101, 2):
#     print(f'${i} is an odd number')


# total = 0

# for i in range(101):
#     total = total + i
# print(total)

# evens = 0
# for i in range(0, 101, 2):
#     evens = evens + i
# print(evens)

# odds = 0
# for i in range(1, 101, 2):
#     odds = odds + i
# print(odds)


# countries = ['Finland', 'Sweden', 'Estonia','Norway', 'Denmark']

# new_list = []
# for country in countries:
#     # print(country, country.upper(), len(country))
#     if(len(country) == 6):
#         new_list.append(country)

# print(new_list)

# ['Sweden', 'Norway']



# new_list = []
# for country in countries:
#     # print(country, country.upper(), len(country))
#     if 'land' in country:
#         new_list.append(country)

# print(new_list)

# for i in range(10, 0, -2):
#     print(i)



# for i in range (6):
#     print(i)

# # While loop
# print('While loop goes after here')
# i = 0
# while i < 6:
#     print(i)
#     i = i + 1

# print('Another example')
# i = 5
# while i >= 0:
#     print(i)
#     i = i - 1

# from countries import countries

# countries_with_land = []
# countries_without_land = []

# for c in countries:
#     # print([c, c.upper(), c.upper()[0:3],len(c)])
#     if 'land' in c:
#         countries_with_land.append(c)
#     else:
#         countries_without_land.append(c)


## Filter out countries contain land
## Filter out countries without a land 
# print(countries_with_land)
# print(countries_without_land)



numbers = [1, 4, 2, 5, 8, 7]
# Break => to interupt the execution of the loop

# for n in numbers:
#     print(n)
#     if n == 5:
#         break

for n in numbers:
    if n == 5:
        continue   
    print(n)
   
        
  


    