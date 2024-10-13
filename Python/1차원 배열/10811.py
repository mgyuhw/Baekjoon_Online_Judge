import sys

def main():
    data = list(map(int, sys.stdin.readline().split()))
    basket = [i for i in range(1, data[0] + 1)]

    for _ in range(data[1]):
        i, j = map(int, sys.stdin.readline().split())
        i -= 1
        j -= 1
        while i < j:
            basket[i], basket[j] = basket[j], basket[i]
            i += 1
            j -= 1

    sys.stdout.write(' '.join(map(str, basket)))

if __name__ == "__main__":
    main()