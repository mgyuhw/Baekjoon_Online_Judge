import sys
from collections import deque

sys.setrecursionlimit(3000)

g_dx = (-1, 0, 1, -1, 1, -1, 0, 1)
g_dy = (-1, -1, -1, 0, 0, 1, 1, 1)
g_width = g_height = 0
g_matrix = g_visited = []

# def bfs(y, x):
#     queue = deque()
#     queue.append((y, x))
#
#     while queue:
#         y, x = queue.popleft()
#         for i in range(8):
#             nx = x + g_dx[i]
#             ny = y + g_dy[i]
#             # print(f"nx {nx}, ny {ny}")
#
#             if 0 <= nx < g_width and 0 <= ny < g_height and g_matrix[ny][nx] and not g_visited[ny][nx]:
#                 g_visited[ny][nx] = True
#                 queue.append((ny, nx))
#                 # print(f"dfs visited {g_visited}\n")
#
# def main():
#     global g_width, g_height, g_visited, g_matrix
#
#     while True:
#         g_width, g_height = map(int, sys.stdin.readline().split())
#         if g_width == 0 and g_height == 0: break
#
#         g_matrix = [[0] * g_width for _ in range(g_height)]
#         g_visited = [[False] * g_width for _ in range(g_height)]
#         count = 0
#
#         for i in range(g_height):
#             g_matrix[i] = list(map(int, sys.stdin.readline().split()))
#
#         for i in range(g_height):
#             for j in range(g_width):
#                 if not g_visited[i][j] and g_matrix[i][j]:
#                     g_visited[i][j] = True
#                     # print(f"main visitied {g_visited}\n")
#                     # print(i, j)
#                     bfs(i, j)
#                     count += 1
#
#         sys.stdout.write(str(count) + "\n")

"""
visited 안쓰고 하는 방법
지나간 땅을 바다로 바꾼다.
"""

def bfs(y, x):
    queue = deque()
    queue.append((y, x))

    while queue:
        y, x = queue.popleft()
        for i in range(8):
            nx = x + g_dx[i]
            ny = y + g_dy[i]
            # print(f"nx {nx}, ny {ny}")

            if 0 <= nx < g_width and 0 <= ny < g_height and g_matrix[ny][nx]:
                g_matrix[ny][nx] = 0
                queue.append((ny, nx))
                # print(f"dfs visited {g_visited}\n")

def main():
    global g_width, g_height, g_matrix

    while True:
        g_width, g_height = map(int, sys.stdin.readline().split())
        if g_width == 0 and g_height == 0: break

        g_matrix = [[0] * g_width for _ in range(g_height)]
        count = 0

        for i in range(g_height):
            g_matrix[i] = list(map(int, sys.stdin.readline().split()))

        for i in range(g_height):
            for j in range(g_width):
                if g_matrix[i][j]:
                    g_matrix[i][j] = 0
                    # print(f"main visitied {g_visited}\n")
                    # print(i, j)
                    bfs(i, j)
                    count += 1

        sys.stdout.write(str(count) + "\n")

if __name__ == "__main__":
    main()
