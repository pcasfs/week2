from queue import Queue

# 그래프 구성
def create_graph():
    # Vertex 입력받기
    vertices = input("Vertex (정점들 입력, 예: A, B, C, D): ").split(", ")
    
    # Edge 입력받기
    edges_input = input("Edges (간선들 입력, 예: A-B, A-C, B-D, C-D, C-E, D-F, E-H, E-G, G-H):  ").split(", ")
    
    # 인접 리스트 초기화
    adj_list = {v: [] for v in vertices}
    
    # Edge 정보로 인접 리스트 생성
    for edge in edges_input:
        u, v = edge.split("-")
        # 정점이 vertices에 없으면 추가
        if u not in adj_list:
            adj_list[u] = []
        if v not in adj_list:
            adj_list[v] = []
        # 간선을 추가
        adj_list[u].append(v)
        adj_list[v].append(u)
    
    # 인접 리스트를 정렬 (일관성 있는 탐색 순서 보장)
    for key in adj_list:
        adj_list[key].sort()
    
    return list(adj_list.keys()), adj_list

# DFS 구현
def DFS(vtx, adj_list, start):
    visited = set()
    stack = [start]
    dfs_result = []

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            dfs_result.append(node)
            # 스택은 역순으로 추가해야 DFS가 올바르게 작동
            stack.extend(sorted(adj_list[node], reverse=True))
    return dfs_result

# BFS 구현
def BFS(vtx, adj_list, start):
    visited = set()
    queue = Queue()
    queue.put(start)
    bfs_result = []

    while not queue.empty():
        node = queue.get()
        if node not in visited:
            visited.add(node)
            bfs_result.append(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    queue.put(neighbor)
    return bfs_result

# 연결 성분 계산
def find_connected_components(vtx, adj_list):
    visited = set()
    components = []

    for node in vtx:
        if node not in visited:
            component = BFS(vtx, adj_list, node)  # BFS로 연결 성분 탐색
            components.append(component)
            visited.update(component)
    return components

# BFS 기반 스패닝 트리
def spanning_tree_bfs(vtx, adj_list, start):
    visited = set()
    tree_edges = []
    queue = Queue()
    queue.put(start)
    visited.add(start)

    while not queue.empty():
        node = queue.get()
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                tree_edges.append((node, neighbor))
                visited.add(neighbor)
                queue.put(neighbor)
    return tree_edges

# DFS 기반 스패닝 트리
def spanning_tree_dfs(vtx, adj_list, start):
    visited = set()
    tree_edges = []

    def dfs(node):
        visited.add(node)
        for neighbor in adj_list[node]:
            if neighbor not in visited:
                tree_edges.append((node, neighbor))
                dfs(neighbor)

    dfs(start)
    return tree_edges

# Main
def main():
    # 그래프 입력받기
    vertices, adj_list = create_graph()

    # DFS와 BFS 수행
    dfs_result = DFS(vertices, adj_list, vertices[0])  # 첫 정점부터 탐색
    bfs_result = BFS(vertices, adj_list, vertices[0])  # 첫 정점부터 탐색

    # 연결 성분 계산
    connected_components = find_connected_components(vertices, adj_list)

    # BFS 및 DFS 기반 스패닝 트리 계산
    spanning_tree_edges_bfs = spanning_tree_bfs(vertices, adj_list, vertices[0])
    spanning_tree_edges_dfs = spanning_tree_dfs(vertices, adj_list, vertices[0])

    # 결과 출력
    print("DFS:", " - ".join(dfs_result))
    print("BFS:", " - ".join(bfs_result))
    print("연결 성분의 개수:", len(connected_components))
    print("Connected Components (BFS):")
    for component in connected_components:
        print(" - ".join(component))

    print("Spanning Tree (BFS):")
    for edge in spanning_tree_edges_bfs:
        print(f"{edge[0]} - {edge[1]}")

    print("Spanning Tree (DFS):")
    for edge in spanning_tree_edges_dfs:
        print(f"{edge[0]} - {edge[1]}")

# 실행
if __name__ == "__main__":
    main()
