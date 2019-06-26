import sys
input = sys.stdin.readline

c = 0
MAX = 1000000000
def merge(li, l, mid, r):
	global c
	nl = mid - l
	nr = r - mid
	left = [li[i] for i in range(l, mid)]
	right = [li[i] for i in range(mid, r)]
	left.append(MAX)
	right.append(MAX)
	q = 0
	w = 0
	for i in range(nl + nr):
		c += 1
		if left[q] < right[w]:
			li[l+i] = left[q]
			q += 1
		else:
			li[l+i] = right[w]
			w += 1

def mergesort(li, l, r):
	if l+1 < r:
		mid = (l+r)//2
		mergesort(li, l, mid)
		mergesort(li, mid, r)
		merge(li, l, mid, r)

n = int(input().strip())
v = list(map(int, input().strip().split()))
mergesort(v, 0, n)

for i, val in enumerate(v):
	if i == len(v)-1:
		print(val)
	else:
		print("{} ".format(val), end='')
print(c)
