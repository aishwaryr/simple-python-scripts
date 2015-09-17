"""Counts the number of times a substring occurs in a text file."""

def substring_count(string, substring):
	count = 0
	sub_len = len(substring)
	for i in range(len(string)):
		# print string[i:i+(sub_len)]
		if string[i:i+(sub_len)] == substring:
			count += 1
	return count

lines = open("/home/ash/code/python/substring_count.txt")
input_string = lines.read()
lines.close()

# input_string = raw_input('Enter string: ')
input_substring = raw_input('Enter substring: ')

print substring_count(input_string, input_substring)