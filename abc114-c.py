import sys
input = sys.stdin.readline


c = 0
num = 0
def check(n):
	strn = str(n)
	l = [0, 0, 0]
	for c in strn:
		if c == '3':
			l[0] = 1
		elif c == '5':
			l[1] = 1
		elif c == '7':
			l[2] = 1
	return all(l) or False

def gen(n):
	global c
	# print(n)
	if n > num:
		return
	if check(n):
		# print(n)
		c += 1
	for i in [3, 5, 7]:
		k = 10 * n + i
		gen(k)

def main():
	global num
	num = int(input().strip())
	gen(0)
	print(c)

if __name__ == '__main__':
	main()
