INF = 9999

# 최단 경로 테이블 출력
def printA(A):
    vsize = len(A)
    print("====================================")
    for i in range(vsize):
        for j in range(vsize):
            if A[i][j] == INF:
                print(" INF ", end="")
            else:
                print("%4d " % A[i][j], end="")
        print("")

# 경로 복원을 위한 경로 추적 함수
def reconstruct_path(P, start, end):
    if P[start][end] == -1:  # 경로가 존재하지 않는 경우
        return None
    path = [start]
    while start != end:
        start = P[start][end]
        path.append(start)
    return path

# Floyd 알고리즘 수정: 경로 복원 포함
def shortest_path_floyd(vertex, adj):
    vsize = len(vertex)  # 정점의 개수

    A = [list(row) for row in adj]  # 가중치 행렬 복사
    P = [[-1 if adj[i][j] == INF or i == j else j for j in range(vsize)] for i in range(vsize)]  # 경로 추적 행렬 초기화

    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]
                    P[i][j] = P[i][k]  # 경로 갱신
        printA(A)  # 진행 상황 출력

    return A, P  # 최단 거리와 경로 정보를 반환

if __name__ == "__main__":
    # 그래프 정의
    vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    weight = [
        [0, 7, INF, INF, 3, 10, INF],
        [7, 0, 4, 10, 2, 6, INF],
        [INF, 4, 0, 2, INF, INF, INF],
        [INF, 10, 2, 0, 11, 9, 4],
        [3, 2, INF, 11, 0, 13, 5],
        [10, 6, INF, 9, 13, 0, INF],
        [INF, INF, INF, 4, 5, INF, 0],
    ]

    print("Shortest Path By Floyd's Algorithm")
    A, P = shortest_path_floyd(vertex, weight)  # 최단 거리와 경로 정보 계산

    # 사용자 입력 처리
    start_vertex = input("Start Vertex: ").strip().upper()
    end_vertex = input("End Vertex: ").strip().upper()

    if start_vertex in vertex and end_vertex in vertex:
        start = vertex.index(start_vertex)
        end = vertex.index(end_vertex)

        if A[start][end] == INF:
            print(f"* No path exists between {start_vertex} and {end_vertex}.")
        else:
            path_indices = reconstruct_path(P, start, end)
            path = " -> ".join(vertex[i] for i in path_indices)
            print(f"* Shortest Path: {path}")
            print(f"* Distance of the Shortest Path: {A[start][end]}")
    else:
        print("Invalid vertices entered. Please try again.")
