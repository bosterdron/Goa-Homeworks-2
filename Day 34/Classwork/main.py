def manual_map(func, iterable):
    result = []
    for item in iterable:
        result.append(func(item))
    return result

nums = [1, 2, 3, 4]
squared = manual_map(lambda x: x**2, nums)
print(squared)

def manual_filter(func, iterable):
    result = []
    for item in iterable:
        if func(item):
            result.append(item)
    return result


nums = [1, 2, 3, 4, 5, 6]
even_nums = manual_filter(lambda x: x % 2 == 0, nums)
print(even_nums) 
