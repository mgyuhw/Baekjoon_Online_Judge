import sys

def main():
    data = list(map(int, sys.stdin.read().split()))
    count = 0

    for i in range(1, data[0] + 1):
        if data[-1] == data[i]:
            count += 1

    sys.stdout.write(count)

if __name__ == "__main__":
    main()

"""
배열에 .count(n) 하면 찾아줌;;
"""