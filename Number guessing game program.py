##Number guessing game

def magic_number_logic(num1, num2):
	return num1 == num2

def magic_number():
	number = 3
	return number

def magic_number_game():
	user_guess: int(input("Pick a number between 0 and 10 "))
	if magic_number_logic(user_guess, magic_number):
		print ("You win!")
	else:
		 print ("Guess Again!")

