import sys
input = sys.stdin.readline
n = 0
m = 0
s = []
p = []
ans = 0

def rec(v, y):
	global n, m, p, s, ans
	if y == 0:
		# ひかる電球数
		d = 0
		for i in range(m):
			# ONスイッチ数
			c = 0
			for j in range(s[i][0]):
				if v[s[i][1 + j]-1] == 1:
					c += 1
			if c % 2 == p[i]:
				d += 1
		if d == m:
			ans += 1
		return
	rec(list(v + [0]), y-1)
	rec(list(v + [1]), y-1)

def main():
	global n, m, s, p, ans
	n, m = map(int, input().strip().split())
	s = [[] for _ in range(m)]
	for i in range(m):
		s[i] = list(map(int, input().strip().split()))
	p = list(map(int, input().strip().split()))
	rec([], n)
	print(ans)

if __name__ == '__main__':
	main()
