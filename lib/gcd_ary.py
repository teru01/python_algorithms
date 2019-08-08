def gcd(a, b):
	if b % a == 0:
		return a
	else:
		return gcd(b % a, a)

def gcd_ary(ary, n):
	for i in range(n-1):
		ary[i+1] = gcd(ary[i], ary[i+1])
	return ary[n-1]
