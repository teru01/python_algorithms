import sys
input = sys.stdin.readline
from collections import defaultdict

def main():
	n = int(input().strip())
	v = list(map(int, input().strip().split()))
	ki = {}
	gu = {}
	for i in range(n):
		if i % 2 == 0:
			if v[i] in gu:
				gu[v[i]] += 1
			else:
				gu[v[i]] = 1
		else:
			if v[i] in ki:
				ki[v[i]] += 1
			else:
				ki[v[i]] = 1
	km = 0
	kmi = 0
	ksm = 0
	ksmi = 0
	gm = 0
	gsm = 0
	gmi = 0
	gsmi = 0
	for k, v in ki.items():
		print(k, v)
		if v > km:
			km = v
			kmi = k
			print(k)
	for k, v in ki.items():
		if k == kmi:
			continue
		if v > ksm:
			ksm = v
			ksmi = k

	for k, v in gu.items():
		if v > gm:
			gm = v
			gmi = k
	for k, v in gu.items():
		if k == gmi:
			continue
		if v > gsm:
			gsm = v
			gsmi = k
	ks = sum(ki.values()) - km
	gs = sum(gu.values()) - gm
	# print(ks)
	# print(gs)
	# print(kmi)
	# print(gmi)
	if kmi == gmi:
		if km < gm:
			ks = ks - ksm + km
		else:
			gs = gs - gsm + gm
	print(ks + gs)
	return 0

if __name__ == '__main__':
	main()
