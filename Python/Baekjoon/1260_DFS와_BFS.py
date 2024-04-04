n, m, v = map(int, input().split())  # 정점의 개수, 간선의 개수, 시작 정점 번호

# 인접 리스트 초기화
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)  # 무방향 그래프이므로 양방향 추가

visited = [False] * (n + 1)  # 방문 리스트 초기화

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

dfs(graph, v, visited)
