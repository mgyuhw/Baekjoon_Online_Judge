"""
랭크 코드를 보고 변경한 내용입니다.

.sort() 하던 부분을 모두 지우고 삼항연산자에서 바로 sorted 사용
"""
import sys
from collections import deque

def main():
    student = deque()
    want_menu = deque()
    good = []
    bad = []

    for _ in range(int(sys.stdin.readline())):
        buffer = list(map(int, sys.stdin.readline().split()))

        if buffer[0] == 1:
            student.append(buffer[1])
            want_menu.append(buffer[2])
        else:
            (good if buffer[1] == want_menu.popleft() else bad).append(student.popleft())

    sys.stdout.write(f"{' '.join(map(str, sorted(good))) if good else 'None'}\n{' '.join(map(str, sorted(bad))) if bad else 'None'}\n{' '.join(map(str, sorted(student))) if student else 'None'}")

if __name__ == "__main__":
    main()
