# Aceasta este a doua ta sarcină legată de seturi

# Creați un set gol numit `numbers_set`

# CODUL TĂU VINE MAI JOS:
numbers_set = set()
print("Setul gol:", numbers_set)
# CODUL TĂU VINE MAI SUS:

# Acum adăugați numerele de la 1 la 5 în setul `numbers_set`

# CODUL TĂU VINE MAI JOS:
numbers_set.add(1)
numbers_set.add(2)
numbers_set.add(3)
numbers_set.add(4)
numbers_set.add(5)
# CODUL TĂU VINE MAI SUS:

# Acum afișați setul `numbers_set`

# CODUL TĂU VINE MAI JOS:
print( numbers_set)
# CODUL TĂU VINE MAI SUS:

# Acum adăugați numărul 6 la setul `numbers_set`

# CODUL TĂU VINE MAI JOS:
numbers_set.add(6)
# CODUL TĂU VINE MAI SUS:

# Acum adaugă numerele de la 1 la 5 în setul `numbers_set` folosind metoda update()

# CODUL TĂU VINE MAI JOS:
numbers_set.update({1, 2, 3, 4, 5})
# CODUL TĂU VINE MAI SUS:

# Extrageți numărul 3 din setul `numbers_set`

# CODUL TĂU VINE MAI JOS:
numbers_set.remove(3)
# CODUL TĂU VINE MAI SUS:

# Ștergeți un număr inexistent din setul `numbers_set` fără a genera o eroare

# CODUL TĂU VINE MAI JOS:
numbers_set.discard(6)
# CODUL TĂU VINE MAI SUS:

# Verificați dacă numărul 3 există în setul `numbers_set`

# CODUL TĂU VINE MAI JOS:
print(3 in numbers_set)
# CODUL TĂU VINE MAI SUS:

# Verificați elementele comune din setul `numbers_set` și setul {4, 5, 6, 7}

# CODUL TĂU VINE MAI JOS:
print(numbers_set.intersection({4, 5, 6, 7}) )
# CODUL TĂU VINE MAI SUS:

# Verificați elementele diferite din setul `numbers_set` și setul {4, 5, 6, 7}

# CODUL TĂU VINE MAI JOS:
print(numbers_set.difference({4, 5, 6, 7}) )
# CODUL TĂU VINE MAI SUS:

# Verificați dacă setul `numbers_set` este un subset al setului {1, 2, 3, 4, 5, 6, 7}

# CODUL TĂU VINE MAI JOS:
print(numbers_set.issubset({1, 2, 3, 4, 5, 6, 7}))
# CODUL TĂU VINE MAI SUS:

# Verificați dacă setul {1, 2, 3, 4, 5, 6, 7} este un subset al setului `numbers_set`

# CODUL TĂU VINE MAI JOS:
print({1, 2, 3, 4, 5, 6, 7}.issubset(numbers_set))
# CODUL TĂU VINE MAI SUS:

# Verificați dacă setul `numbers_set` este un superset al setului {1, 2, 3, 4, 5, 6, 7}

# CODUL TĂU VINE MAI JOS:
print(numbers_set.issuperset({1, 2, 3, 4, 5, 6, 7}))
# CODUL TĂU VINE MAI SUS:

# Verificați dacă setul {1, 2, 3, 4, 5, 6, 7} este un superset al setului `numbers_set`

# CODUL TĂU VINE MAI JOS:
print({1, 2, 3, 4, 5, 6, 7}.issuperset(numbers_set))
# CODUL TĂU VINE MAI SUS:

# Afișați lungimea setului `numbers_set`

# CODUL TĂU VINE MAI JOS:
print(len(numbers_set))
# CODUL TĂU VINE MAI SUS:

# Ștergeți toate elementele din setul `numbers_set`

# CODUL TĂU VINE MAI JOS:
numbers_set.clear()
# CODUL TĂU VINE MAI SUS:

# Afișați setul `numbers_set` pentru a verifica dacă a fost șters

# CODUL TĂU VINE MAI JOS:
print(numbers_set)
# CODUL TĂU VINE MAI SUS:

# Asta a fost tot pentru a doua ta sarcină legată de seturi