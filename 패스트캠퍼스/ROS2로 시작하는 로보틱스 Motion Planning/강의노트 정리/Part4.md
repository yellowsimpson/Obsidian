# Chapter 1. 그래프
## 1. 그래프
#### 1. 그래프
- 정의: Vertex(V)와 Edge(E)로 이루어진 순서쌍(V, E)
필수 용어
- 가중치(weight)
- 차수(degree): 차수로 많을 수록 연결되어 있는 노드가 많음
- 경로(path)

```python
import networkx as nx

G = np.Graph()
nodes = ['A', 'B', 'C', 'D']
edges = [
	('A', 'B'), ('A', 'C'),
	('B', 'D'), ('C', 'D'),
	('B', 'C') 
	]
G.add_nodes_from(nodes)
G.add_edges_from(edges)
```
#### 2. 방향성 그래프(Directed-Graph)
	->그래프에 방향성이 추가됨
필수 용어
- 차수(degree): 차수로 많을 수록 연결되어 있는 노드가 많음
	- outbound degree(나가는 차수)
	- inbound degree(들어오는 차수)
	- degree = outbound degree + inbound degree
- 경로(path)
- 사이클(cycle): motion planning에서는 cycle을 피해야되는 경향이 있음
			-> cycle이 생기면 원하는 곳으로 못갈 수 있음

## 2. 알고리즘의 필요성
__테스크 -> 데이터 구조로 문제를 정의(그래프) -> 경로 탐색 -> 경로(루트)__


## 3. 트리
트리(tree)
- 모든 노드(Vertex) 들이 연결되어 있을 것
- Cycle이 없어야 할 것
필수 용어
- 루트(root)
- 리프(leaf)
- 부모 & 자식(parent & child)
- 차수(degree)
- 경로(path)
- 깊이(depth, level)
- 높이(height)
- 조상(ancestor)
- 후손(descendnat)

결정 트리 예시 코드
```python
import networkx as nx

G = nx.DiGraph()
tree_nodes = ['A', 'B', 'C', 'D']
tree_edges = [
	('A', 'B'), ('A', 'C'),('A', 'D'),
	('B', 'E'), ('B', 'F'),
	('D', 'G') 
	]
G.add_nodes_from(nodes)
G.add_edges_from(edges)
```

# Chapter 2. 기본 서치 알고리즘

## 1. 강의 요약
데이터구조와 트리에 대해서 배움T
## 2. 탐색의 기초
### 1. 들락날락(BFS)
### 2. 깊이 들어가보고 없으면 다시 돌아오기(DFS)
## 3. BFS
BFS(Breadth Frist Search): 먼저 들어간 친구는 먼저 나온다

```python
from collections import deque

queue = deque()
queue.append("A")
queue.appendleft("B")
queue.pop()
queue.deque()
queue.popleft()
```
BFS 특징
- 시간 복잡도: O(V + E)
- 공간 복잡도: O(V)
- 목표 노드가 시작점 근처에 있을 때 빠르게 발견 가능
- 가중치가 모두 동일할 경우 최단 경로 탐색 가능

BFS 수도 코드로 보는 예시

```python
graph = {
	'A' : ['B', 'C'],
	'B' : ['A', 'D', 'E'],
	'C' : ['A', 'F'],
	'D' : ['B'],
	'E' : ['B', 'G'],
	'F' : ['C'],
	'G' : ['E']
 	}
 
 bfs(graph, start='A')
```


```python
from collections import deque

def bfs(graph, start_node):
	visited = set()
	qieie = deque()
	
	queue.append(start_node)
	visited.add(start_node)
	
	while queue:
		current_node = queue.popleft()
		
		for neighbor in graph.get(current_node, []):
			if neighbor not in visited:
				queue.append(neighbor)
				visited.add(neighbor)
```

```python
from collections import deque

def bfs_path(graph, start, goal):
    visited = set()
    queue = deque()
    parent = {}

    queue.append(start)
    visited.add(start)
    parent[start] = None

    while queue:
        current = queue.popleft()

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                parent[neighbor] = current
                queue.append(neighbor)
```

## 4. 스택 설명 수정
```python
from collections import deque

queue = deque()
queue.append("A")
queue.appendleft("B")
queue.pop()
queue.deque()
queue.popleft()
```

deque를 옆으로 누워있는 원통 형태라고 생각

append, pop => 오른쪽에서 오는거라고 생각
appendleft, popleft => 왼쪽과 관련있는거라고 생각

