import sys

def main():
    data = list(map(int, sys.stdin.read().splitlines()))
    print(data)
    stack = []
    result = []
    j = 1

    for i in range(1, data[0] + 1):
        stack.append(i)
        result.append("+")
        print("PUSH")

        while j < data[0] + 1 and stack and stack[-1] == data[j]:
            stack.pop()
            result.append("-")
            j+=1
            print(f"POP and j = {j}")

    if stack:
        print(stack)
        sys.stdout.write("NO")
    else:
        sys.stdout.write("\n".join(result))

if __name__ == "__main__":
    main()