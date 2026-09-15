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
def average(values: dict[str, float]):
    grade = 0
    for value in values:
        grade += values[value]
    average_grade = grade / len(values)
    return average_grade


# Variabele maken voor iedere klas
studenten_eerste_klas = {
 "Anna": 7.5,
 "Funda": 6.9,
 "Chen": 8.2,
}
studenten_tweede_klas = {
 "Mohammed": 6.9,
 "Karin": 7.2,
 "Thomas": 8.2,
}
studenten_derde_klas = {
 "Lisa": 7.3,
 "Connor": 4.9,
 "Pete": 8.9,
}

# Geef deze variabelen de waarden van het gemiddelde van die klas (gebruik functie)
average_eerste_klas = average(studenten_eerste_klas)
average_tweede_klas = average(studenten_tweede_klas)
average_derde_klas = average(studenten_derde_klas)

# Toon deze in de terminal
print(average_eerste_klas)
print(average_tweede_klas)
print(average_derde_klas)

# Sla de gemiddelden op in een nieuwe dictionary
averages_dict = {
    "Klas 1": average_eerste_klas,
    "Klas 2": average_tweede_klas,
    "Klas 3": average_derde_klas
}

# Toon het gemiddelde van alle klassen
# Toon deze in de terminal
print(average(averages_dict))

