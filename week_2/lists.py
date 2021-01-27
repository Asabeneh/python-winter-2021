# List => is a collection of different or the same data types
empty_list = list() # or []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(numbers))

# Extracting values from list using the index

print(numbers[0])
print(numbers[1])
print(numbers[4])
lastIndex = len(numbers) - 1
print(numbers[lastIndex])
print(numbers[8])
print(numbers[-1])
print(numbers[-2])

# Modify
numbers[0] = 10
print(numbers)
numbers[5] = 600
print(numbers)

# Adding number from other side
numbers.append(1000)
print(numbers)
numbers.extend([200, 150,300])
print(numbers)
print(dir(numbers))
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)
numbers.sort(reverse = True)
print(numbers)

countries = ['Finland', 'Sweden', 'Estonia']

countries_2 = countries.copy()
print('lets the copy', countries_2)

# countries.insert(1, 'Norway')
# print(countries)

countries.pop()
countries.pop(1)
print(countries)

del countries[0]
print(countries)
print(countries_2)

nums = [1, 2, 4, 4, 4, 3, 1]
print(nums.count(4))


