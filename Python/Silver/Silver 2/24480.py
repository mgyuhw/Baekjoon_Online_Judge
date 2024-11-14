import sys

def dfs(vertex):
    stack = [vertex]
    count = 1

    while stack:
        vertex = stack.pop()
        if not visited[vertex]:
            visited[vertex] = count
            count += 1
            stack.extend(sorted(nodes[vertex]))

if __name__ == "__main__":
    data = sys.stdin.read().splitlines()
    node, link, start = map(int, data[0].split())
    nodes = [[] for _ in range(node + 1)]
    visited = [0] * (node + 1)

    for i in data[1:]:
        vertex1, vertex2 = map(int, i.split())
        nodes[vertex1].append(vertex2)
        nodes[vertex2].append(vertex1)

    dfs(start)

    sys.stdout.write('\n'.join(map(str, visited[1:])))