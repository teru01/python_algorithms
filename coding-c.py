import sys
input = sys.stdin.readline
from statistics import mean

def main():
	header = input().strip()
	m = len(header.split(','))
	csv = sys.stdin.read().split('\n')
	n = len(csv)
	ave = [0] * m
	row = []
	for line in csv:
		row.append(list(map(int, line.split(','))))
	for j in range(m):
		s = 0
		for i in range(n):
			s += row[i][j]
		ave[j] = round(s/n)

	print(header)
	print(','.join(map(str, ave)))

if __name__ == "__main__":
	main()
