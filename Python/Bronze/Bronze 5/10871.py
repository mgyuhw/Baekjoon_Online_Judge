import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    stack = []

    for i in range(2, data[0] + 2):
        if data[1] > data[i]: stack.append(str(data[i]))

    sys.stdout.write(' '.join(stack))

if __name__ == "__main__":
    main()