#Freddy Sena
#CS350Midterm Project

import random
from PIL import Image
import sys

#USING PILLOW LIBRARY
#Requirements file and Read Me file are need for the midterm !!!
#sudo apt-get install imagemagick  ONLY FOR UBUNTU!

def math(attempts, shiny):
	shiny = shiny + 1 #Adds in the shiny you wanted to get accurate results
	encounter_rate = attempts/shiny #Finds the average shiny encounter rate
	print "\n"
	print "Your average shiny encounter rate was 1 in", encounter_rate,"attempts."
	

def image(pokemon):
	if pokemon == 0:
	    Image.open('poochyena2.jpg').show()
	    Image.open('poochyena.jpg').show()

	elif pokemon == 1:
		Image.open('zigzagoon2.jpg').show()
		Image.open('zigzagoon.png').show()

	elif pokemon == 2:
		Image.open('wurmple2.jpg').show()
		Image.open('wurmple.png').show()

	elif pokemon == 3:
		Image.open('seedot.png').show()
		Image.open('seedot2.jpg').show()

	elif pokemon == 4:
		Image.open('ralts2.jpg').show()
		Image.open('ralts.png').show()
	else:
		Image.open('surskit.png').show()
		Image.open('surskit2.jpg').show()


def shinypkmn(pokemon):
	attempts = 0
	shiny = 0
	v = []
    
	pkmn = ['Poochyena', 'Zigzagoon', 'Wurmple', 'Seedot', 'Ralts', 'Surskit']

	while True:
		num = random.randint(0,8192)
		i = random.randint(0,100)

		if i > 85 and i < 101: #15% chance of finding a Poochyena
			poke = pkmn[0]

		elif i > 55 and i <= 85: #30% chance of finding a Zigzagoon
			poke = pkmn[1]

		elif i > 25 and i <= 55: #30% chance of finding a Wurmple
			poke = pkmn[2]

		elif i > 5 and i <= 25: #20% chance of finding a Seedot
			poke = pkmn[3]

		elif i > 1 and i <= 5: # 4% chance of finding a Ralts
			poke = pkmn[4]

		else: # 1% chance of finding a Surskit
			poke = pkmn[5]

		if num < 1 and poke == pkmn[pokemon]: #If num = 0 and poke is equal to the pokemon you selected, you encountered the shiny pokemon you were looking for. 
			print "You encountered a shiny", poke,"!\n"
			attempts += 1
			break

		elif num < 1: #If num = 0, you encountered a shiny pokemon (Not the shiny we're looking for, though.)
			print "You encountered a shiny", poke,"!\n"
			shiny += 1
			v.append(poke)

		else:
			print "You encountered a",poke,"!\n"
			attempts += 1


	print "\n"
	print "It took you",attempts,"encounters to find a shiny",pkmn[pokemon],"!\n"
	print "You also found", shiny, "other shiny Pokemon while searching for",pkmn[pokemon],"including:\n"

	for j in v:
		print "A shiny",j
	
	image(pokemon)
	math(attempts,shiny)


"""START OF PROGRAM"""
odds = float(1)/8192
pkmn1 = ['Poochyena', 'Zigzagoon', 'Wurmple', 'Seedot', 'Ralts', 'Surskit']
percentage = (15, 30, 30, 20, 4, 1) #Tuple of percentages



print"\n"
print "Welcome to the Shiny Pokemon simulation!\n"
print "There are 6 different Pokemon available to encounter on Route 102 in Pokemon Ruby, each with their own odds of encountering. This program simulates encounters until you find the shiny Pokemon you are looking for.\n"
print "The actual odds of finding a Shiny Pokemon are 1 in 8192, or", odds, "\n"
pokemon = int(raw_input("Please Enter in the Pokemon you would like to find shiny. \nPoochyena(0)  Zigzagoon(1)  Wurmple(2)  Seedot(3)  Ralts(4)  Surskit(5) \n"))

if pokemon not in range(0,6):
	sys.exit("You entered in a wrong number. Please try again.")

shiny_chance = float((float(percentage[pokemon])/100))/8192


print "There is a",percentage[pokemon],"% chance of encountering a", pkmn1[pokemon]
print "The odds of finding a shiny",pkmn1[pokemon],"are",shiny_chance
raw_input("Press enter to begin the simulation.\n")

shinypkmn(pokemon)


