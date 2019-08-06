import sys
input = sys.stdin.readline

def main():
	s = input().strip()
	rc = 0
	lc = 0
	i = 0
	n = len(s)
	ans = [0] * n
	while i <= n-2:
		if s[i] == 'R':
			rc += 1
		if s[i] == 'R' and s[i+1] == 'L':
			# 上でカウントしたのを覗く
			rc -= 1
			k = 0
			while i+2+k < n and  s[i+2+k] != 'R':
				k += 1
			# print("{rc k}", rc, k)
			tor = 1 + ((k+1) // 2) + (rc // 2)
			tol = 1 + ((rc+1) // 2) + (k // 2)
			# print('tor, rol',tor, tol)
			if max(rc, k) % 2 == 0:
				# RはRと同じ場所にいる
				ans[i] = tor
				ans[i+1] = tol
			else:
				# 違う場所
				ans[i] = tor
				ans[i+1] = tol

			rc = 0
			i = i + 1 + k
		i += 1
	for i in ans:
		print("{} ".format(i) , end="")
	print("")
if __name__ == '__main__':
	main()
