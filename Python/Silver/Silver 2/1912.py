# import sys
#
# """
# 주어진 수열의 모든 경우의 수를 계산
# 결과값은 memo 배열에 저장하여 재사용
# e.g., progression[0]부터 progression[3]까지의 합을 구할 때,
# 그 이전에 계산했던 [0]부터 [2]까지의 합을 메모에서 꺼내와 계산.
# 즉, progression[3] + memo[2]
# 단, 이 방법은 시간초과가 난다.
# """
# def main():
#     # Input Step
#     count = int(sys.stdin.readline())
#     progression = list(map(int, sys.stdin.readline().split()))
#
#     # Dynamic Programming Memoization Step
#     memo = []
#     result = -1000
#
#     # Bottom - Up Dynamic Programming
#     for i in range(count):
#         memo.clear()
#
#         for j in range(i, count):
#             if i == j:
#                 memo.append(progression[j])
#             else:
#                 memo.append(progression[j] + memo[len(memo) - 1])
#
#         result = max(memo) if result < max(memo) else result
#
#     sys.stdout.write(str(result))
#
#
# if __name__ == "__main__":
#     main()

import sys

def main():
    # Input Step
    count = int(sys.stdin.readline())
    progression = list(map(int, sys.stdin.readline().split()))

    # Memory variable for Memoization
    memo = [0] * count
    memo[0] = progression[0]
    # memo = [progression[0]]

    # Bottom - Up Dynamic Programming
    """
    주어진 수열의 모든 경우의 수를 계산
    단, 이전까지의 모든 합 + 다음 수 가 다음 수 단독보다 작을 경우
    다음 숫자를 그대로 memo에 저장.
    결과값은 memo 배열에 저장하여 재사용
    """

    for i in range(1, count):
        # 점화식, max 함수보다 if else가 조금 더 빠르다.
        memo[i] = memo[i - 1] + progression[i] if memo[i - 1] + progression[i] > progression[i] else progression[i]
        # memo.append(memo[i - 1] + progression[i] if memo[i - 1] + progression[i] > progression[i] else progression[i])

    sys.stdout.write(str(max(memo)))

if __name__ == "__main__":
    main()

"""
놀랍게도
낼 때마다 속도가 바뀐다...
60, 64, 56...

append? 인덱싱? 유의미한 속도 차이는 아니지만 조금의 차이가 있는 듯 하다.
인덱스를 사용해서 하는 것이 조금 더 빠른건가...?
"""