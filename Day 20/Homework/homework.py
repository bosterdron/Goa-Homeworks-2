def manual_sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

def manual_len(items):
    count = 0
    for _ in items:
        count += 1
    return count

def manual_min(numbers):
    if not numbers:
        return None
    minimum = numbers[0]
    for number in numbers:
        if number < minimum:
            minimum = number
    return minimum
