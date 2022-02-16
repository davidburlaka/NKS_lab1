data = [647, 1948, 1204, 1757, 16, 0, 2279, 353, 450, 660, 950, 1210, 114, 1017, 1595, 370,
        32, 1725, 327, 209, 121, 1427, 1324, 293, 602, 606, 1057, 1586, 393, 2835, 12, 866,
        353, 55, 47, 1586, 149, 604, 586, 671, 726, 1024, 224, 998, 99, 300, 781, 232, 239, 312,
        47, 312, 1813, 257, 1602, 2422, 247, 240, 2255, 28, 694, 1657, 102, 353, 3195, 141,
        1980, 143, 440, 1974, 472, 169, 358, 1207, 824, 30, 39, 2167, 1761, 696, 1384, 1656,
        73, 184, 224, 873, 1117, 2667, 107, 2278, 246, 484, 1408, 1873, 1864, 1399, 331, 1764, 326, 12
        ]
# data = [
#     644, 1216, 2352, 1386, 1280, 903, 607, 2068, 4467, 835, 313, 555, 307, 508, 1386, 2895, 583, 292, 5159, 1107,
#     181, 18, 1247, 125, 1452, 4211, 890, 659, 1602, 2425, 214, 68, 21, 1762, 1118, 45, 1803, 1187, 2154, 19, 1122,
#     278, 1622, 702, 1396, 694, 45, 1739, 3483, 1334, 1852, 96, 173, 7443, 901, 2222, 4465, 18, 1968, 1426, 1424,
#     1146, 435, 1390, 246, 578, 281, 455, 609, 854, 436, 1762, 444, 466, 1934, 681, 4539, 164, 295, 1644, 711, 245,
#     740, 18, 474, 623, 462, 605, 187, 106, 793, 92, 296, 226, 63, 246, 446, 2234, 2491, 315
# ]
T = 0.84
Time = 2748
Time_intensity = 2308


def get_average(data: list):
    sum = 0
    for elem in data:
        sum += elem
    return sum / len(data)


average = get_average(data)

print(f'Середнэ значення вибірки - {average}')
print('#' * 50)
sorted_data = sorted(data)
max_data = sorted_data[-1]
h = max_data / 10
intervals = [x * max_data / 10 for x in range(11)]

for i in range(0, 10):
    print(f'{i + 1}-й інтервал від {intervals[i]} до {intervals[i + 1]}')

lst_with_f = []

for i in range(10):
    count = 0
    for elem in sorted_data:
        if intervals[i] <= elem < intervals[i + 1]:
            count += 1
        elif elem >= intervals[i + 1]:
            continue

    lst_with_f.append(count / (max_data / 10 * len(data)))

print('#' * 50)

for i in range(10):
    print(f'для {i + 1} інтервалу f{i + 1} = {lst_with_f[i]}')


def find_p(intervals, h, lst_with_f, time):
    if time == 0:
        return 1
    count = 0
    for index in range(1, len(intervals)):
        if intervals[index] < time:
            count += 1
        elif time < intervals[index]:
            break

    p = 1
    for index in range(count):
        p -= lst_with_f[index] * h

    p -= lst_with_f[count] * (time - h * count)

    return p


print('#' * 50)
lst_with_p = []
for index in range(len(intervals)):
    lst_with_p.append(find_p(intervals, h, lst_with_f, intervals[index]))
    print(f'Для {index} P({intervals[index]})={lst_with_p[index]}')


def d(start, stop, p, time):
    return (p[stop] - time) / (p[stop] - p[start])


def find_f(h, p, time):
    start = 0
    stop = 1
    for index in range(len(p)):
        if index + 1 < len(p):
            if p[index] > time > p[index + 1]:
                start, stop = index, index + 1
    return h - h * d(start, stop, lst_with_p, time)


print('#' * 50)
print(f"Відсотковий наробіток на відмову: {find_f(h, lst_with_p, T)}")
print('#' * 50)
count = 0
count_intensity = 0
for elem in intervals:
    if elem < Time:
        count += 1
    if elem < Time_intensity:
        count_intensity += 1

P = 1
P_intensity = 1
for index in range(count):
    if index != count - 1:
        P -= lst_with_f[index] * h
    else:
        P -= lst_with_f[index] * (Time - intervals[index])

for index in range(count_intensity):
    if index != count_intensity - 1:
        P_intensity -= lst_with_f[index] * h
    else:
        P_intensity -= lst_with_f[index] * (Time_intensity - intervals[index])

print(f"Ймовірність безвідмовної роботи на час {Time} становить: {P}")
print('#' * 50)
print(f"Інтенсивність відмов на час {Time_intensity} становить: {lst_with_f[count_intensity - 1] / P_intensity}")


