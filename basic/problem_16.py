# -------------------------------------------------------------------
#
# Exercise from: http://www.practicepython.org/exercise/2014/05/28/16-password-generator.html
#
# Objective: 
# 1. Write a password generator in Python. Be creative with how you generate passwords - 
# 		strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. 
# 		The passwords should be random, generating a new password every time the user asks for a new password. 
# 		Include your code in a main method.
# 2. Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
#
# -------------------------------------------------------------------

import random

def main():
	random.seed() # Set seed for teting purposes
	while True:
		try:
			length = int(input("How long does the password need to be? Please input an integer.\n"))
			break
		except ValueError:
			print("Your input is not an integer. Please try again.")

	strength = input("Do you want a strong password? Please input 'yes' or 'no'.\n")

	while True:
		if strength == "yes":
			password = password_maker(length)
		else:
			password = password_maker(length, strong=False)
		print("Your password is '{}'.".format(password))

		reply = input("Would you like a different password? Please input 'yes' or 'no'.\n")
		if reply == 'no':
			break

def password_maker(length, strong=True):
	if strong:
		strong_chars = [chr(i) for i in range(33, 126)]
		password_list = random.sample(strong_chars, length)
		password = "".join(password_list)
	else:
		weak_words = ["raisin", "airplane", "tree", "goat", "bicycle", "Steelers",
					  "barbie", "ant", "pal", "guy", "gal", "super", "special",
					  "Texas", "cheese", "bacon", "egg", "lipstick", "tootpaste"]
		password_len = 0
		password = ""
		while password_len < length:
			random_word = random.sample(weak_words, 1)
			password_len += len(random_word[0])
			password += random_word[0]
	return password

if __name__ == "__main__":
	main()
