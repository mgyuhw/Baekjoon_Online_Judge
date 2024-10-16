import sys

def main():
    n = sys.stdin.readline().rstrip()
    data = list(map(int, sys.stdin.readline().split()))

    sys.stdout.write(f"{min(data)} {max(data)}")

if __name__ == "__main__":
    main()