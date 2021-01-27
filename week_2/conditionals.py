# Conditionals 
# 17:30 => I will be in Python lesson

a = int(input('Enter a number: '))

if a > 0:
    print(f'{a} is positive number')
elif a == 0:
    print(f'{a} is zero')
elif a < 0:
    print(f'{a} is a negative number')
else:
    print(f'{a} is not  a number')

country = 'FinLanD'
print(country)
print(len(country))
print(country.lower())
print(country.upper())
print(country.title())


weather = input('Enter the weather: ').lower()

if weather == 'sunny':
    print('You can go out freely, the day seems very sunny')
elif weather == 'rainy':
      print('Please take an umberella or a raincoat')
elif weather =='cloudy':
    print('The weather todays is foggy, cloudy and gloomy and it may rain')
else:
    print('No one knows the weather of today')