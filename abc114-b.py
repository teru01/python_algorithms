import sys
input = sys.stdin.readline

def main():
	s = input().strip()
	ans = 100000000
	for i in range(len(s)-2):
		ans = min(ans, abs(753 - int(s[i]+s[i+1]+s[i+2])))
	print(ans)

if __name__ == '__main__':
	main()
