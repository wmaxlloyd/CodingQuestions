# Reverse bits of a given 32 bits unsigned integer.

# For example, given input 43261596 (represented in binary as 00000010100101000001111010011100), return 964176192 (represented in binary as 00111001011110000010100101000000).

#This flips all bits in an integer
a = 43261596
# bitLen = 32
# b = a

# for i in xrange(bitLen):
# 	b ^= (1 << i)

# print b

# Reversing the string
print "String Reverse"
bina = bin(a)[2:] #removing 0b prefix
a32 = "0" * (32-len(bina)) + bina
print int(a32[::-1],2)

#Assumptions:
# - Number is not over 32 bits
# - is int (not string)
# - requires no validation
# Advantage - uses 32 bits of memory to flip
print "bitwise operations"
rev = 0
for i in xrange(32):
	if a>>i & 1: # If the ith bit of a is 1
		rev |= 1<<(32-i-1)
print rev