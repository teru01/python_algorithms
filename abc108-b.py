import sys
input = sys.stdin.readline
from operator import itemgetter

def rotate(x, y):
	return (-y, x)

def main():
	x1, y1, x2, y2 = map(int, input().strip().split())
	v = (x2-x1, y2-y1)
	lp = (x2, y2)
	for i in range(2):
		v = rotate(v[0], v[1])
		next = lp[0]+v[0], lp[1]+v[1]
		print("{} {} ".format(next[0], next[1]), end="")
		lp = next
	print("")
	# d = max(abs(x1 - x2), abs(y1 - y2))
	# if y1 > y2:
	# 	print(" ".join(map(str, [x2+d, y2, x2+d, y1])))
	# elif y1 < y2:
	# 	print(" ".join(map(str, [x2-d, y2, x2-d, y1])))
	# elif x1 > x2:
	# 	print(" ".join(map(str, [x2, y2-d, x1, y2-d])))
	# elif x1 < x2:
	# 	print(" ".join(map(str, [x2, y2+d, x1, y2+d])))

if __name__ == '__main__':
	main()
