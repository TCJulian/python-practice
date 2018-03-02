import random

def main():
	pass

def password_maker(length, strong=True):
	if strong:
		strong_chars = [chr(i) for i in range(3, 126)]
		password_list = random.sample(strong_chars, length)
		password = " ".join(password_list)
	else:
		weak_words = ["raisin", "airplane", "tree", "goat", "bicycle", "Steelers", 
					  "barbie", "ant", "pal", "guy", "gal", "super", "special", 
					  "Texas", "cheese", "bacon", "egg", "lipstick", "tootpaste"]
		password_len = 0
		while password_len < length:
			random_word = random.sample(weak_words, 1)
			password_len += len(random_word[0])
			password = " ".join(random_word)
	return password		

if __name__ == "__main__":
	main()
