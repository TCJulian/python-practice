from datetime import datetime

def main():
    name = get_name()
    age = get_age()
    count = get_message_count()

    answer(name, age, count)

def get_name():
    name = str(input('Welcome! What is your first name? '))
    return name

def get_age():
    while True:
        try:
            age = -1
            while age < 0:
                age = int(input('How old are you? '))
                return age
        except ValueError:
            print("That is not a valid number. Try again.")

def get_message_count():
    while True:
        try:
            count = int(input('Number of messages: '))
            return count
        except ValueError:
            print("That is not a valid number. Try again.")

def answer(name, age, count):
    age_difference = 100 - age
    current = datetime.now()
    answer = current.year + age_difference

    for i in range(count):
        print('{}, you will be 100 years old in the year {}.'.format(name, answer))

if __name__ == '__main__':
    main()
