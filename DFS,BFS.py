# DFS 예제
def dfs(graph, v, visited):
    #현재 노드를 방문처리
    visited[v] = True
    print(v,end=' ')

    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)


# 각 노드가 방문된 정보를 리스트 자료형으로 표현(2차원 리스트)    
graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited=[False]*9

dfs(graph,1,visited)


#BFS 예제
from collections import deque

def bfs(graph, start, visited):
    #큐를 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    #현재 노드를 방문 처리
    visited[start] = True
    
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 하나의 원소를 뽑아 출력
        v= queue.popleft()
        print(v,end=' ')

        # 해당 원소와 연결된, 아직 방문하지 않은 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(2차원 리스트)    
graph=[[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현(1차원 리스트)
visited=[False]*9

bfs(graph,1,visited)  









