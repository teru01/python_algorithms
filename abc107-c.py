import sys
input = sys.stdin.readline
from operator import itemgetter
from bisect import bisect_left

def main():
	n, k = map(int, input().strip().split())
	x = list(map(int, input().strip().split()))
	zero = bisect_left(x, 0)
	# print("zero:{}".format(zero))
	ans = 10**12
	for l in range(k+1):
		r = k-l-1
		left_i = zero-l
		right_i = zero+r
		if left_i >= 0 and right_i < n:
			if x[left_i] >= 0:
				ans = min(ans, x[right_i])
			elif x[right_i] <= 0:
				ans = min(ans, abs(x[left_i]))
			else:
				ans = min(ans, min(2*abs(x[left_i])+x[right_i], 2*x[right_i]+abs(x[left_i])))
		# print("l:{}, r:{}, ans:{}".format(left_i, right_i, ans))
	print(ans)

if __name__ == '__main__':
	main()
