import sys
input = sys.stdin.readline

def main():
	n = int(input().strip())
	v = list(map(int, input().strip().split()))
	ans = 0
	for i in range(n-2):
		l = v[i:i+3]
		# print(l)
		t = l[1]
		if t == sorted(l)[1]:
			ans += 1
	print(ans)

if __name__ == '__main__':
	main()
