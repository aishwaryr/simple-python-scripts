'''Finds out if a string is a palindrome or not using recursion.'''


def isPalindrome(s):
	
	def toChars(s):
		s = s.lower()
		ans = ''
		for c in s:
			if c in 'abcdefghijklmnopqrstuvwxyz':
				ans = ans + c
		return ans

	def isPal(s):
		if len(s) <= 1:
			return True
		else:
			return s[0] == s[-1] and isPal(s[1:-1])

	print isPal(toChars(s))

string = raw_input('Enter a string: ')
isPalindrome(string)