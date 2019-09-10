import sys
input = sys.stdin.readline
from operator import itemgetter

ans = []
v = []

# def rec(i, p):
# 	global ans, v
# 	if p != -1:
# 		ans[i] += ans[p]
# 	for node in v[i]:
# 		if node != p:
# 			rec(node, i)

# 隣接リストからのdfs
def rec(i, p):
	global ans, v
	for node in v[i]:
		if node != p:
			ans[node] += ans[i]
			rec(node, i)

def main():
	global v, ans
	n, q = map(int, input().strip().split())
	v = [[] for _ in range(n)]
	ans = [0] * n
	for i in range(n-1):
		a, b = map(int, input().strip().split())
		a -= 1
		b -= 1
		v[a].append(b)
		v[b].append(a)
	
	for i in range(q):
		a, b = map(int, input().strip().split())
		a -= 1
		ans[a] += b
	
	rec(0, -1)
	for e in ans:
		print(e)

if __name__ == '__main__':
	main()
