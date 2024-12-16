import sys

def main():
    first_len, second_len = map(int, sys.stdin.readline().split())
    first_arr = list(map(int, sys.stdin.readline().split()))
    second_arr = list(map(int, sys.stdin.readline().split()))

    fl = sl = 0
    temp = list()

    while fl < first_len and sl < second_len:
        if first_arr[fl] <= second_arr[sl]:
            temp.append(first_arr[fl])
            fl += 1
        else:
            temp.append(second_arr[sl])
            sl += 1

    while fl < first_len:
        temp.append(first_arr[fl])
        fl += 1
    while sl < second_len:
        temp.append(second_arr[sl])
        sl += 1

    sys.stdout.write(' '.join(map(str, temp)))

if __name__ == "__main__":
    main()
