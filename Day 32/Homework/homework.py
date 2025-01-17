numbers = [2, 4, 6, 8, 10]
doubled_numbers = list(map(lambda x: x * 2, numbers))
print(doubled_numbers)  # Output: [4, 8, 12, 16, 20]


names = ["Alice", "Bob", "Charlie"]
greeting_names = list(map(lambda name: "Hello, " + name, names))
print(greeting_names)  # Output: ['Hello, Alice', 'Hello, Bob', 'Hello, Charlie']

fruits = ["apple", "banana", "kiwi"]
fruit_lengths = list(map(len, fruits))
print(fruit_lengths)  # Output: [5, 6, 4]


numbers = [-5, 3, -2, 7, 0, 10]
positive_numbers = list(filter(lambda x: x > 0, numbers))
print(positive_numbers)  # Output: [3, 7, 10]


numbers = [-5, 3, -2, 7, 0, 10]
positive_numbers = list(filter(lambda x: x > 0, numbers))
print(positive_numbers)  # Output: [3, 7, 10]

words = ["pear", "apple", "peach", "grape"]
p_words = list(filter(lambda word: word.startswith('p'), words))
print(p_words)  # Output: ['pear', 'peach']


numbers = [10, 55, 42, 78, 65, 20]
greater_than_50 = list(filter(lambda x: x > 50, numbers))
print(greater_than_50)  # Output: [55, 78, 65]
