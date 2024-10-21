"""
랭킹의 코드를 보고 고친 코드입니다.

1. data = sys.stdin.read().split("ENTER")[1:] 사용
2. for i in data 사용
"""

import sys

def main():
    data = sys.stdin.read().split("ENTER")[1:]
    count = 0

    for i in data:
        count += len(set(i.split()))

    sys.stdout.write(str(count))

if __name__ == "__main__":
    main()
