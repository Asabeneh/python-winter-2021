# Time is an important physical quantity

def display_day_time ():
    from datetime import datetime
    # print(dir(datetime))
    current_time = datetime.now()
    print(type(current_time))
    day = current_time.day
    month = current_time.month
    year = current_time.year
    hours = current_time.hour
    minutes = current_time.minute

# print(current_time)
# print('Date: ', day, 'Month: ', month, 'year:', year, 'hours: ', hours, 'minuts: ', minutes )

# if minutes < 10:
#     minutes = '0' + str(minutes) 
# print(f'{day}/{month}/{year} {hours}:{minutes}')

time = current_time.strftime('%H:%M:%S')
print('The time now:', time)
print(current_time.strftime('%A, %B %Y %H:%M:%S'))

date_string = "Mon Dec, 2019"
time_obj = datetime.strptime(date_string, '%a %b, %Y')
print(type(time_obj))
print(time_obj)

from datetime import date, timedelta
d = date(2020, 1, 1)
print(d)
print(d.today())

challenge_started_date = date(year=2019, month=11, day=22)
today = date(year=2021, month=2, day=10)

time_elapsed = today - challenge_started_date
print(time_elapsed)

t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
print(dir(timedelta))