import sys
input = sys.stdin.readline
from operator import itemgetter
sys.setrecursionlimit(10000000)
INF = 10**30

class UnionFind:
	def __init__(self, n):
		self.rank = [0] * (n+1)
		self.parent = [0] * (n+1)
		self.make(n)

	def make(self, n):
		for i in range(n+1):
			self.parent[i] = i

	def unite(self, x, y):
		xroot = self.findset(x)
		yroot = self.findset(y)
		if self.rank[xroot] < self.rank[yroot]:
			self.parent[xroot] = yroot
		elif self.rank[xroot] > self.rank[yroot]:
			self.parent[yroot] = xroot
		else:
			self.parent[xroot] = yroot
			self.rank[yroot] += 1
			node = y
			while True:
				self.rank[node] += 1
				if self.parent[node] == node:
					break
				node = self.parent[node]
			self.rank[y] += 1

	def findset(self, x):
		if self.parent[x] == x:
			return x
		else:
			root = self.findset(self.parent[x])
			self.parent[x] = root
			return root


def same(uf, x, y):
    return uf.findset(x) == uf.findset(y)

def main():
    n, d, k = list(map(int, input().strip().split()))
    l = [0] * d
    r = [0] * d
    s = [0] * k
    t = [0] * k
    for i in range(d):
        l[i], r[i] = list(map(int, input().strip().split()))
    for i in range(k):
        s[i], t[i] = list(map(int, input().strip().split()))
    for i in range(k):
        uf = UnionFind(n)
        days = 0
        while not same(uf, s[i], t[i]):
            for j in range(l[days], r[days]):
                uf.unite(j, j+1)
            days += 1
        print(days)
if __name__ == '__main__':
    main()
