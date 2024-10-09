# import sys
#
# """
# Dynamic Programming을 이용한 최장 감소 부분 수열
# 다만 이 방법은 O(n^2)이므로 오래 걸린다.
# Bottom - Up 방식의 DP이다.
#
# 수열의 첫번째 병사가 들어가고 시작하니 memo를 1로 초기화한다. (수열의 길이는 1부터)
# 수열에서 다음에 올 병사의 전투력이 이전의 병사보다 약할 경우, 그 수의 memo를 읽어 1을 더한 값과 본인의 memo와 비교
# 더 큰 값을 본인의 memo에 저장한다.
# 이를 반복해 가장 큰 memo를 count와 뺄셈 연산을 해주면 제외된 병사의 수가 나온다.
#
# 왜... 왜 풀리는거지...?
# """
# def main():
#     # Data Input
#     count = int(sys.stdin.readline())
#     data = list(map(int, sys.stdin.readline().split()))
#
#     # Memo variable for Memoization
#     memo = [1 for _ in range(count)]
#
#     # Bottom - Up Dynamic Programming
#     for i in range(1, count):
#         for j in range(0, i):
#             # Recurrence Relation
#             if data[i] < data[j]:
#                 memo[i] = memo[j] + 1 if memo[j] + 1 > memo[i] else memo[i]
#
#     sys.stdout.write(str(count - max(memo)))
#
# if __name__ == "__main__":
#     main()

import sys

"""
이진탐색을 이용한 최장 감소 부분 수열

기존의 bisect 라이브러리는 오름차순에서 사용이 가능
따라서 내림차순에서 사용이 가능한 이진탐색 함수 작성
"""

def custom_binary_search(arr, target):
    start = 0
    end = len(arr) - 1

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target: return mid
        elif arr[mid] > target: start = mid + 1
        else: end = mid - 1

    return start

def main():
    # Data Input
    count = int(sys.stdin.readline())
    data = list(map(int, sys.stdin.readline().split()))

    # Memo variable for Memoization
    memo = [data[0]]

    # Binary Search
    for i in range(1, count):
        # print(i)
        # Recurrence Relation
        if data[i] < memo[-1]:
            memo.append(data[i])
            # print(memo)
        else:
            # print(f"data : {data[i]}\nbinary : {custom_binary_search(memo, data[i])}")
            memo[custom_binary_search(memo, data[i])] = data[i]

    sys.stdout.write(str(count - len(memo)))

if __name__ == "__main__":
    main()
