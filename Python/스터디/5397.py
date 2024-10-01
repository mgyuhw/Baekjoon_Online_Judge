import sys

def main():
    data = sys.stdin.read().splitlines()

    for i in range(1, int(data[0]) + 1):
        word = data[i]
        stack = []
        dispenser = []

        for j in word:
            if j.isalnum():
                stack.append(j)
            elif j == '-':
                if stack: stack.pop()
            elif j == '<':
                if stack: dispenser.append(stack.pop())
            elif j == '>':
                if dispenser: stack.append(dispenser.pop())

        sys.stdout.write(''.join(stack) + ''.join(reversed(dispenser)) + '\n')

if __name__ == "__main__":
    main()
