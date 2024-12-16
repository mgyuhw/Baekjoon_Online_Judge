import sys

if __name__ == "__main__":
    length, target = map(int, sys.stdin.readline().split())
    data = list(map(int, sys.stdin.readline().split()))

    result = low = high = 0
    partial_sum = data[0]

    while high < length - 1:
        if partial_sum == target:
            result += 1
            high += 1
            partial_sum += data[high]
            continue
        elif low == high or partial_sum < target:
            high += 1
            partial_sum += data[high]
            continue
        elif low < high and partial_sum > target:
            low += 1
            partial_sum -= data[low]
            continue

    if partial_sum == target: result += 1

    sys.stdout.write(str(result))