import sys

def main():
    data = int(sys.stdin.readline().rstrip())

    for i in range(data - (len(str(data)) * 9) if data - (len(str(data)) * 9) > 0 else 0, data):
        if (i + sum(map(int, str(i)))) == data:
            sys.stdout.write(str(i))
            return

    sys.stdout.write("0")

if __name__ == "__main__":
    main()
