import sys

def main():
    data = sys.stdin.read().splitlines()

    sys.stdout.write(f"{int(max(data))}\n{int(data.index(max(data))) + 1}")

if __name__ == "__main__":
    main()

"""
정수로 나와야 한다네요...
"""