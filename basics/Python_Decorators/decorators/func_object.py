# Python program to illustrate functions
# can be treated as objects
def shout(text, val2):
	return text.upper() + val2

# print(shout('Hello'))

yell = shout

print(yell('Hello', "sec2"))
