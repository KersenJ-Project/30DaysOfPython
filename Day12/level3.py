import random


def shuffle_list(my_list):
    shuffled_list = my_list.copy()
    random.shuffle(shuffled_list)

    return shuffled_list


def unique_random_numbers():
    numbers = []

    while len(numbers) < 7:
        number = random.randint(0, 9)

        if number not in numbers:
            numbers.append(number)

    return numbers


# Tests
print(shuffle_list([1, 2, 3, 4, 5]))
print(unique_random_numbers())