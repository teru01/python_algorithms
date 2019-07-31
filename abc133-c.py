import sys
input = sys.stdin.readline

K = 2019

def f(a):
	return a // K

def main():
	l, r = map(int, input().strip().split())
	ans = 0
	if f(r) - f(l) >= 1:
		pass
	else:
		t = 10**9
		for i in range(l, r):
			for j in range(l+1, r+1):
				t = min(t , (i*j) % K)
		ans = t
	print(ans)

if __name__ == '__main__':
	main()
