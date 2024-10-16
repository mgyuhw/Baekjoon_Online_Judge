import sys

def main():
    remainder = set()

    for i in range(10):
        operand = int(sys.stdin.readline())
        remainder.add(operand % 42)

    print(len(remainder))

if __name__ == "__main__":
    main()
