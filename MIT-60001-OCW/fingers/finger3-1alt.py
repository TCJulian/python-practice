### Finger 3-1 ###
# Write a program that asks the user to enter an integer and
# prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal
# to the integer entered by the user. If no such pair of integers exists, it should
# print a message to that effect.

i = int(input("Enter an integer: "))

pairs = 0

for pwer in range(1, 6):
    root = 0
    while root**pwer < i:
        root += 1
    if root**pwer == i:
        print(f"{root} to the {pwer} power equals {i}")
        pairs += 1

if pairs == 0:
    print("No pair of integers exist.")
