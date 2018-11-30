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
	elif user_guess  > magic_number:
		print("{} Isn't Not quite..try guessing a lower number!".format(user_guess))
	elif user_guess  < magic_number:
		print("{} Isn't Not quite..try guessing a higher number!".format(user_guess))



######################
#Notes for future dev plans:
#####################

#1
#consider adding logic to let the user know to guess higher or lower, depending on their response. 
# ^ DONE on 11/29/18
# could be refactored to give the greater than and less than instances their own method.
#e.g.
#User guesses too low
#def user_guess_low(num1, num2):
                #return num1 < num2
#user guesses too high
#def magic_number_high(num1, num2):
                #return num1 > num2


#2
