# Opdracht 1
# Functie die de volgende taken doet:
# - Vreemde tekens weghalen (!, ?, $)
# - Spaties weghalen aan begin en eind
# - Naam van de student als argument gebruiken
def clean_name(name):
    name = name.replace('!', '')
    name = name.replace('?', '')
    name = name.replace('$', '')
    name = name.strip()
    return name

# Loop over een lijst van studenten
studenten = [" Anna Pe!ter ", " Bilal Amrabat ? ", " $ Chen Fong "]

# Per student functie aanroepen om de string mooi te maken
for student in studenten:
    student = clean_name(student)
    print(student)

# Opdracht 2
# Functie die de gemiddelden berekent

# Variabele maken voor iedere klas
# Geef deze variabele de waarde van het gemiddelde van de klas (gebruik functie)
# Toon het gemiddelde van alle klassen
# Toon deze in de terminal