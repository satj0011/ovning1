#Utg� fr�n Implementationen av DirectedList  Ladda ner DirectedListi modulen Datatyper.
#DirectedList beh�ver �ven filen OneCell
#Skriv ut resultat av varje �tg�rd, s� att du ser vad som h�nder.
#Importera r�tt modul
from DirectedList import DirectedList
from OneCell import OneCell
from random import randint


#skapa en tom lista
#testa om listan �r tom (skriv ut resultatet)

lista = DirectedList.__init__
print(lista)



#l�gg in 10 slumpm�ssiga heltal i intervallet [-100, 100]
#testa igen om listan �r tom
#skriv ut listans v�rden

for i in range(10):
    value = randint(-100,100)
    DirectedList.insert(lista,i,value)
    
#ta fram listans sista v�rde
lastnumber = (lista[-1])
print("\n\n Last number of the list is " +str(lastnumber))

#summera v�rdena i listan
listsum=sum(lista)
print("\n\n Sum of list = " +str(listsum))



#anv�nd det v�rde du nu vet �r det sista och unders�k om det finns i listan
#testa ocks� med ett slumpm�ssigt v�rde

#skriv en funktion printDL(list) som skriver ut en Directedlist
#multiplicera alla v�rden i listan med 10, och skriv ut den nya listan med din printDL-funktion
#tips Directedlist har ingen funktion som s�tter ett v�rde i ett givet element, du m�ste i praktiken ta bort det gamla elementet och s�tta in ett nytt
#skriv en funktion lengthDL(list)  som returnerar antalet element i en Directedlist 