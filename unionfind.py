class UnionFind:
	def __init__(self, n):
		self.rank = [0] * n
		self.parent = [0] * n
		self.make(n)

	def make(self, n):
		for i in range(n):
			self.parent[i] = i

	def unite(self, x, y):
		xroot = self.findset(x)
		yroot = self.findset(y)
		if xroot == yroot:
			return
		if self.rank[xroot] < self.rank[yroot]:
			self.parent[xroot] = yroot
		elif self.rank[xroot] > self.rank[yroot]:
			self.parent[yroot] = xroot
		else:
			self.parent[xroot] = yroot
			self.rank[yroot] += 1

	def findset(self, x):
		if self.parent[x] == x:
			return x
		else:
			root = self.findset(self.parent[x])
			self.parent[x] = root
			return root
