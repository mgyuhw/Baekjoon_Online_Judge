import sys

def main():
    length = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))

    sys.stdout.write(str((sum(data) / max(data) * 100) / length))

if __name__ == "__main__":
    main()
