import sys

def surf():
    width, height = map(int, sys.stdin.readline().split())
    matrix = [[0 for j in range(width)] for i in range(height)]

    for i in range(height):
        matrix[i] = list(map(int, sys.stdin.readline().split()))


def main():
    surf()

if __name__ == "__main__":
    main()