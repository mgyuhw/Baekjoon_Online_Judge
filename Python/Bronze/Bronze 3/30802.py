import sys

def main():
    num = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))
    shirts, pen = map(int, sys.stdin.readline().split())
    shirts_bundle = 0

    for i in data:
        shirts_bundle += (i // shirts + 1) if i % shirts != 0 else (i // shirts)

    sys.stdout.write(f"{shirts_bundle}\n{num // pen} {num % pen}")

if __name__ == "__main__":
    main()
    