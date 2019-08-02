import sys
input = sys.stdin.readline

mat = []
dist = []
v = 0
e = 0
INF = 10**9
def warshallFloyd():
	global dist, mat
	for k in range(v):
		for i in range(v):
			if mat[i][k] == INF:
				continue
			for j in range(v):
				#mat(1)[i][j]からmat(v)[i][j]まで
				if mat[k][j] == INF:
					continue
				mat[i][j] = min(mat[i][j], mat[i][k] + mat[k][j])

def main():
	global v, e, mat, dist
	v, e = map(int, input().strip().split())
	mat = [[INF] * v for _ in range(v)]
	for i in range(e):
		a, b, c = map(int, input().strip().split())
		mat[a][b] = c
	for i in range(v):
		mat[i][i] = 0
	warshallFloyd()
	for i in range(v):
		for j in range(v):
			if i == j and mat[i][j] < 0:
				print("NEGATIVE CYCLE")
				return
	for i in range(v):
		for j in range(v):
			if j != 0:
				print(" ", end="")
			if mat[i][j] == INF:
				print("INF", end="")
			else:
				print("{}".format(mat[i][j]), end="")
		print("")

if __name__ == '__main__':
	main()
