import sys

def main():
    count = int(sys.stdin.readline())
    max_memo = [0 for _ in range(3)]
    min_memo = [0 for _ in range(3)]

    for i in range(count):
        left, mid, right = map(int, sys.stdin.readline().split())
        max_memo[0], max_memo[1], max_memo[2] = (max_memo[0] + left) if max_memo[0] > max_memo[1] else (max_memo[1] + left), max(max_memo[0], max_memo[1], max_memo[2]) + mid, (max_memo[1] + right) if max_memo[1] > max_memo[2] else (max_memo[2] + right)
        min_memo[0], min_memo[1], min_memo[2] = (min_memo[0] + left) if min_memo[0] < min_memo[1] else (min_memo[1] + left), min(min_memo[0], min_memo[1], min_memo[2]) + mid, (min_memo[1] + right) if min_memo[1] < min_memo[2] else (min_memo[2] + right)

    sys.stdout.write(str(max(max_memo[0], max_memo[1], max_memo[2])) + ' ' + str(min(min_memo[0], min_memo[1], min_memo[2])))

if __name__ == "__main__":
    main()
