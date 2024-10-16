"""
랭킹에 올라온 다른 분들의 코드를 살펴서 수정한 코드입니다.
batch, array에 대해 알아볼 수 있었습니다.
"""

import sys
import array

def main():
    # Input Step
    num = int(sys.stdin.readline())

    # Ready for Counting Sort
    counting = array.array('i', [0] * 10001)

    # Count Data
    for i in range(num):
        counting[int(sys.stdin.readline())] += 1

    for i in range(1, 10001):
        count = counting[i]
        while count > 0:
            batch = min(count, 20000)
            sys.stdout.write(f"{i}\n" * batch)
            count -= batch

if __name__ == "__main__":
    main()
