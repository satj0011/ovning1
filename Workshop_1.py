#Utgå från Implementationen av DirectedList  Ladda ner DirectedListi modulen Datatyper.
#DirectedList behöver även filen OneCell
#Skriv ut resultat av varje åtgärd, så att du ser vad som händer.
#Importera rätt modul
from DirectedList import DirectedList
from OneCell import OneCell
from random import randint


#skapa en tom lista
#testa om listan är tom (skriv ut resultatet)

lista = DirectedList.__init__
print(lista)



#lägg in 10 slumpmässiga heltal i intervallet [-100, 100]
#testa igen om listan är tom
#skriv ut listans värden

for i in range(10):
    value = randint(-100,100)
    DirectedList.insert(lista,i,value)
    
#ta fram listans sista värde
lastnumber = (lista[-1])
print("\n\n Last number of the list is " +str(lastnumber))

#summera värdena i listan
listsum=sum(lista)
print("\n\n Sum of list = " +str(listsum))



#använd det värde du nu vet är det sista och undersök om det finns i listan
#testa också med ett slumpmässigt värde

#skriv en funktion printDL(list) som skriver ut en Directedlist
#multiplicera alla värden i listan med 10, och skriv ut den nya listan med din printDL-funktion
#tips Directedlist har ingen funktion som sätter ett värde i ett givet element, du måste i praktiken ta bort det gamla elementet och sätta in ett nytt
#skriv en funktion lengthDL(list)  som returnerar antalet element i en Directedlist 