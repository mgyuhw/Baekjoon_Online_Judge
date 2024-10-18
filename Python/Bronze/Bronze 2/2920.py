import sys

def main():
    data = list(map(int, sys.stdin.readline().split()))

    if data == sorted(data): sys.stdout.write("ascending")
    elif data == sorted(data, reverse=True): sys.stdout.write("descending")
    else: sys.stdout.write("mixed")

if __name__ == "__main__":
    main()
