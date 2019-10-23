a = 18000
b = 2756789
total = ""
carry = False

while a != 0 or b != 0:
	if carry:
		if a&1 == 1 and b&1 == 1:
			total = "1" + total
			carry = True
		elif a&1 ^ b&1 == 1:
			total = "0" + total
			carry = True
		else:
			total = "1" + total
			carry = False
	else:
		if a&1 == 1 and b&1 == 1:
			total = "0" + total
			carry = True
		elif a&1 ^ b&1 == 1:
			total = "1" + total
			carry = False
		else:
			total = "0" + total
			carry = False

	a >>= 1
	b >>= 1

if carry:
	total = "1" + total

print total
print int(total,2)