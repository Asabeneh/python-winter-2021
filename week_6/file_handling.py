
import os
import socket
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
    return f'{day}/{month}/{year} {hours}:{minutes}'

skills = ['Python','JavaScript','Pandas','sklear']

with open('./files/example.txt', 'a') as f:
    for skill in skills:
        f.write(f'\n {socket.gethostname()} {display_day_time()}Every body want to know {skill}.')


# print(dir(f))
# print(os.path)
# os.remove('./files/sample.txt')
# print(dir(os))

print(socket.gethostname())
