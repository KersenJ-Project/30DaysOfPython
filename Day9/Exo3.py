person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_married': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {'street': 'Space street', 'zipcode': '02210'},
}

if 'skills' in person:
    skills_list = person['skills']
    middle_index = len(skills_list) // 2
    print("1. Compétence du milieu :", skills_list[middle_index])

if 'skills' in person:
    has_python = 'Python' in person['skills']
    print("2. Possède la compétence 'Python' :", has_python)

skills_set = set(person.get('skills', []))

if skills_set == {'JavaScript', 'React'}:
    print('3. Il est développeur front-end')
elif {'React', 'Node', 'MongoDB'}.issubset(skills_set) and {
    'JavaScript',
    'Python',
}.issubset(skills_set):
    print('3. Il est développeur full-stack')
elif {'Node', 'Python', 'MongoDB'}.issubset(skills_set):
    print('3. Il est développeur back-end')
else:
    print('3. unknown title')

if person.get('is_married') and person.get('country') == 'Finland':
    print(
        f"4. {person['first_name']} {person['last_name']} lives in Finland. He is"
        ' married.'
    )