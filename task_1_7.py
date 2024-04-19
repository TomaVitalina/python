# Aceasta este sarcina pentru lecția 7 legată de comentarii, continuarea liniilor și instrucțiuni condiționale.

# Creați o variabilă numită number și atribuiți-i o valoare întreagă.

# CODUL TĂU VINE MAI JOS:
number=7
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este pozitiv și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number>0 : 
    print("Numarul este pozitiv")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este par și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number % 2 ==0 :
    print("numarul este par")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă numărul este impar și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if number % 2 !=0 :
     print("numarul este impar")
# CODUL TĂU VINE MAI SUS:

# Creați o variabilă text și atribuiți-i un șir de caractere.

# CODUL TĂU VINE MAI JOS:
text = "Eu astazi sunt la Conferinta despre AI si BIG Data si programez in Python"
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if "Python" in text:
    print("Textul conține cuvântul 'Python'.")
else:
    print("Textul nu conține cuvântul 'Python'.")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Java" și afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if "Java" in text:
    print("Textul conține cuvântul 'Java'.")
else:
    print("Textul nu conține cuvântul 'Java'.")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și afișați un mesaj corespunzător.
# în cazul în care nu conține, verificați dacă conține cuvântul "Java" și afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
if "Python" in text:
    print("Textul conține cuvântul 'Python'.")
elif "Java" in text:
    print("Textul conține cuvântul 'Java'.")
else:
    print("Textul nu conține nici cuvântul 'Python' și nici cuvântul 'Java'.")
# CODUL TĂU VINE MAI SUS:

# Folosind o instrucțiune condițională, verificați dacă textul conține cuvântul "Python" și cuvântul "Java" și afișați un mesaj corespunzător.
# În cazul în care conține doar unul dintre ele, afișați un mesaj corespunzător.
# Dacă nu conține niciunul dintre ele, afișați un mesaj corespunzător.

# CODUL TĂU VINE MAI JOS:
text = "Acesta este un exemplu de text care conține Python și Java."

# Verifică dacă textul conține cuvântul "Python" și "Java"
if "Python" in text and "Java" in text:
    print("Textul conține atât cuvântul 'Python', cât și cuvântul 'Java'.")
elif "Python" in text:
    print("Textul conține doar cuvântul 'Python'.")
elif "Java" in text:
    print("Textul conține doar cuvântul 'Java'.")
else:
    print("Textul nu conține nici cuvântul 'Python' și nici cuvântul 'Java'.")
# CODUL TĂU VINE MAI SUS:

# Extrageți de la tastatură utilizând funcția input un număr de la 1 la 5 și atribuiți-l variabilei number.
# Folosiți o instrucțiune condițională pentru a printa un mesaj corespunzător în funcție de numărul introdus.
# pentru 1 - printați "Unu"
# pentru 2 - printați "Doi"
# pentru 3 - printați "Trei"
# pentru 4 - printați "Patru"
# pentru 5 - printați "Cinci"

# CODUL TĂU VINE MAI JOS:
number = input("Introduceți un număr de la 1 la 5: ")
if number == '1':
    print("Unu")
elif number == '2':
    print("Doi")
elif number == '3':
    print("Trei")
elif number == '4':
    print("Patru")
elif number == '5':
    print("Cinci")
else:
    print("Numărul introdus nu este între 1 și 5.")

# CODUL TĂU VINE MAI SUS:


