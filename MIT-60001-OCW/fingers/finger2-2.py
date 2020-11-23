### Finger 2-2 ###
# Write a program that examines three variables—x, y, and z—
# and prints the largest odd number among them. If none of them are odd, it
# should print a message to that effect.

x = int(input("Enter x:"))
y = int(input("Enter y:"))
z = int(input("Enter z:"))

odd = []

for i in [x,y,z]:
    if i%2 != 0:
        odd.append(i)

if len(odd) > 0:
    print(f"The largest odd number is {max(odd)}.")
else:
    print("No variables are odd.")
    