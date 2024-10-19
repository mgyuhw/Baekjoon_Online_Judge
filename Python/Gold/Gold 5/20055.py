"""
랭킹의 코드를 참고하여 변경한 코드입니다.

1. 로봇 내려놓기 if robot[-1] != 0 -> if robot[-1]    (비교 연산 제거)
2. if robot[i] != 0 and robot[i+1] == 0 and belt[i + 1] > 0: -> if robot[i] and not robot[i+1] and belt[i + 1] > 0: (== 비교 제거 후 not 사용)
3. 로봇 올려놓기 if robot[0] == 0 and belt[0] > 0: -> if not robot[0] and belt[0] > 0:    (== 비교 제거 후 not 사용)

4. 로봇 내려놓기 위치 변경. for문 내부에서 외부로 (마지막 부분에 넣는 때가 아닐때는 비교 X)
5. 종료 확인 단일화. (어차피 사이클 내부에서는 사이클이 증가하지 않음. 따라서 마지막에 한번만 파악해도 됨.)

6. 덱 대신 리스트 사용 시도
"""

import sys
from collections import deque

def main():
    space, limit = map(int, sys.stdin.readline().split())
    belt = list(map(int, sys.stdin.readline().split()))
    robot = [0 for i in range(space)]
    count, step = 0, 0

    while True:
        step += 1

        # 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전
        belt[:0] = belt.pop(),
        robot[:0] = robot.pop(),

        # 로봇 내려놓기
        if robot[-1]: robot[-1] = 0

        # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
        for i in range(space - 2, -1, -1):
            # 해당칸에 로봇이 있고, 다음칸에 로봇이 없고, 벨트의 내구성 또한 0이 아니라면
            if robot[i] and not robot[i+1] and belt[i + 1] > 0:
                robot[i], robot[i + 1] = 0, 1
                belt[i + 1] -= 1
                # 내구도 체크
                if belt[i + 1] == 0:
                    count += 1

        # 로봇 내려놓기
        if robot[-1]: robot[-1] = 0

        # 로봇 올려놓기
        if not robot[0] and belt[0] > 0:
            robot[0] = 1
            belt[0] -= 1
            # 내구도 체크
            if belt[0] == 0:
                count += 1

        # 종료 확인
        if count >= limit:
            sys.stdout.write(str(step))
            return

if __name__ == "__main__":
    main()
