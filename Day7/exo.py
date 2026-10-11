it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM'}

print("1. Longueur de it_companies:", len(it_companies))

it_companies.add('Twitter')
print("2. Après ajout de 'Twitter':", it_companies)

it_companies.update(['Amazon', 'Oracle', 'Netflix'])
print("3. Après ajout multiple:", it_companies)

it_companies.remove('Facebook')
print("4. Après suppression de 'Facebook':", it_companies)

# 5. Différence entre remove et discard
# - remove() lève une erreur (KeyError) si l'élément n'existe pas.
# - discard() ne fait rien et n'émet pas d'erreur si l'élément est absent.


A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

joiture_ab = A.union(B)
print("1. Union de A et B:", joiture_ab)

intersection_ab = A.intersection(B)
print("2. Intersection de A et B:", intersection_ab)

est_sous_ensemble = A.issubset(B)
print("3. A est-il un sous-ensemble de B ?", est_sous_ensemble)

sont_disjoints = A.isdisjoint(B)
print("4. A et B sont-ils disjoints ?", sont_disjoints)

ab = A.union(B)
ba = B.union(A)
print("5. A union B:", ab, "| B union A:", ba)

diff_symetrique = A.symmetric_difference(B)
print("6. Différence symétrique (A ^ B):", diff_symetrique)

del A
del B
print("7. Les ensembles A et B ont été supprimés.")


# 1. Convertissez les âges en un ensemble et comparez la longueur
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages_set = set(ages)
print("Longueur de la liste:", len(ages))
print("Longueur de l'ensemble:", len(ages_set))
print("   -> La liste est plus grande car elle conserve les doublons.")

# 2. Expliquez la différence entre les types de données : chaîne, liste, tuple, ensemble
# - Chaîne (str) : Séquence immuable de caractères.
# - Liste (list) : Séquence ordonnée et muable, autorise les doublons.
# - Tuple (tuple) : Séquence ordonnée et immuable.
# - Ensemble (set) : Collection non ordonnée, muable et sans doublons.

# 3. Mots uniques dans la phrase
phrase = "I am a teacher and I love to inspire and teach people."

phrase_propre = phrase.replace(".", "")
mots_liste = phrase_propre.split()
mots_uniques = set(mots_liste)

print("Phrase d'origine:", phrase)
print("Mots uniques trouvés:", mots_uniques)
print("Nombre de mots uniques:", len(mots_uniques))