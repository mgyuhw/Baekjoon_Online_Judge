import sys

def main():
    count = int(sys.stdin.readline())

    for _ in range(count):
        data = list(map(int, sys.stdin.readline().split()))

        num = data[2] // data[0] + 1
        height = data[2] % data[0]

        if height == 0:
            num -= 1
            height = data[0]

        sys.stdout.write("{:d}{:02d}\n".format(height, num))

if __name__ == "__main__":
    main()