### Finger 3-5 ###
"""
Add some code to the implementation of Newton-Raphson that
keeps track of the number of iterations used to find the root. Use that code as
part of a program that compares the efficiency of Newton-Raphson and bisection
search. (You should discover that Newton-Raphson is more efficient.)
"""

x = 24
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low)/2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to square root of', x)

#Newton-Raphson for square root
#Find x such that x**2 - 24 is within epsilon of 0
k = 24.0
epsilon = 0.01
newtonGuesses = 0
guess = k/2.0
while abs(guess*guess - k) >= epsilon:
    guess = guess - (((guess**2) - k)/(2*guess))
    newtonGuesses += 1

print('newtonGuesses =', newtonGuesses)
print('Square root of', k, 'is about', guess)
