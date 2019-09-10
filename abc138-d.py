import sys
input = sys.stdin.readline
from operator import itemgetter

WHITE = -1
BLACK = -100
class Node:
	def __init__(self, id):
		self.id = id
		self.color = WHITE
	parent = None
	children = []
	x = 0
	w = 0

v = []
nodes = []

def dfs(node, p = -1):
	global v, nodes
	nodes[node].w = nodes[nodes[node].parent].w + nodes[node].x
	if len(nodes[node].children) == 0:
		return
	for k in nodes[node].children:
		if k != nodes[node].parent:
			dfs(k)

def main():
	global v, nodes
	n, q = map(int, input().strip().split())
	v = [[] for _ in range(n)]
	for i in range(n-1):
		a, b = map(int, input().strip().split())
		a -= 1
		b -= 1
		v[a].append(b)
		v[b].append(a)
	nodes = [Node(i) for i in range(n)]
	# for i in range(n-1):
	# 	for j in v[i]:
	# 		if j != nodes[i].parent:
	# 			nodes[i].children.append(j)
	# for i in range(n):
	# 	print("id: {}".format(nodes[i].id))
	# 	print(nodes[i].color)
	# 	print(nodes[i].parent)
	# 	print(nodes[i].children)
	# 	print("==============")
	
	for i in range(q):
		a, b = map(int, input().strip().split())
		nodes[a-1].x += b

	dfs(0)

	for i in range(n):
		print(v[i])
		print(nodes[i].w)

if __name__ == '__main__':
	main()
