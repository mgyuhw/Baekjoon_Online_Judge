import sys

def main():
    data = list(map(int, sys.stdin.readline().split()))
    num = 0

    for i in range(len(data)):
        num += data[i] ** 2

    sys.stdout.write(str(num % 10))

if __name__ == "__main__":
    main()