import sys

def dfs(vertex, depth):
    stack = [(vertex, depth)]
    count = 1

    while stack:
        vertex, depth = stack.pop()
        if visited[vertex] == 0:
            deep[vertex] = depth
            visited[vertex] = count
            count += 1

            for v in nodes[vertex]:
                if visited[v] == 0:
                    stack.append((v, depth + 1))

if __name__ == "__main__":
    data = sys.stdin.read().splitlines()
    node, link, start = map(int, data[0].split())
    nodes = [[] for _ in range(node + 1)]
    visited = [0] * (node + 1)
    deep = [-1] * (node + 1)

    for i in data[1:]:
        vertex1, vertex2 = map(int, i.split())
        nodes[vertex1].append(vertex2)
        nodes[vertex2].append(vertex1)

    for i in range(1, node + 1):
        nodes[i].sort(reverse = True)

    dfs(start, 0)

    result = [a * b for a, b in zip(visited[1:], deep[1:])]

    sys.stdout.write(str(sum(result)))
