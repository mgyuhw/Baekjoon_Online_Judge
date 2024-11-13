import sys

sys.setrecursionlimit(300000)

g_dx = (0, 1, 0, -1)
g_dy = (-1, 0, 1, 0)
g_width = g_height = g_area = 0
g_matrix = []

def dfs(y, x):
    global g_area
    g_area += 1

    for i in range(4):
        nx = x + g_dx[i]
        ny = y + g_dy[i]
        # print(f"nx {nx}, ny {ny}")

        if 0 <= nx < g_width and 0 <= ny < g_height and g_matrix[ny][nx]:
            g_matrix[ny][nx] = 0
            dfs(ny, nx)
            # print(f"dfs visited {g_visited}\n")

def main():
    global g_width, g_height, g_matrix, g_area

    g_height, g_width = map(int, sys.stdin.readline().split())

    g_matrix = [[0] * g_width for _ in range(g_height)]
    count = area = 0

    for i in range(g_height):
        g_matrix[i] = list(map(int, sys.stdin.readline().split()))

    for i in range(g_height):
        for j in range(g_width):
            if g_matrix[i][j]:
                g_matrix[i][j] = 0
                # print(f"main visitied {g_visited}\n")
                # print(i, j)
                dfs(i, j)
                count += 1
                area = area if area > g_area else g_area
                g_area = 0

    # g_area = area if area > g_area else g_area
    sys.stdout.write(str(count) + "\n" + str(area))

if __name__ == "__main__":
    main()
