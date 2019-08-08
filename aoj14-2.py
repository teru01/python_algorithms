import sys
input = sys.stdin.readline
from operator import itemgetter

p = []
np = 0
def make_1d_tree(l, r):
	global p, np
	if l >= r:
		return
	p[l:r] = sorted(p[l:r])
	mid = (l + r) // 2
	np += 1
	T[np].location = mid
	

def main():
	global p
	n = int(input().strip())
	p = list(map(int, input().strip().split()))
	

if __name__ == '__main__':
	main()
