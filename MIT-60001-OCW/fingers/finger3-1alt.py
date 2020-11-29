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
