import sys
input = sys.stdin.readline

def main():
	S = input().strip().split()
	words = set()
	for w in S:
		if w[-1] in [',', '.', '?', '!']:
			w = w[:-1]
		if w[0].isupper() or w[0].isdecimal():
			words.add(w)
	print(len(words))

if __name__ == '__main__':
	main()
