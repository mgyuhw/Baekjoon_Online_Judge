import sys

def main():
    data = list(map(int, sys.stdin.read().splitlines()))

    for i in range(1, 31):
        if i not in data:
            print(i)

if __name__ == "__main__":
    main()
