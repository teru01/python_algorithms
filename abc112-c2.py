import sys
input = sys.stdin.readline
W = 101
def main():
	n = int(input().strip())
	x = [0] * n
	y = [0] * n
	h = [0] * n
	for i in range(n):
		x[i], y[i], h[i] = map(int, input().strip().split())
	for s in range(W):
		for t in range(W):
			needH = -1
			for i in range(n):
				if h[i] > 0:
					tmp = h[i] + abs(x[i]-s) + abs(y[i]-t)
					if needH == -1:
						needH = tmp
					elif needH != tmp:
						needH = -2
						break
			if needH == -2:
				continue
			for i in range(n):
				if h[i] == 0 and needH > abs(x[i]-s) + abs(y[i]-t):
					needH = -2
					break
			if needH == -2:
				continue
			else:
				print("{} {} {}".format(s, t, needH))

if __name__ == '__main__':
	main()
