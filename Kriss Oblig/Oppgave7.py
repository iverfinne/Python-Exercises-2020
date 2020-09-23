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