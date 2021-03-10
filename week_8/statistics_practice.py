
# the age of my students

data = [19, 20, 22, 33, 45, 60, 25, 24, 40, 20, 22, 24, 26, 26, 28, 27, 24, 35, 40, 40, 24, 38, 40, 28, 23]

# mean, median, standard deviation, variance, range, mode

print(len(data))

def calculate_mean (lst):
    return sum(lst)/len(lst)

print(calculate_mean(data))

def calculate_std_dev (lst):
    n = len(lst)
    mean = calculate_mean(lst)
    st_dev = 0
    for l in lst:
        st_dev += (l - mean) ** 2

    st_dev = (st_dev/(n -1)) ** 0.5
    return st_dev

print(calculate_std_dev(data))

import statistics

print(statistics.mean(data))
print(statistics.stdev(data))

def calculate_range(lst):
    data_sorted = sorted(data)
    lowest = data_sorted[0]
    heighest = data_sorted[-1]
    return heighest - lowest

def calculate_median(lst):
    n = len(lst)
    median = None
    if n % 2 == 0:
        median = (lst[n/2] + lst[n/2 - 1])/2
    else:
        median = lst[int(n/2)] 
    return median

    
print(calculate_median(data))
print(statistics.median(data))

variance = calculate_std_dev(data) ** 2
print(variance)
print(statistics.variance(data))

def calculate_mode (lst):
    sorted_data = sorted(data)
    freq_table = {}
    for age in sorted_data:
        if age not in freq_table:
            freq_table[age] = 1
        else:
            freq_table[age] = freq_table[age] + 1
    freq_table = {k: v for k, v in sorted(
        freq_table.items(), key=lambda item: item[1])}
    print(freq_table.items())
    print('lets here', freq_table.keys()[-1])

print(statistics.mode(data))

# NumPy
















