import math

def evens_and_odds(number):
    odds = 0
    evens = 0

    for value in range(number + 1):
        if value % 2 == 0:
            evens += 1
        else:
            odds += 1

    print("The number of odds are", odds)
    print("The number of evens are", evens)


def factorial(number):
    if number < 0:
        return "Le nombre doit être positif ou nul."

    result = 1

    for value in range(1, number + 1):
        result = result * value

    return result


def is_empty(value):
    return len(value) == 0


def calculate_mean(numbers):
    if len(numbers) == 0:
        return None

    total = 0

    for number in numbers:
        total += number

    return total / len(numbers)


def calculate_median(numbers):
    if len(numbers) == 0:
        return None

    ordered = sorted(numbers)
    length = len(ordered)
    middle = length // 2

    if length % 2 == 1:
        return ordered[middle]

    return (ordered[middle - 1] + ordered[middle]) / 2


def calculate_mode(numbers):
    if len(numbers) == 0:
        return None

    most_frequent = numbers[0]
    highest_count = 0

    for number in numbers:
        count = 0

        for other_number in numbers:
            if number == other_number:
                count += 1

        if count > highest_count:
            highest_count = count
            most_frequent = number

    return most_frequent


def calculate_range(numbers):
    if len(numbers) == 0:
        return None

    smallest = numbers[0]
    largest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

        if number > largest:
            largest = number

    return largest - smallest


def calculate_variance(numbers):
    if len(numbers) == 0:
        return None

    mean = calculate_mean(numbers)
    total = 0

    for number in numbers:
        total += (number - mean) ** 2

    return total / len(numbers)


def calculate_std(numbers):
    variance = calculate_variance(numbers)

    if variance is None:
        return None

    return math.sqrt(variance)


def greet(name="Guest"):
    print("Hello,", name + "!")


def show_args(**kwargs):
    print("Received:", end=" ")

    first = True

    for name, value in kwargs.items():
        if not first:
            print(", ", end="")

        print(name + ": " + str(value), end="")
        first = False

    print()