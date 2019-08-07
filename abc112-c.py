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
			gr = set()
			for i in range(n):
				if h[i] != 0:
					H = h[i] + abs(x[i]-s) + abs(y[i]-t)
					gr.add(H)
			for i in range(n):
				if h[i] == 0:
					gr = {k for k in gr if k <= abs(x[i]-s) + abs(y[i]-t)}

			if len(gr) == 1:
				u = gr.pop()
				print(s, t, u)
				# return

if __name__ == '__main__':
	main()
