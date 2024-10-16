import sys

def main():
    number = int(sys.stdin.readline().rstrip())

    for i in range(number):
        data = sys.stdin.readline().rstrip()
        stack = []

        for j in data:
            if j == "(":
                stack.append(j)
            elif j == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack = True
                    break

        sys.stdout.write("NO\n" if stack else "YES\n")

if __name__ == "__main__":
    main()

"""
예제 2를 보면 알 수 있겠지만, 개수를 보면 아니된다.
"""