##Number guessing game


#Here, I'm creating the logic that should be returned as "true" if the user guesses the right number.
def magic_number_logic(num1, num2):
	return num1 == num2

#Setting the magic number that the user is trying to guess. The above method will only return "true"  if this number is input buy the user.
def magic_number():
	number = 3
	return number

#This puts it all together. There is a user prompt and input and then an  If, else statement that will print a message back to them. 
def magic_number_game():
	user_guess: int(input("Pick a number between 0 and 10 "))
	if magic_number_logic(user_guess, magic_number):
		print ("You win!")
	else:
		 print ("Guess Again!")


#Notes for future dev plans:
#consider adding logic to let the user know to guess higher or lower, depending on their response. 
