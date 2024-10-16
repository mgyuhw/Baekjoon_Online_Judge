# import sys
#
# dict_num, question_num = map(int, sys.stdin.readline().split())
# pocket_dict = {}
#
# for i in range(1, dict_num + 1):
#     name = sys.stdin.readline().rstrip()
#
#     """
#     딕셔너리를 사용했으며, 숫자가 나와도, 이름이 나와도 출력 해줘야 하니 key와 value를 각기 넣었음.
#     또한 숫자의 경우 입력 받았을 때를 대비해 문자열로 변형시켜 저장하였다.
#     """
#
#     pocket_dict[str(i)] = name
#     pocket_dict[name] = str(i)
#
# print("Input Finish")
# for i in range(1, question_num + 1):
#     question = sys.stdin.readline().rstrip()
#
#     print(pocket_dict[question])


"""
백준에서 입력값을 복붙했더니
마지막이 잘 안되는데 백준에서는 된다.
직접 입력해봐도 잘 된다.
걱정 ㄴㄴ
"""

"""
대전 과학고 선생의 다른 방법을 위의 방법으로 해보자.
내가 가져온 방법은 입력을 계속 받는 것이 아닌 한번에 받아서 이것들을 처리하는 것이다.
"""

import sys
input = sys.stdin.read


def main():
    data = input().splitlines()

    # 첫 번째 줄에서 N과 M을 파싱
    N, M = map(int, data[0].split())

    # # 두 딕셔너리 선언
    # num_to_name = {}
    # name_to_num = {}

    # 한개의 딕셔너리 선언
    pocket_dict = {}

    # # N개의 포켓몬 이름 입력
    # for i in range(1, N + 1):
    #     name = data[i]
    #     num_to_name[i] = name
    #     name_to_num[name] = i

    # 한개의 딕셔너리에 key value 양쪽으로 저장
    for i in range(1, N + 1):
        pocket_dict[str(i)] = data[i]
        pocket_dict[data[i]] = str(i)

    # M개의 문제 입력 처리
    result = []
    for j in range(N + 1, N + M + 1):
        query = data[j]
    #     if query.isdigit():  # 숫자인 경우
    #         result.append(num_to_name[int(query)])
    #     else:  # 문자인 경우
    #         result.append(str(name_to_num[query]))
        result.append(pocket_dict[query])


    # 결과 출력
    sys.stdout.write("\n".join(result) + "\n")


# 실행
if __name__ == "__main__":
    main()

"""
이렇게 하면 빨라진건 맞으나 저분 처럼은 안된다.
딕셔너리를 따로 넣어야 더 빠른 듯 하다.
"""