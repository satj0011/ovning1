# Utg� fr�n Implementationen av DirectedList  Ladda ner DirectedListi modulen Datatyper.
# DirectedList beh�ver �ven filen OneCell
# Skriv ut resultat av varje �tg�rd, s� att du ser vad som h�nder.
# Importera r�tt modul

from DirectedList import DirectedList
from OneCell import OneCell
from random import randint

# skapa en tom lista
# testa om listan �r tom (skriv ut resultatet)
directed_list = DirectedList()
is_empty1 = directed_list.isempty()
print("Uppgift 1: Är den tom? - ", is_empty1)

# l�gg in 10 slumpm�ssiga heltal i intervallet [-100, 100]
# testa igen om listan �r tom
# skriv ut listans v�rden
# Sätt in för varje position

curren_pos = directed_list.first()
for i in range(10):
    # Talet som ska in
    random_integer = randint(-100, 100)
    current_pos = directed_list.insert(position=curren_pos, obj=random_integer)

is_empty2 = directed_list.isempty()
print("Uppgift2: Är den tom efter 10 insättningar av slumpmässiga värden mellan [-100,100] - ", is_empty2)

# ta fram listans sista v�rde
# Börja på första positionen, för att sedan iterera igenom listan tills dess att DirectedList.isEnd Returnerar True
position = directed_list.first()
print(directed_list.isEnd(position))
while not directed_list.isEnd(position=position):
    # Räkna upp index med 1, så att
    print("Nuvarande Position i Listan: ", position.inspectLink())
    position = directed_list.next(position)

last_position_value = position.inspectValue()
print("Sista värdet i listan: ", last_position_value)

# summera v�rdena i listan
sum_of_values = 0
position = directed_list.first()
while not directed_list.isEnd(position):
    sum_of_values += directed_list.inspect(position)
    position = directed_list.next(position)
print("Sumering av värden från listan: ", sum_of_values)

# anv�nd det v�rde du nu vet �r det sista och unders�k om det finns i listan
# testa ocks� med ett slumpm�ssigt v�rde
position = directed_list.first()
random_number = randint(-100, 100)
while not directed_list.isEnd(position):
    if last_position_value is directed_list.inspect(position):
        print("Last value in list - {} is in list position {} where last index returns {}".format(last_position_value,
                                                                                                  position,
                                                                                                  directed_list.inspect(
                                                                                                      position)))

    if random_number is directed_list.inspect(position):
        print("random number {} is in list position {} where last index returns {}".format(random_number, position,
                                                                                           directed_list.inspect(
                                                                                               position)))
    # TODO: Utan Denna så blir det en oändlig Loop. Fundera över varför
    position = directed_list.next(position)

# skriv en funktion printDL(list) som skriver ut en Directedlist


def function_that_writes_full_list(in_list: DirectedList):
    position = in_list.first()
    list_with_values = []
    while not directed_list.isEnd(position):
        list_with_values.append(directed_list.inspect(position))
        position = directed_list.next(position)
    print("DIRECTED LIST: ", list_with_values)

function_that_writes_full_list(directed_list)
"""
    Vi startar så här :D och reservation för slarvfel 
"""

# multiplicera alla v�rden i listan med 10, och skriv ut den nya listan med din printDL-funktion
# tips Directedlist har ingen funktion som s�tter ett v�rde i ett givet element, du m�ste i praktiken ta bort det gamla elementet och s�tta in ett nytt
# skriv en funktion lengthDL(list)  som returnerar antalet element i en Directedlist
