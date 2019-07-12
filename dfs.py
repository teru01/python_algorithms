import sys
input = sys.stdin.readline
v = []
tl = []
t = 1

def rec(node):
	global t, tl, v
	if tl[node-1][0] != -1:
		# print("ret", node, tl[node-1][0])
		return
	tl[node-1][0] = t
	t += 1
	# print("t: {}", t)
	adj = v[node-1][2:]
	# print("adj: ", adj)
	for i in adj:
		rec(v[i-1][0])
	tl[node-1][1] = t
	t += 1

def main():
	global v, tl
	n = int(input().strip())
	tl = [[-1, -1] for _ in range(n)]
	for i in range(n):
		l = list(map(int, input().strip().split()))
		v.append(l)
	for i in range(1, n+1):
		rec(i)
	for i in range(n):
		print("{} {} {}".format(i+1, tl[i][0], tl[i][1]))

if __name__ == '__main__':
	main()
