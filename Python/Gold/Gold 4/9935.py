import sys

def main():
    text = list(map(str, sys.stdin.readline().rstrip()))
    text.reverse()
    bomb = sys.stdin.readline().rstrip()
    stack = []
    bomb_len = len(bomb)

    while text:
        stack.append(text.pop())
        if len(stack) >= bomb_len:
            bomb_check = ''.join(stack[-bomb_len:])
            if bomb_check == bomb:
                for _ in range(bomb_len):
                    stack.pop()

    sys.stdout.write(''.join(stack) if stack else "FRULA")

if __name__ == "__main__":
    main()


"""
이이이잉
위에가 내 본연의 코드
리스트를 거꾸로 만들어 스택에 하나하나 넣어 풀기
길이 비교해서 일정 길이 되면 폭탄과 비교하기
"""

"""
아래는 랭킹 참고해서 만든 코드
리스트를 거꾸로 할 필요 없이 스트링을 반복문에 넣으면 처음부터 차례로 나옴
문자가 폭탄 마지막과 같으면, 폭탄 길이만큼 비교
맞으면 펑
"""

import sys

def main():
    text = sys.stdin.readline().strip()
    bomb = list(sys.stdin.readline().rstrip())
    stack = []
    bomb_len = len(bomb)

    for i in text:
        stack.append(i)
        if i == bomb[-1] and stack[-bomb_len:] == bomb:
            del stack[-bomb_len:]

    sys.stdout.write(''.join(stack) if stack else "FRULA")

if __name__ == "__main__":
    main()

