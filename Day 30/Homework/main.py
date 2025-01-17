def sum_numbers(numbers):
    total = 0 
    for num in numbers:
        if isinstance(num, (int, float)):
            total += num
        elif num.isdigit():
            total += int(num)
        else:
            total += 0
    return total


numbers = [10, "10", 5, "20", "abc"]
result = sum_numbers(numbers)
print(result)

# ინიციალიზაცია
a = "10"  # სტრიქონი
b = 5      # მთელი რიცხვი

# მცდელობა, განვახორციელოთ დაყოფა
try:
    result = a / b
except TypeError:
    print("შეცდომა ტიპებში! ვერ გააკეთებთ სტრიქონის დაყოფას რიცხვზე.")

# ინსტანცია
numbers = [1, 2, 3, 4, 5]

# მცდელობა, ვიპოვოთ ელემენტი ინდექსით
try:
    number = numbers[5]  # IndexError
except IndexError:
    print("ინდექსი გადადის დიაპაზონს!")

x = "abc"
y = 5

# მცდელობა, გადავაკეთოთ სტრიქონი რიცხვად და დავამატოთ
try:
    result = int(x) + y  # ValueError
except ValueError:
    print("არასწორი მნიშვნელობა. შეუძლებელია სტრიქონის გადაკეთება რიცხვად!")
