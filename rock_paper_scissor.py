print('==================================================================')
print('                 Rock Paper Scissor Game')
print('==================================================================')

from random import randint 

choice = ["Rock", "Paper", "Scissor"]
computer = choice[randint(0,2)]
player = ""

print(""" Choose One:
1. Rock
2. Paper
3. Scissor
""")

def play(): 
	global player
	try: 
		while player == False:
			player = int(input())
			print('Computer wants', computer) 
			if player == computer:
				print("Tie!")
			elif player == 1:
				print('Player wants Rock')
				if computer == "Paper": 
					print('Computer wins because Paper beats Rock!')
				else:                  
					print('You win because Rock beats Scissor!')
			elif player == 2:
				print('Player wants Paper')                
				if computer == "Scissor":                   
					print('Computer wins because Scissor beats Paper!')
				else: 
					print('You win because Rock beats Paper!')
			elif player == 3:
				print('Player wants Scissor')                
				if computer == "Rock":                   
					print('Computer wins because Rock beats Scissor!')
				else: 
					print('You win because Scissor beats Paper!') 
			else:
				print('Something else')

	except Exception as e: 
		print("Error. Try again.")
		print(e)
		

if __name__ == "__main__":
	player = False
	play()