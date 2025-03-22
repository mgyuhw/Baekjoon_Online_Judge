import sys

if __name__ == "__main__":
    hour, minute = map(int, sys.stdin.readline().split())
    time = int(input())

    minute += time

    while minute >= 60:
        hour += 1
        minute -= 60

    if hour >= 24:
        hour -= 24

    sys.stdout.write(f"{hour} {minute}")
