#Find the number of "1"'s in the binary representation of a number

a = 2345678
count = 0

while a > 0:
	if a&1 == 1:
		count += 1
	a >>= 1

print count