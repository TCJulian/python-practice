### Finger 2-4 ###
# Write a program that asks the user to input 10 integers, and
# then prints the largest odd number that was entered. If no odd number was
# entered, it should print a message to that effect.

numbers = 10

iterstep = 0
max_odd = None

while iterstep < numbers:
    x = int(input(f"{iterstep+1}. Enter an integer: "))
    if x%2 != 0:
        if not max_odd or x > max_odd:
            max_odd = x
    iterstep += 1
    
if max_odd:
    print(f"The largest odd number is {max_odd}.")
else:
    print("There were no odd numbers.")
