import sys

def main():
    while True:
        data = list(map(int, sys.stdin.readline().split()))
        if data == [0, 0, 0]: break
        data.sort()
        sys.stdout.write("right" if ((data[0] ** 2 + data[1] ** 2) == (data[2] ** 2)) else "wrong")

if __name__ == "__main__":
    main()
