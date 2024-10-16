import sys

def main():
    target = int(sys.stdin.readline())

    if target % 5 == 0:
        sys.stdout.write(str(target // 5))
        return

    remainder = target % 5

    while remainder % 3 != 0:
        if remainder + 5 <= target:
            remainder += 5
        else:
            sys.stdout.write("-1")
            return

    sys.stdout.write(str(((target - remainder) // 5) + (remainder // 3)))

if __name__ == "__main__":
    main()