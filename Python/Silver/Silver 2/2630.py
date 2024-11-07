import sys

def divide(side, matrix, color):
    colored = any(1 in value for value in matrix)
    white = any(0 in value for value in matrix)

    if colored and white:
        side //= 2
        divide(side, [row[:side] for row in matrix[:side]], color)
        divide(side, [row[side:] for row in matrix[:side]], color)
        divide(side, [row[:side] for row in matrix[side:]], color)
        divide(side, [row[side:] for row in matrix[side:]], color)
    elif not colored:
        color[0] += 1
        return
    elif not white:
        color[1] += 1
        return

if __name__ == "__main__":
    n = int(sys.stdin.readline())
    paper = [list(map(int, row.split())) for row in sys.stdin.read().splitlines()]
    color = [0, 0]
    divide(n, paper, color)

    sys.stdout.write('\n'.join(map(str, color)))
