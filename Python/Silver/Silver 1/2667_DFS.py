import sys

def dfs(y, x, space):
    space += 1

    for dy, dx in direction:
        ny = y + dy
        nx = x + dx

        if 0 <= nx < width and 0 <= ny < width and matrix[ny][nx]:
            matrix[ny][nx] = 0
            space = dfs(ny, nx, space)

    return space

if __name__ == "__main__":
    width = int(sys.stdin.readline())
    matrix = [list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(width)]
    direction = ((-1, 0), (0, 1), (1, 0), (0, -1))
    count = 0
    result = []

    for i in range(width):
        for j in range(width):
            if matrix[i][j]:
                matrix[i][j] = 0
                count += 1
                area = dfs(i, j, 0)
                result.append(area)

    sys.stdout.write(str(count) + '\n')
    sys.stdout.write('\n'.join(map(str, sorted(result))))