__보통 append(오른쪽으로 들어옴)와 popleft(왼쪽으로 나옴)를  사용__
## 5.  DFS
DFS(Depth Fist Search): 가장 나중에 들어온 친구가 가장 먼저 나온다.
- Stack: Last in Frist Out(LIFO)

특징:
- 시간 복잡도: O(V + E)
- 공간 복잡도: O(V)
	일반적으로 BFS보다
	메모리 사용량이 낮음
- 일반적으로 최단 경로를 보장하지 않음


DFS 수도 코드로 보는 예시

```python
graph = {
	'A' : ['B', 'C'],
	'B' : ['D', 'E'],
	'C' : ['F'],
	'D' : [],
	'E' : ['F'],
	'F' : []
 	}
 
path = dfs(graph, 'A', 'F')
```

```python
def dfs(graph, start, goal):
	visited = set()
	stack = [start]
	
	while stack:
		current = stack.pop()
		
		if current == goal:
			return True #path가 있는지 확인
		
		if current not in visited:
			visited.add(current)	
			for neighbor in graph.get(current, []):
				if neighbor not in visited:
				stack.append(neighbor)
				
		return False
```

```python
def dfs(graph, start, goal):
	stack = [(start, [start])]
	visited = set()

    while stack:
        current, path = stack.pop()

        if current == goal:
	        return path
	        
        if current not in visited:
	        visited.add(current)   
	        for neighbor in graph.get(current, []):
	            if neighbor not in visited:
		            stack.append((neighbor, path + [neighbor]))
return None
```
## 6. 강의 요약
- 데이터 구조: Queue
- BFS
- Stack
- DFS

# Chapter 3. 최단 경로 알고리즘

## 1. 이전 강의 요약
- 데이터 구조: Queue
	- FIFO
- BFS
	- Queue
	- 시간 복잡도
	- 공간 복잡도
	- 목표 노드가 시작점 근처에 있을 때
	- 가중치가 모두 동일할 경우 최단 경로 탐색 가능
- Stack
	- LIFO
- DFS
	- Stack 사용
	- 시간 복잡도: O(V + E)
	- 공간 복잡도: O(V)
		일반적으로 BFS보다 메모리 사용량이 낮음
	- 일반적으로 최단 경로를 보장하지 않음
## 2. 강의 개요
짧은 경로를 찾는 알고리즘에 대해 공부할것!
## 3. pq 설명
### 다익스트라 알고리즘(Dijkstra Algorithm)
Priority Queue: First in First OUT(FIFO)
## 4. Dijkstra
특징:
- priority Queue 사용
- 가중치가 양수인 경우 항상 최단경로를 찾을 수 있음
- 시간 복잡도: O((V + E)log V)
- 공간 복잡도: O(V + E)

Dijkstra 알고리즘을 실행하는 예제 code

```python
import networkx as nx
from networkx.algorithms.shortest_paths.weighted import dijkstra

# 그래프 생성
G = nx.Graph()

# 노드 추가 (V1 ~ V10)
nodes = [f"V{i}" for i in range(1, 11)]
G.add_nodes_from(nodes)

# 엣지 추가
edges = [
    ("V1", "V2"), ("V1", "V3"), ("V2", "V4"), ("V2", "V5"),
    ("V3", "V6"), ("V3", "7"), ("V4", "V8"), ("V5", "V8"),
    ("V6", "V9"), ("V7", "V9"), ("V8", "V10"), ("V9", "V10"),
    ("V5", "V6"), ("V2", "V3")
]
G.add_edges_from(edges)

# 각 엣지에 가중치(weight) 기본값 1 부여
for u, v in G.edges():
    G[u][v]['weight'] = 1

# Dijkstra 알고리즘 실행
distances, predecessors = dijkstra(G, source="V1")

print("최단 거리:", distances)
print("이전 노드:", predecessors)
```
```python
import heapq

def dijkstra(graph, source):
    # 거리와 이전 노드 초기화
    dist = {node: float('inf') for node in graph}
    prev = {node: None for node in graph}
    dist[source] = 0

    # 우선순위 큐 (priority queue)
    pq = [(0, source)]

    while pq:
        # 현재 노드와 거리 추출
        current_dist, u = heapq.heappop(pq)

        # 더 긴 경로는 무시
        if current_dist > dist[u]:
            continue

        # 인접 노드 탐색
        for v, weight in graph[u].items():
            new_dist = current_dist + weight
            if new_dist < dist[v]:
                dist[v] = new_dist
                prev[v] = u
                heapq.heappush(pq, (new_dist, v))

    return dist, prev
```

