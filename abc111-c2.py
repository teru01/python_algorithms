import sys
input = sys.stdin.readline
from collections import Counter
from operator import itemgetter

def mpsort(m):
	ary = sorted([[k, v] for (k, v) in m.items()], key=itemgetter(1), reverse=True)
	if len(ary) == 1:
		return ary[0], [0, 0]
	return ary[0], ary[1]

def main():
	n = int(input().strip())
	v = list(map(int, input().strip().split()))
	gu = [i for i in v[::2]]
	ki = [i for i in v[1::2]]
	gu_map = Counter(gu)
	ki_map = Counter(ki)
	s = n//2
	# print(gu_map)
	gu_f, gu_s = mpsort(gu_map)
	ki_f, ki_s = mpsort(ki_map)

	if gu_f[0] == ki_f[0]:
			print(min(s - gu_s[1] + s - ki_f[1],
					  s - gu_f[1] + s - ki_s[1]))
	else:
		print(s - gu_f[1] + s - ki_f[1])

if __name__ == '__main__':
	main()
