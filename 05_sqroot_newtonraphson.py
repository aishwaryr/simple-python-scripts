'''Finding square roots using Newton-Raphson algorithm'''

epsilon = 0.01           #epsilon is the amount of error we can accept.
y = float(input('Enter a num : '))
guess = y/2.0

while abs(guess*guess - y) >= epsilon:
	guess = guess - (((guess**2) - y)/(2*guess))
print('Square root of '+str(y)+' is about '+str(guess))