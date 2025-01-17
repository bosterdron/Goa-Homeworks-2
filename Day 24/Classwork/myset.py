# Set მაგალითი
my_set = {1, 2, 3}

# add() მეთოდი
my_set.add(4)
print(my_set)  # {1, 2, 3, 4}

# remove() მეთოდი
my_set.remove(2)
print(my_set)  # {1, 3, 4}

# remove() შეუძლია გამოიწვიოს შეცდომა თუ ელემენტი არ არის სეტში
# my_set.remove(5)  # ValueError: 5 is not in set
