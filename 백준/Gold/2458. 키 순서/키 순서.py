import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

N, M = map(int, input().split())

# --- 그래프 초기화: 인접 리스트 (노드 1..N)
adj = [[] for _ in range(N+1)]   # 정방향: a -> b (a < b)
rev = [[] for _ in range(N+1)]   # 역방향: b -> a (b의 부모들)

for _ in range(M):
    a, b = map(int, input().split())
    adj[a].append(b)
    rev[b].append(a)

# ---------------------------------------------------------
# dfs_count: 오직 '한 방향(graph)에서 node로부터 도달 가능한 노드 수'만 반환한다.
# -> 이 함수는 "하나의 책임"만 갖는다.
# ---------------------------------------------------------
def dfs_count(node, graph, visited):
    """
    node에서 출발해 graph(정방향 또는 역방향)으로 방문 가능한
    (나 자신 제외) 노드의 개수를 반환.
    """
    count = 0
    for nxt in graph[node]:
        if not visited[nxt]:
            visited[nxt] = True
            count += 1
            # 재귀 호출이 반환하는 값(하위에서 새로 방문한 개수)을 더한다.
            count += dfs_count(nxt, graph, visited)
    return count
    # --> 여기에서 탐색이 끝나면 (for문이 끝나면) 자연스럽게 반환됨
    # --> 이 함수는 "더 이상 갈 곳이 없다"는 종료 조건을 따로 쓰지 않아도 된다.
    # 이 함수는 '정방향 전용' 또는 '역방향 전용'으로만 호출되어야 함.
    # <-- 이 부분이 바로 "이건 구분해야 함" 이다.

# ---------------------------------------------------------
# 메인: 각 노드에 대해 정방향(나보다 큰 사람)과 역방향(나보다 작은 사람) 각각 탐색
# ---------------------------------------------------------
answer = 0
for i in range(1, N+1):
    # --- i보다 큰 사람 수 (정방향)
    visited = [False] * (N+1)
    visited[i] = True
    big = dfs_count(i, adj, visited)   # 이 호출은 "정방향 역할"만 담당.  # 이건 구분해야 함

    # --- i보다 작은 사람 수 (역방향)
    visited = [False] * (N+1)
    visited[i] = True
    small = dfs_count(i, rev, visited) # 이 호출은 "역방향 역할"만 담당.  # 이건 구분해야 함

    if big + small == N - 1:
        answer += 1

print(answer)
