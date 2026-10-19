import string
import random

def random_hexa_colors():
    characters = string.ascii_lowercase[:6] + string.digits
    hexa_colors = ""

    for i in range(6):
        hexa_colors += random.choice(characters)
    
    print(f'#{hexa_colors}')

random_hexa_colors()