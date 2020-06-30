

from random import randint
from time import sleep


print ('Welcome to my dice game!')
print ('\n')
print ('\n')





class Dice(): 
  def __init__(self, size = 6):
    self.size = size
  
  def roll(self):
    roll = randint(1, self.size)
    return roll

   
class Player():
	def __init__(self):
		self.username = input('Whats Your name: ')
		print ('Welcome! ' + self.username)
	def guess_roll(self):
		guess = int(input('Take a guess: '))
		return guess
		

def run_game():
	
	print ('Lets start!')
	print ('\n')
	player_1 = Player()
	dice_1 = Dice()
	dice_2 = Dice()
	for turn in range(3):
		print ('It is Your ', turn + 1, ' guess')
		guess = player_1.guess_roll()
		sleep(1)
		print ('Rolling...')
		sleep(1)
		roll_both = dice_1.roll() + dice_2.roll()
		if guess == roll_both:
			print ('Well done You won!')
			break
		else:
			print ("Maybe next time mate!")
			print ('\n')
            
run_game()
