import sys

def main():
    count = int(sys.stdin.readline())
    pack = [0] + list(map(int, sys.stdin.readline().split()))
    memo = [0] * (count + 1)

    for i in range(1, count + 1):
        for j in range(1, i + 1):
            memo[i] = memo[i] if memo[i] > (memo[i - j] + pack[j]) else (memo[i - j] + pack[j])

    sys.stdout.write(str(memo[-1]))

if __name__ == "__main__":
    main()