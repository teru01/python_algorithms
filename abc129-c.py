import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
N = []
v = []
def rec(n):
	global N
	global v
	if v[n] != -1:
		return v[n]

	if N[n] == 1:
		v[n] = 0
	elif n == 1:
		v[n] = 1
	elif N[n-1] == 1:
		v[n] = rec(n-2)
	else:
		v[n] = rec(n-2) + rec(n-1)
	# print("v:", v[n])
	return v[n]

def main():
	global N, v
	n, m = map(int, input().strip().split())
	N = [0] * (n+1)
	v = [-1] * (n+1)
	v[0] = 1
	for i in range(m):
		a = int(input().strip())
		N[a] = 1
	# print(v)
	# print(N)
	print(rec(n) % (10**9+7))

if __name__ == '__main__':
	main()
