"""
랭크에 있는 코드를 참고하여 고친 코드입니다.

1. 반복되는 문자열 출력 코드 줄임
2. if else를 사용, 재귀를 만족하는 조건을 참으로 올려 반복을 줄여보려고 하였음.
"""
import sys

def repeat(num, limit = 0):
    sys.stdout.write("_" * 4 * limit + """"재귀함수가 뭔가요?"\n""")

    if limit < num:
        sys.stdout.write("_" * 4 * limit + """"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n""")
        sys.stdout.write("_" * 4 * limit + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n")
        sys.stdout.write("_" * 4 * limit + """그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."\n""")
        repeat(num, limit + 1)
    else:
        sys.stdout.write("_" * 4 * limit + """"재귀함수는 자기 자신을 호출하는 함수라네"\n""")

    sys.stdout.write("_" * 4 * limit + "라고 답변하였지.\n")

if __name__ == "__main__":
    count = int(sys.stdin.readline())
    sys.stdout.write("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.\n")
    repeat(count)
