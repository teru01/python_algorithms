import sys
input = sys.stdin.readline

def is_753(n):
	s = str(n)
	f = [0,0,0]
	for c in s:
		if c == '3':
			f[0] = 1
		elif c == '5':
			f[1] = 1
		elif c == '7':
			f[2] = 1
	if all(f):
		return True
	else:
		return False

N = 0
c = 0
def gen(n):
	global c
	for i in [3,5,7]:
		k = 10 * n + i
		# print(k)
		if k > N:
			return
		if is_753(k):
			c += 1
			# print(k)
		gen(k)

def main():
	global N
	s = input().strip()
	N = int(s)
	n = len(s)

	gen(0)
	print(c)


if __name__ == '__main__':
	main()
