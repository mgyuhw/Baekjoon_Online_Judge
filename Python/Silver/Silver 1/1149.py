import sys

def main():
    count = int(sys.stdin.readline())
    red, green, blue = [[0] * 1001 for _ in range(3)]
    memo = [[0] * 3 for _ in range(count)]

    for i in range(count):
        red[i], green[i], blue[i] = list(map(int, sys.stdin.readline().split()))

    memo[0][0], memo[0][1], memo[0][2] = red[0], green[0], blue[0]

    for i in range(1, count):
        # Red Home
        memo[i][0] = (memo[i-1][1] + red[i]) if (memo[i-1][1] + red[i]) < (memo[i-1][2] + red[i]) else (memo[i-1][2] + red[i])
        # Green Home
        memo[i][1] = (memo[i-1][0] + green[i]) if (memo[i-1][0] + green[i]) < (memo[i-1][2] + green[i]) else (memo[i-1][2] + green[i])
        # Blue Home
        memo[i][2] = (memo[i-1][1] + blue[i]) if (memo[i-1][1] + blue[i]) < (memo[i-1][0] + blue[i]) else (memo[i-1][0] + blue[i])

    print(min(memo[count-1][0], memo[count-1][1], memo[count-1][2]))


if __name__ == "__main__":
    main()