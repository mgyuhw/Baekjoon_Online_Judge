import sys
from collections import deque


def main():
    data = list(map(int, sys.stdin.readline().split()))
    table = deque(str(i) for i in range(1, data[0] + 1))
    result = list()

    while table:
        for _ in range(data[1]-1):
            table.append(table.popleft())

        result.append(table.popleft())

    sys.stdout.write('<')
    sys.stdout.write(", ".join(result))
    sys.stdout.write('>')

if __name__ == "__main__":
    main()
