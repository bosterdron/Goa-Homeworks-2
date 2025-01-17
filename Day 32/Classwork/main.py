sum_func = lambda x, y: x + y
print(sum_func(3, 5))  # გამოსავალი იქნება 8

double_func = lambda x: x * 2
print(double_func(4))  # გამოსავალი იქნება 8


range_func = lambda start, end: list(range(start, end + 1))
print(range_func(1, 5))  # გამოსავალი იქნება [1, 2, 3, 4, 5]


numbers = [1, 2, 3, 4, 5]
tripled_numbers = list(map(lambda x: x * 3, numbers))
print(tripled_numbers)  # გამოსავალი იქნება [3, 6, 9, 12, 15]
