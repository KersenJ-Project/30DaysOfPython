import re

txt = 'I love to teach python and javaScript'
# Retourne un objet avec span et match
match = re.match('I love to teach', txt, re.I)
print(match)