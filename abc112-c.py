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
	for s in range(10):
		for t in range(10):
			for i in range(n):
				gr = set()
				gr.add(h[i] - abs(x[i]-s)-abs(y[i]-t))
		if len(gr) == 1:
			h = gr.pop()
			if h >= 0:
				print(s, t, h)
				return


if __name__ == '__main__':
	main()
