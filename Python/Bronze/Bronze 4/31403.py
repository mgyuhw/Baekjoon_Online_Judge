import sys

def main():
    data = list(map(int, sys.stdin.read().splitlines()))

    sys.stdout.write(str(data[0] + data[1] - data[2]) + '\n')
    sys.stdout.write(str(int(str(data[0]) + str(data[1])) - data[2]))

if __name__ == "__main__":
    main()