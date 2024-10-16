import sys

def main():
    data = list(sys.stdin.readline().rstrip())
    data.reverse()
    stack = []

    while data:
        value = data.pop()

        if value.isdigit():
            stack.append(value)
        else:
            operand_1, operand_2 = stack.pop(), stack.pop()
            stack.append(str(int(eval(f"{operand_2} {value} {operand_1}"))))

    sys.stdout.write(stack.pop())

if __name__ == "__main__":
    main()
