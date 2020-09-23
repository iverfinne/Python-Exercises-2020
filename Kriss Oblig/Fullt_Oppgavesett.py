#Oppgave 1
animal = ["whale", "turtle", "swan", "fox"]
navn = ["Yun", "Johannes", "Iver", "Kristoffer"]

print(navn[0] + " is a " + animal[0])
print(navn[1] + " is a " + animal[1])
print(navn[2] + " is a " + animal[2])
print(navn[3] + " is a " + animal[3])

#Oppgave 2
res = [ animal[0], animal[-1] ]
print(res)
    
    #.sort sorterer listen alfabetisk, .reverse reverserer den
animal.sort(reverse=True)
print(animal)

#Oppgave 3
# -- A --

my_list = ["H", "I", "O", "F"]
my_string1 = "H:I:O:F"
my_string2 = "HIOF"

def listToString(s):  
    str1 = ""  
    for ele in my_list:  
        str1 += ele   
    return str1   

print(listToString(my_list))  

# -- B --

    #.split splitter elementene etter ":" det samme som i oppgaven over, men der splittes den av "" (altså mangelen på mellomrom)
def Convert(my_string1): 
    li = list(my_string1.split(":")) 
    return li 
print(Convert(my_string1)) 

# -- C --

res = []
res[:] = my_string2
print(str(res))

#Oppgave 4
    #loop / løkke sikter til "for" funksjonen
for i in range(5):
    print("Hello World")

    #alternativt bruker ein while for mer kontroll
i = 0
while i < 5:
    print("Hello World")
    i += 1

i = 0
while i < 5:
    print(str(i) + ". Hello World")
    i += 1

#Oppgave 5
    # liste med tall, range lager liste mellom to heltall
list1 = range(10, 25) 
num = 0
  
    # bruk av løkke
while(num < len(list1)): 
      
    # bruk av *modulus funksjonen: "Dersom man kan dele tallet på og det tallet er et hel tall: Print tallet"
    if num % 2 == 0: 
       print(list1[num], end = " ") 
      
    # denne funksjonen stopper at kalkulasjonen ikke looper for altid
    num += 1

#Oppgave 6
def MinÅrligeInnbetaling(beløp, årlig_rente, løpetid_år):
    n = løpetid_år
    r = (årlig_rente / 100)
    årlig_beløp = (r * beløp * ((1+r) ** n)) / (((1+r) ** n) - 1)
    return årlig_beløp

løpetid_år = int(7)
årlig_rente = float(0.06)
beløp = int(600000)

print('Årlig innbetaling i NOK: {}'.format(MinÅrligeInnbetaling(beløp, årlig_rente, 
løpetid_år)))

#Oppgave 7
import random
player_names = []

input_players = int(input('Hvor mange spillere? '))

for i in range(0,input_players):
  name = input('Skriv inn spillerens navn: ')
  name = name.upper()
  player_names.append(name)

score = 0
for i in player_names:
    piler = int(input("antall piler: "))
    for piler in range(piler):
        print(input("kast en pil? [Press enter]: "))
        n = random.randrange(0,50)
        print("du scorte: ", n) # placeholder for my turn function 
        score += n
    print(i, "din totalscore er: ", score)
print

#Oppgave 8
my_list = [[1, 0, 1, 0], [0, 1, 1, 0,], [0, 1, 1, 1], [0, 0, 0, 1]]

print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in my_list]))


#Oppgave 9

  
streng = []

for letter in 'Høgskolen i Østfold':
    streng.append(letter)

print(streng)