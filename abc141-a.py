import sys
input = sys.stdin.readline
from operator import itemgetter

def main():
    v = input().strip()
    if v == "Sunny":
        print("Cloudy")
    elif v == "Cloudy":
        print("Rainy")
    else:
        print("Sunny")

if __name__ == '__main__':
    main()
