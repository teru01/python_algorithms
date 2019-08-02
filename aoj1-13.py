import sys
input = sys.stdin.readline
board = []
row = []
col = []
dpos = []
dneg = []
ZONE = -1
N = -1
VOID = '-'
FILLED = '●'
ZONED = '○'
npattern = 0
def putQ(r, c):
	global board, row, col, dpos, dneg
	board[r][c] = FILLED
	row[r] = ZONE
	col[c] = ZONE
	dpos[r+c] = ZONE
	dneg[r-c+N-1] = ZONE

def popQ(r, c):
	global board, row, col, dpos, dneg
	board[r][c] = VOID
	row[r] = 0
	col[c] = 0
	dpos[r+c] = 0
	dneg[r-c+N-1] = 0

def printBoard():
	global npattern
	for i in range(N):
		for j in range(N):
			if board[i][j] == FILLED:
				print("{:2}".format(FILLED), end="")
			else:
				print("{:2}".format(ZONED), end="")
		print("")
	print("===========================")
	npattern += 1

# うまくいけば
def backtrack(i):
	if i == N:
		printBoard()
		return
	if row[i] == ZONE:
		# すでにクイーンが置かれている行
		return backtrack(i+1)
	for j in range(N):
		# print(i, j)
		if col[j] == ZONE or dpos[i+j] == ZONE or dneg[i-j+N-1] == ZONE:
			continue
		putQ(i, j)
		backtrack(i+1)
		popQ(i, j)

def main():
	global board, row, col, dpos, dneg, N
	N, k = map(int, input().strip().split())
	board = [[VOID] * N for _ in range(N)]
	row = [0] * N
	col = [0] * N
	dpos = [0] * (2*N-1)
	dneg = [0] * (2*N-1)
	for _ in range(k):
		r, c = map(int, input().strip().split())
		putQ(r, c)
	backtrack(0)
	print("Number of patterns: {}".format(npattern))

if __name__ == '__main__':
	main()
