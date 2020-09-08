print('==================================================================')
print('				 Rock Paper Scissor Games')
print('==================================================================')

from random import randint 

choice = ["Rock", "Paper", "Scissor", 'Lizard', 'Spock']
computer = choice[randint(0,2)]
player = ""

print(""" Choose One:
1. Rock
2. Paper
3. Scissor
4. Lizard
5. Spock
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
				if computer == "Scissor" or computer == "Lizard":
					print('You win because Rock crushes',computer,'!')				   
				else:				  
					print('Computer wins!')
			elif player == 2:
				print('Player wants Paper')				
				if computer == "Spock" or computer == "Lizard": 
					print('You win because Paper wins',computer,'!')		   
				else:				  
					print('Computer wins!')
			elif player == 3:
				print('Player wants Scissor')				
				if computer == "Paper" or computer == "Lizard":				  
					print('You win because Scissor cuts',computer,'!') 
				else: 
					print('Computer wins!')
			elif player == 4:
				print('Player wants Lizard')				
				if computer == "Spock" or computer == "Paper":				  
					print('You win because Lizard beats',computer,'!') 
				else: 
					print('Computer wins!')
			elif player == 5:
				print('Player wants Spock')				
				if computer == "Rock" or computer == "Scissor":				  
					print('You win because Spock evaporate' ,computer,'!') 
				else: 
					print('Computer wins!')                                         
			else:
				print('Something else')

	except Exception as e: 
		print("Error. Try again.")
		print(e)
		

if __name__ == "__main__":
	player = False
	play()