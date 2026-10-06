empty_list = []

print(empty_list)

numbers = [10, 20, 30, 40, 50, 60, 70]

print(numbers)

print(len(numbers))

print("First item:", numbers[0])
print("Middle item:", numbers[len(numbers) // 2])
print("Last item:", numbers[-1])

mixed_data_types = [
    "Nyle",
    18,
    1.86,
    False,
    "Montreal, Quebec"
]

print(mixed_data_types)

it_companies = [
    "Facebook",
    "Google",
    "Microsoft",
    "Apple",
    "IBM",
    "Oracle",
    "Amazon"
]

print(it_companies)

print(it_companies)

print(len(it_companies))

print("First company:", it_companies[0])
print("Middle company:", it_companies[len(it_companies) // 2])
print("Last company:", it_companies[-1])

it_companies[0] = "Meta"

print(it_companies)

it_companies.append("Nvidia")

print(it_companies)

middle_index = len(it_companies) // 2

it_companies.insert(middle_index, "Intel")

print(it_companies)

it_companies[1] = it_companies[1].upper()

print(it_companies)

joined_companies = "#;  ".join(it_companies)

print(joined_companies)

print("Apple" in it_companies)


it_companies.sort()

print(it_companies)

it_companies.reverse()

print(it_companies)

first_three = it_companies[:3]

print(first_three)

last_three = it_companies[-3:]

print(last_three)


middle_index = len(it_companies) // 2

if len(it_companies) % 2 == 1:
    middle_companies = it_companies[middle_index:middle_index + 1]
else:
    middle_companies = it_companies[middle_index - 1:middle_index + 1]

print(middle_companies)

it_companies.pop(0)

print(it_companies)


middle_index = len(it_companies) // 2

if len(it_companies) % 2 == 1:
    it_companies.pop(middle_index)
else:
    it_companies.pop(middle_index)
    it_companies.pop(middle_index - 1)

print(it_companies)

it_companies.pop()

print(it_companies)

it_companies.clear()

print(it_companies)

del it_companies

front_end = ["HTML", "CSS", "JS", "React", "Redux"]

back_end = ["Node", "Express", "MongoDB"]

full_stack = front_end + back_end

print(full_stack)

full_stack = front_end + back_end

redux_index = full_stack.index("Redux")

full_stack.insert(redux_index + 1, "Python")
full_stack.insert(redux_index + 2, "SQL")

print(full_stack)