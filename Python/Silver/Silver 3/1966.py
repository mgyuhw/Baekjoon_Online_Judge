# import sys
# from collections import deque
#
# def main():
#     count = int(sys.stdin.readline().rstrip())
#
#     for i in range(count):
#         data = list(map(int, sys.stdin.readline().split()))
#         line = deque(map(int, sys.stdin.readline().split()))
#         index = deque()
#         index.extend(range(data[0]))
#
#         print_count = 0
#
#         while data[1] in index:
#             if line[0] == max(line):
#                 index.popleft()
#                 line.popleft()
#                 print_count += 1
#             else:
#                 line.rotate(-1)
#                 index.rotate(-1)
#
#         sys.stdout.write(f"{print_count}\n")
#
# if __name__ == "__main__":
#     main()

"""
한준햄 풀이
그룹에서만 안보이지 이거 이상하네요.
2차원 배열? 이건 생각도 몬했네
리스트 append가 덱 rotate보다 빠르다. 결국 rotate는 모든 요소들을 움직여야 하기 때문
원형큐 이런거만 생각해버리면 속도가 빠르게 나오지 않을 것이다.
단순히 리스트를 이용해 연산을 더 줄이는 방법이 속도면에서는 좋을 것
더 만져도 다르게 없다. 만질거 없다.
"""

import sys

def main():
    count = int(sys.stdin.readline().rstrip())

    for i in range(count):
        data = list(map(int, sys.stdin.readline().split()))
        data2 = list(map(int, sys.stdin.readline().split()))
        line = list((i, data2[i]) for i in range(data[0]))
        data2.sort(reverse = True)

        print_count = 0
        turn = 0

        while True:
            if line[turn][1] == data2[print_count]:
                print_count += 1
                if line[turn][0] == data[1]:
                    sys.stdout.write(f"{print_count}\n")
                    break
            else:
                line.append((line[turn]))

            turn += 1

if __name__ == "__main__":
    main()
