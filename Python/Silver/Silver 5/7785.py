import sys

def main():
    data = sys.stdin.read().splitlines()
    count = int(data[0])
    remain = {}

    for i in range(1, count + 1):
        name, state = data[i].split()

        if state == "enter": remain[name] = state
        else: del remain[name]

    sys.stdout.write("\n".join(sorted(remain.keys(), reverse = True)))

if __name__ == "__main__":
    main()

"""
리스트는 느리다. 딕셔너리를 사랑해보자.
변수 하나 만들어서 넣었던거 바로 넣었더니 4ms 줄었다. 이거 진짜냐...
"""