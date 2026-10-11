dog = {}

dog["name"] = "Rudy"
dog["color"] = "brown"
dog["breed"] = "Husky"
dog["legs"] = 4
dog["age"] = 5

print("1. Dictionnaire dog:", dog)

student = {
    "first_name" : "John",
    "last_name" : "Doe",
    "gender": "Male",
    "age" : 19,
    "marital_status" : "Single",
    "skills" : ["Python", "JavaScript", "HTML"],
    "country" : "USA",
    "city" : "New Jersey",
    "address" : "123 Main St"
}

print("2. Dictionnaire student:", student)

print("3. Longueur du dictionnaire student:", len(student))

print("4. Valeurs de skills:", student["skills"], " | Type de skills:", type(student["skills"]))

student["skills"].append("CSS")
student["skills"].append("React")
print("5. Dictionnaire student après ajout de skills:", student)

print("6. Clés du dictionnaire student:", student.keys())

print("7. Valeurs du dictionnaire student:", student.values())

print("8. Items du dictionnaire student:", student.items())

print("9. Suppression de la clé 'marital_status' du dictionnaire student:", student.pop("marital_status"))

del student

print("10. Dictionnaire student après suppression:", student) # Vas causer une erreur car le dictionnaire student a été supprimé