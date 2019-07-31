import sys
input = sys.stdin.readline

n = 0
v = []
s = []
# s[0]が2*qの時に1周してs[n]を返す関数
def f(q):
	global s
	s = [0] * (n+1)
	# 0の持分
	s[0] = 2 * q
	for j in range(1, n+1):
		s[j] = 2 * (v[j-1] - s[j-1]//2)
	return s[n], s[0]


def bin(i, j):
	if i+1 >= j:
		f(i)
		return s
	mid = (i+j) // 2
	res, expect = f(mid)
	if res == expect:
		return s
	elif res < expect:
		return bin(i, mid)
	else:
		return bin(mid, j)

def main():
	global n, v
	n = int(input().strip())
	v = list(map(int, input().strip().split()))
	w = []
	N = min(v[0], v[1])
	w = bin(0, N+1)
	for i in range(n):
		print("{} ".format(w[i]), end='')
	print("")

if __name__ == '__main__':
	main()
