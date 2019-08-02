import sys
input = sys.stdin.readline
from operator import itemgetter

def main():
	n, m = map(int, input().strip().split())
	city = [[] for _ in range(m)]
	for i in range(m):
		p, y = map(int, input().strip().split())
		city[i] = [i, p, y]
	city.sort(key=itemgetter(2))
	city.sort(key=itemgetter(1))
	id = 0
	for i in range(m):
		if i != 0 and city[i][1] != city[i-1][1]:
			id = 1
		else:
			id += 1
		city[i].append(id)
	city.sort(key=itemgetter(0))
	for i in range(m):
		print("{:06}{:06}".format(city[i][1], city[i][3]))
if __name__ == '__main__':
	main()
