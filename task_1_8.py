# Aceasta este tema pentru lecția 8 legată de loops

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
lista=[]
for numar in range(1, 11): lista.append(numar)
print(lista)
# CODUL TĂU VINE MAI SUS:

# Folosind un for loop, parcurgeți lista creată și afișați numai numerele pare.

# CODUL TĂU VINE MAI JOS:
lista = list(range(1, 11))
print("Numerele pare din lista sunt:")
for numar in lista:
    if numar % 2 == 0:
        print(numar)
# CODUL TĂU VINE MAI SUS:

# Folosind un while loop, creați o variabilă 'i' inițializată cu 1 și incrementați-o până când ajunge la 5. Afișați valoarea 'i' la fiecare pas.

# CODUL TĂU VINE MAI JOS:
i = 1
while i <= 5:
    print("Valoarea lui 'i' este:", i)
    i += 1
# CODUL TĂU VINE MAI SUS:

# Creați un dicționar person cu cheile 'name', 'age' și 'city' și iterați prin dicționar afișând perechile de cheie-valoare.

# CODUL TĂU VINE MAI JOS:
person = {'name': 'John', 'age': 30, 'city': 'New York'}
for key, value in person.items():
    print(f"{key}: {value}")
# CODUL TĂU VINE MAI SUS:

# Utilizați un for loop pentru a itera printr-o listă de liste (matrice) și afișați fiecare element.

# CODUL TĂU VINE MAI JOS:
matrice = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for lista in matrice:
        for element in lista:
            print(element, end=" ")
            print()  
# CODUL TĂU VINE MAI SUS:

# Creați o secvență de numere folosind funcția range() și apoi iterați prin această secvență folosind un for loop pentru a afișa numerele.

# CODUL TĂU VINE MAI JOS:
secventa = range(1, 11) 
for numar in secventa:
    print(numar)
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția enumerate() pentru a itera printr-o listă și a afișa indexul fiecărui element alături de valoarea sa.

# CODUL TĂU VINE MAI JOS:
lista = ['1', '2', '3', '4', '5']
for index, valoare in enumerate(lista):
    print(f"Indexul: {index}, Valoarea: {valoare}")
# CODUL TĂU VINE MAI SUS:

# Folosiți funcția zip() pentru a itera simultan prin două liste și a afișa elementele corespunzătoare.

# CODUL TĂU VINE MAI JOS:
lista1 = ['a', 'b', 'c', 'd']
lista2 = [1, 2, 3, 4]
for elem1, elem2 in zip(lista1, lista2):
    print(f"Elementul din lista1: {elem1}, Elementul din lista2: {elem2}")
# CODUL TĂU VINE MAI SUS:

# Creați o listă de numere de la 1 la 10 folosind un for loop și funcția range().

# CODUL TĂU VINE MAI JOS:
lista=[]
for numar in range(1, 11): lista.append(numar)
print(lista)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while, dublează valorile listei până când primul element va deveni mai mare decât 50.

# CODUL TĂU VINE MAI JOS:
liste=[1,2]
while liste[0] <= 50:
     liste = [x * 2 for x in liste]
     print(liste)
# CODUL TĂU VINE MAI SUS:

# Generează și printează o listă cu toate numerele pătrat perfect din intervalul [1, 100].

# CODUL TĂU VINE MAI JOS:
patperf = []
for numar in range(1, 101):
    if numar ** 0.5 == int(numar ** 0.5):  
       patperf.append(numar)  
print("Patratele perfecte sunt:", patperf)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă for , printează tabla înmulțirii pentru numărul 7.

# CODUL TĂU VINE MAI JOS:
for numar in range(1, 11):
    rezultat = 7 * numar
    print(f"7 * {numar} = {rezultat}")
# CODUL TĂU VINE MAI SUS:

# Creează o listă de liste, unde fiecare sub-listă conține perechi (i, j) pentru i și j de la 1 la 5. Printează această listă de perechi.

# CODUL TĂU VINE MAI JOS:
lista_de_liste = [[(i, j) for j in range(1, 6)] for i in range(1, 6)]
for sub_lista in lista_de_liste:
    print(sub_lista)
# CODUL TĂU VINE MAI SUS:

# Parcurge lista de la punctul anterior și printează doar perechile unde i < j .

# CODUL TĂU VINE MAI JOS:
for sub_lista in lista_de_liste:
    for pereche in sub_lista:
        i, j = pereche
        if i < j:
            print(pereche)
# CODUL TĂU VINE MAI SUS:

# Folosind un buclă while , caută și printează prima valoare care este mai mare decât 10 dintr-o listă cu numere random creată de tine. Dacă nu există, printează "Nu există valori mai mari decât 10".

# CODUL TĂU VINE MAI JOS:
import random
lista_numere = [random.randint(1, 20) for _ in range(10)]  
index = 0
while index < len(lista_numere):
    if lista_numere[index] > 10:
        print( lista_numere[index])
        break 
    index += 1
else:
    print("Nu există valori mai mari decât 10 în lista.")
# CODUL TĂU VINE MAI SUS:

# Folosind loop-uri Creează un pătrat de stele ( * ) folosind bucle încadrate. Dimensiunea pătratului va fi citită de la utilizator.
# Exemplu pentru un pătrat de dimensiune 5:
# *****
# *****
# *****
# *****
# *****

# CODUL TĂU VINE MAI JOS:
a = int(input())
for i in range(a):  
    for j in range(a):  
        print("*", end=" ")  
    print()  
# CODUL TĂU VINE MAI SUS:

# Folosind for sau while loops realizați afișările de mai jos

# Afișarea 1:
# 1
# 12
# 123
# 1234
# 12345
# 123456

# CODUL TĂU VINE MAI JOS:
for i in range(1, 7):  
    for j in range(1, i + 1):  
        print(j, end="")  
    print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 2:

# 54321
# 5432
# 543
# 54
# 5

# CODUL TĂU VINE MAI JOS:
for i in range(6,0, -1):  
    for j in range(6, 6-i, -1):  
        print(j, end="")  
    print()
# CODUL TĂU VINE MAI SUS:

# Afișarea 3:

# abcdefg
# bcdefg
# cdefg
# defg
# efg
# fg
# g

# CODUL TĂU VINE MAI JOS:
for i in range(7):  
    for j in range(i, 7):
        print(chr(97 + j), end="")  
    print()  

# CODUL TĂU VINE MAI SUS:

# Afișarea 4:

# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+
# +-+-+-+-+-+-+-+-
# -+-+-+-+-+-+-+-+

# CODUL TĂU VINE MAI JOS:
for i in range(8):  
    for j in range(15):  
        if (i + j) % 2 == 0:
            print("+", end="")
        else:
            print("-", end="")
    print()  
# CODUL TĂU VINE MAI SUS:

# Afișarea 5:

# 3
# 3 9
# 3 9 27
# 3 9 27 81
# 3 9 27 81 243
# 9 27 81 243
# 27 81 243
# 81 243
# 243

# CODUL TĂU VINE MAI JOS:
for i in range(5):  
    for j in range(i + 1):  
        b = 3 ** (j + i)
        print(b, end=" ")
    print()  
for i in range(5):  
    for j in range(5 - i):  
        b= 3 ** (j + i + 1)
        print(b, end=" ")
    print()  
# CODUL TĂU VINE MAI SUS:

# Completați sarcinile de mai sus pentru a exersa lucrul cu buclele în Python.