## 5. 휴리스틱
휴리스틱 
- 목표 지점까지의 거리를 근사
- Admissible: 실제 최단 경로 비용보다 과대평가(overestimate) 하지 않아야 함.
```python
h(n) <= 실제 최단거리(n -> goal)
```
-  Consistency:  휴리스틱에 의해 선택된 노드는 실제 목표 지점에 가까워지고 있어야 함.
```python
h(n) <= w(n, m) + h(m)
```
## 6. Astar
## 🧭 1️⃣ A* 알고리즘이란?

**A*** 알고리즘은 **최단 경로 탐색 알고리즘**이에요.  
즉, 시작점에서 목표점까지 가는 **가장 짧은 경로**를 찾는 방법입니다.

> 🚀 핵심 아이디어:  
> 단순히 “지금까지 온 거리”뿐 아니라,  
> “앞으로 남은 거리의 예측값”도 함께 고려한다는 점입니다.

이게 다익스트라와의 큰 차이예요.  
그래서 A*는 다익스트라보다 **더 빠르고 효율적**하게 목표까지 도달할 수 있습니다.

A* star알고리즘 특징:
- Priority Queue 사용
- 가중치가 양수인 경우 항상 최단경로를 찾을 수 있음
- 시간 복잡도와 공간 복잡도가 휴리스틱의 성능에 따라서 크게 달라짐

## 7. A* star 수도코드
```python
import networkx as nx
import math

# 그래프 생성
G = nx.Graph()
nodes = [f"V{i}" for i in range(1, 11)]
G.add_nodes_from(nodes)

edges = [
    ("V1", "V2"), ("V1", "V3"), ("V2", "V4"), ("V2", "V5"),
    ("V3", "V6"), ("V3", "V7"), ("V4", "V8"), ("V5", "V8"),
    ("V6", "V9"), ("V7", "V9"), ("V8", "V10"), ("V9", "V10"),
    ("V5", "V6"), ("V2", "V3")
]
G.add_edges_from(edges)

# 각 엣지에 weight 부여 (순서대로 1, 2, 3, ...)
for i, (u, v) in enumerate(edges, start=1):
    G[u][v]['weight'] = i

# 노드 위치 (시각화용, 좌표 기반 휴리스틱 계산)
pos = nx.spring_layout(G, seed=42)

# 휴리스틱 함수 정의 (목표 V10까지의 유클리드 거리)
def heuristic(n):
    return math.dist(pos[n], pos["V10"])

# A* 알고리즘 실행
path = nx.astar_path(G, source="V1", target="V10", heuristic=heuristic, weight="weight")

print("Found path:", path)
```
```python
def astar(G, start, goal, h):
    open_set = {start}
    closed_set = set()
    g_score = {v: float('inf') for v in G.nodes()}
    f_score = {v: float('inf') for v in G.nodes()}
    parent = {}

    g_score[start] = 0
    f_score[start] = h(start)

    while open_set:
        current = min(open_set, key=lambda v: f_score[v])

        if current == goal:
            return reconstruct_path(parent, current)

        open_set.remove(current)
        closed_set.add(current)

        for neighbor in G.neighbors(current):
            if neighbor in closed_set:
                continue

            cost = G[current][neighbor].get('weight', 1)
            tentative_g = g_score[current] + cost

            if tentative_g < g_score[neighbor]:
                parent[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + h(neighbor)

                if neighbor not in open_set:
                    open_set.add(neighbor)

    return None


def reconstruct_path(parent, node):
    path = [node]
    while node in parent:
        node = parent[node]
        path.append(node)
    return path[::-1]

```
## 8. Dijkstra&Astar

| Dijkstra Algorithm                                                                                            | Astar Algorithm                                                                                     |
| ------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| - Priority Queue (FIFO)<br>- 시간 복잡도: O((V + E) log V)<br>- 공간 복잡도: O(V + E)<br>- 가중치가 양수인 경우 항상 최단경로를 찾을 수 있음 | - Priority Queue (FIFO)<br>- 가중치가 양수인 경우 항상 최단경로를 찾을 수 있음<br>- 시간 복잡도와 공간 복잡도가 휴리스틱의 성능에 따라서 크게 달라짐 |



