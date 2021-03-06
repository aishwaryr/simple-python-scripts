'''Finding square root by bisection search.'''

x = float(input('Enter a num: '))
epsilon = 0.01        #epsilon is the amount of error we can accept.
numGuesses = 0
low = 0.0
high = x
ans = (high + low)/2.0
while abs(ans**2 - x) >= epsilon:
	print('low = '+str(low)+' high = '+str(high)+' ans = '+str(ans))
	numGuesses += 1
	if ans**2 < x:
		low = ans
	else:
		high = ans
	ans = (high + low)/2.0
print('numGuesses = '+str(numGuesses))
print(str(ans)+' is close to square root of '+str(x))