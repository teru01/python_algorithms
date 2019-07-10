import sys
input = sys.stdin.readline

v = []
p = []
count = 0
m = 0
def rec(l, n):
	global count
	if len(l) == n:
		c = 0
		st = set()
		for i in range(n):
			if l[i] == 1:
				st.add(i + 1)
		for k, sw in enumerate(v):
			# print(st)
			if len(sw.intersection(st)) % 2 != p[k]:
				return
		# print("c: {}".format(c))
		count += 1
		# print(l)
		return
	l.append(0)
	rec(list(l), n)
	l.pop()
	l.append(1)
	rec(list(l), n)

def main():
	global v
	global p
	global m
	n, m = map(int, input().strip().split())
	for i in range(m):
		tmp = list(map(int, input().strip().split()))
		v.append(set(tmp[1:]))
	p = list(map(int, input().strip().split()))
	rec([], n)
	print(count)

if __name__ == '__main__':
	main()
