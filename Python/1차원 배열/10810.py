import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    basket = [0] * n
    print(basket)
    for _ in range(m):
        i, j, k = map(int, sys.stdin.readline().split())
        print(f"{i}, {j}, {k}")
        basket[i-1:j] = [k] * (j - i + 1)
        print(basket)

    sys.stdout.write(' '.join(map(str, basket)))

if __name__ == "__main__":
    main()
