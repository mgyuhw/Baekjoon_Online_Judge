import sys


def main():
    difficulty = list(map(int, sys.stdin.readline().split()))
    team = int(sys.stdin.readline())
    result = 0

    for _ in range(team):
        memo = 0
        for i in range(3):
            coding = list(map(int, sys.stdin.readline().split()))
            memo += coding[0] * difficulty[0] + coding[1] * difficulty[1] + coding[2] * difficulty[2]

        result = memo if memo > result else result

    sys.stdout.write(str(result))


if __name__ == "__main__":
    main()
    