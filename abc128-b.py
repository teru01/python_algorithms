import sys
input = sys.stdin.readline
from operator import itemgetter

def main():
	n = int(input().strip())
	res = []
	for i in range(n):
		S, P = input().strip().split()
		res.append((S, int(P), i+1))
	res_sed = sorted(res, key=lambda tup: tup[1], reverse=True)
	res_ans = sorted(res_sed, key=lambda tup: tup[0])
	for tup in res_ans:
		print(tup[2])

if __name__ == '__main__':
	main()
