import sys
input = sys.stdin.readline

N = 0
W = 0
items = []
def main():
	global N, W, items
	N, W = map(int, input().strip().split())
	for i in range(N):
		v, w = map(int, input().strip().split())
		items.append((v, w))
	print(val(0, W, 0))


def val(i, space, value):
	if i > N-1:
		return value

	if space - items[i][1] < 0:
		return val(i+1, space, value)

	return max(val(i+1, space - items[i][1], value + items[i][0]), val(i+1, space, value))
	# max(take -> -1, not take -> -1)

if __name__ == '__main__':
	main()
