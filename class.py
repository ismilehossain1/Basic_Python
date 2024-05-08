# a=int(input("INTER YOUR NUMBE : "))
# print(a)
# b=int(input("INTER YOUR NUMBE : "))
# print(b)
# c=int(input("INTER YOUR NUMBE : "))
# print(c)
from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a - 1].append(b - 1)  # Convert 1-based indexing to 0-based indexing
    graph[b - 1].append(a - 1)

visited = [False] * n
parent = [-1] * n
queue = deque([0])
visited[0] = True

while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if not visited[neighbor]:
            visited[neighbor] = True
            parent[neighbor] = node
            queue.append(neighbor)

# Reconstruct the path from end to start
path = []
while n - 1 != -1:
    path.append(n - 1)  # Convert back to 0-based indexing
    n = parent[n - 1]

if path[-1] == 0:
    print(len(path))
    print(*path[::-1])  # Reverse the path to get start to end order
else:
    print("IMPOSSIBLE")
