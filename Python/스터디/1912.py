import sys

def main():
    count = int(sys.stdin.readline())
    progression = list(map(int, sys.stdin.readline().split()))

    memo = [0] * (sum(range(1, count + 1)))

    for i in range(count):
        print(f"IIIIII : {i}")
        for j in range(i, count):
            print(f"JJJJJJJJ : {j}")
            if i == j:
                print(f"if : {(i * count) + j}")
                memo[(i * count) + j] = progression[j]
            else:
                print(f"else : {(i * count) + j}")
                memo[(i * count) + j] = progression[j] + memo[i * count + j - 1]

    print(memo)


if __name__ == "__main__":
    main()