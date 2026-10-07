empty_tuple = ()
fruits = ('banana', 'orange', 'mango', 'lemon')
sister_name = ('Trysha', 'Sameah')
brother_name = ('Matheo', 'Caleb')

print(f"Voici mes soeurs : {sister_name}")
print(f"Voici mes frères : {brother_name}")

siblings = sister_name + brother_name
print(f"Voici mes frères et soeurs : {siblings}")

print(f"J'ai {len(siblings)} frères et soeurs")

parents = ('Joseph', 'Maria')
family_members = siblings + parents
print(f"Voici ma famille au complet : {family_members}")

siblings = family_members[:-2]
parents = family_members[-2:]

print(f"Voici mes frères et soeurs : {siblings}")
print(f"Voici les parents : {parents}")

vegetables = ('carotte', 'brocoli', 'épinard')
animal_products = ('lait', 'fromage', 'œuf')

food_stuff_tp = fruits + vegetables + animal_products
print(f"food_stuff_tp : {food_stuff_tp}")

food_stuff_lt = list(food_stuff_tp)
print(f"food_stuff_lt : {food_stuff_lt}")

length = len(food_stuff_lt)
if length % 2 == 1:
    middle_item = food_stuff_lt[length // 2]
else:
    middle_item = food_stuff_lt[(length // 2) - 1 : (length // 2) + 1]

print(f"Élément(s) du milieu : {middle_item}")

first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

print(f"Les 3 premiers éléments : {first_three}")
print(f"Les 3 derniers éléments : {last_three}")

del food_stuff_tp

nordic_countries = ('Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden')

print("Estonia est-il un pays nordique ?", 'Estonia' in nordic_countries)
print("Iceland est-il un pays nordique ?", 'Iceland' in nordic_countries)