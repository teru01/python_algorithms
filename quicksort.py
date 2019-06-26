import sys
input = sys.stdin.readline

def partition(a, l, r):
	i = l - 1
	for j in range(l, r):
		if a[j][1] < a[r-1][1]:
			i += 1
			a[j], a[i] = a[i], a[j]
	a[i+1], a[r-1] = a[r-1], a[i+1]
	return i+1

def quicksort(a, l, r):
	if l+1 < r:
		q = partition(a, l, r)
		quicksort(a, l, q)
		quicksort(a, q+1, r)

#9:15
def main():
	n = int(input().strip())
	a = []
	for _ in range(n):
		k, v = input().strip().split()
		a.append((k, int(v)))
	# a = [(int(k), int(v)) for (k, v) in input().strip().split()]
	quicksort(a, 0, n)
	for i in range(n):
		print("{} {}".format(a[i][0], a[i][1]))

if __name__ == '__main__':
	main()
