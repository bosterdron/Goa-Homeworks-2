numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda x: x ** 2, numbers))
print(squares) # we will get [1, 4, 9, 16, 25]


celsius = [0, 20, 30, 40]
fahrenheit = list(map(lambda c: (c * 9/5) + 32, celsius))
print(fahrenheit) # we will get [32.0, 68.0, 86.0, 104.0]

words = ["hello", "world", "python"]
capitalized = list(map(lambda w: w.capitalize(), words))
print(capitalized) # we will get ['Hello', 'World', 'Python']


# --------------------------- Filters ---------------------------------------------


numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens) # we will get [2, 4, 6, 8]

strings = ["cat", "house", "tree", "car"]
long_strings = list(filter(lambda s: len(s) > 4, strings))
print(long_strings) # we will get ['house']


numbers = [3, 9, 15, 22, 27, 30]
divisible_by_3 = list(filter(lambda x: x % 3 == 0, numbers))
print(divisible_by_3) # [3, 9, 15, 27, 30]