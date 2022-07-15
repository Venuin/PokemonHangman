from itertools import count
import random

HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

#Word bank of pokemons
words = ('bulbasaur ivysaur venusaur charmander charmeleon charizard squirtle wartortle blastoise caterpie metapod butterfree weedle kakuna beedrill pidgey pidgeotto pidgeot rattata raticate spearow fearow ekans arbok pikachu raichu sandshrew sandslash nidoran♀ nidorina nidoqueen nidoran♂ nidorino nidoking clefairy clefable vulpix ninetales jigglypuff wigglytuff zubat golbat oddish gloom vileplume paras parasect venonat venomoth diglett dugtrio meowth persian psyduck golduck mankey primeape growlithe arcanine poliwag poliwhirl poliwrath abra kadabra alakazam machop machoke machamp bellsprout weepinbell victreebel tentacool tentacruel geodude graveler golem ponyta rapidash slowpoke slowbro magnemite magneton farfetch doduo dodrio seel dewgong grimer muk shellder cloyster gastly haunter gengar onix drowzee hypno krabby kingler voltorb electrode exeggcute exeggutor cubone marowak hitmonlee hitmonchan lickitung koffing weezing rhyhorn rhydon chansey tangela kangaskhan horsea seadra goldeen seaking staryu starmie mr.mime scyther jynx electabuzz magmar pinsir tauros magikarp gyarados lapras ditto eevee vaporeon jolteon flareon porygon omanyte omastar kabuto kabutops aerodactyl snorlax articuno zapdos moltres dratini dragonair dragonite mewtwo mew ').split()



pokemon = random.choice(words)
correct = list()
incorrect = list()
lettercount = len(set(pokemon))
incorrectcount = 0

while(True):

  print(HANGMANPICS[incorrectcount])

  for x in range(len(pokemon)):
    if correct.count(pokemon[x]) > 0:
      print(pokemon[x], end=' ')
    else:  
      print('_ ', end=' ')

  if incorrectcount == 6:
    print('\nLOSE')
    print('Pokemon was', pokemon)
    break
  elif len(correct) == lettercount:
    print('\nWIN')
    break

  print('\nIncorrect predictions: ', incorrect)

  print('PREDICTION: ')
  prediction = input()[0]

  if pokemon.count(prediction) > 0:
    if correct.count(prediction) == 0:
      correct.append(prediction)
    else:
      print('This prediction was made.')
  else:
    if incorrect.count(prediction) == 0:
      incorrectcount += 1
      incorrect.append(prediction)
    else:
      print('This prediction was made.')
