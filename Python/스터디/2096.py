import sys

def main():
    count = int(sys.stdin.readline())
    max_memo = [0 for _ in range(3)]
    min_memo = [0 for _ in range(3)]

    for i in range(count):
        left, mid, right = map(int, sys.stdin.readline().split())
        max_memo[0], max_memo[1], max_memo[2] = max((max_memo[0] + left), (max_memo[1] + left)), max((max_memo[0] + mid), (max_memo[1] + mid), (max_memo[2] + mid)), max((max_memo[1] + right), (max_memo[2] + right))
        min_memo[0], min_memo[1], min_memo[2] = min((min_memo[0] + left), (min_memo[1] + left)), min((min_memo[0] + mid), (min_memo[1] + mid), (min_memo[2] + mid)), min((min_memo[1] + right), (min_memo[2] + right))

    sys.stdout.write(str(max(max_memo[0], max_memo[1], max_memo[2])) + ' ' + str(min(min_memo[0], min_memo[1], min_memo[2])))

if __name__ == "__main__":
    main()
