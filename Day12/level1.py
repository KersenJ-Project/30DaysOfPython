import random
import string


def random_hexa_colors():
    characters = string.ascii_lowercase[:6] + string.digits
    hexa_colors = "#"

    for i in range(6):
        hexa_colors += random.choice(characters)

    return hexa_colors


def rgb_color_gen():
    color1 = random.randint(0, 255)
    color2 = random.randint(0, 255)
    color3 = random.randint(0, 255)

    return f'rgb({color1}, {color2}, {color3})'


def list_of_hexa_colors(nb_colors):
    colors = []

    for i in range(nb_colors):
        colors.append(random_hexa_colors())

    return colors


def list_of_rgb_colors(nb_colors):
    colors = []

    for i in range(nb_colors):
        colors.append(rgb_color_gen())

    return colors


def generate_colors(color_type, nb_colors):
    if color_type == "hexa":
        return list_of_hexa_colors(nb_colors)

    elif color_type == "rgb":
        return list_of_rgb_colors(nb_colors)


print(generate_colors("hexa", 3))
print(generate_colors("hexa", 1))

print(generate_colors("rgb", 3))
print(generate_colors("rgb", 1))