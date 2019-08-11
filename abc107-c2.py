import sys
input = sys.stdin.readline
from operator import itemgetter
from bisect import bisect_left

def main():
	n, k = map(int, input().strip().split())
	x = list(map(int, input().strip().split()))
	# zero = bisect_left(x, 0)
	# print("zero:{}".format(zero))
	ans = 10**12
	for l in range(n):
		r = l + k - 1
		if r >= n:
			break
		if x[r] <= 0:
			ans = min(ans, abs(x[l]))
		elif 0 <= x[l]:
			ans = min(ans, abs(x[r]))
		else:
			ans = min(ans, min(2*abs(x[l])+x[r], 2*x[r]+abs(x[l])))
		# print("l:{}, r:{}, ans:{}".format(left_i, right_i, ans))
	print(ans)

if __name__ == '__main__':
	main()
