import sys

def main():
    question = int(sys.stdin.readline())

    for _ in range(question):
        count = int(sys.stdin.readline())
        sticker = [list(map(int, sys.stdin.readline().split())) for i in range(2)]

        memo = [[0] * i for i in (count, count)]

        memo[0][0], memo[1][0] = sticker[0][0], sticker[1][0]
        if count == 1:
            print(memo[0][-1] if memo[0][-1] > memo[1][-1] else memo[1][-1])
            continue

        memo[0][1], memo[1][1] = memo[1][0] + sticker[0][1], memo[0][0] + sticker[1][1]
        if count == 2:
            print(memo[0][-1] if memo[0][-1] > memo[1][-1] else memo[1][-1])
            continue

        if count > 2:
            for i in range(2, count):
                memo[0][i] = (memo[1][i-2] if memo[1][i-2] > memo[1][i-1] else memo[1][i-1]) + sticker[0][i]
                memo[1][i] = (memo[0][i-2] if memo[0][i-2] > memo[0][i-1] else memo[0][i-1]) + sticker[1][i]

            print(memo[0][-1] if memo[0][-1] > memo[1][-1] else memo[1][-1])



if __name__ == "__main__":
    main()
