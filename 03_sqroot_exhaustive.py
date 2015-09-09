'''This is a example of exhaustive search'''

x = float(input('Enter a number: '))
epsilon = 0.01      #epsilon is the amount of error we can accept.
step = 0.5
numGuesses = 0
ans = 0.0

while (abs(ans**2 - x)) >= epsilon and ans <= x:
	ans += step
	numGuesses += 1

print('number of Guesses = '+str(numGuesses))
if abs(ans**2-x) >= epsilon:
	print('Failed on square root of '+str(x))
else:
	print(str(ans)+' is close to the square root of '+str(x))