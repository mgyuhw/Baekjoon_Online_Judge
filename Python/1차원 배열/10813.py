import sys

def main():
    data = list(map(int, sys.stdin.readline().split()))
    basket = [i for i in range(1, data[0] + 1)]

    for i in range(data[1]):
        i, j = list(map(int, sys.stdin.readline().split()))
        i -= 1
        j -= 1
        basket[i], basket[j] = basket[j], basket[i]

    sys.stdout.write(' '.join(map(str, basket)))

if __name__ == "__main__":
    main()