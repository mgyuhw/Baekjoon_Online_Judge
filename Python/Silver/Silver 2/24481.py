import sys

def dfs(vertex):
    stack = [vertex]
    count = 0

    while stack:
        vertex = stack.pop()
        if visited[vertex] == -1:
            visited[vertex] = count
            for v in nodes[vertex]:
                if visited[v] == -1:
                    stack.append(v)
        count += 1

if __name__ == "__main__":
    data = sys.stdin.read().splitlines()
    node, link, start = map(int, data[0].split())
    nodes = [[] for _ in range(node + 1)]
    visited = [-1] * (node + 1)

    for i in data[1:]:
        vertex1, vertex2 = map(int, i.split())
        nodes[vertex1].append(vertex2)
        nodes[vertex2].append(vertex1)

    for i in range(1, node + 1):
        nodes[i].sort(reverse = True)

    dfs(start)

    sys.stdout.write('\n'.join(map(str, visited[1:])))
