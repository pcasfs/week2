from BinaryTree import *
from BinSrchTree import *
from AVLTree import *
from CircularQueue import *

# 레벨 순회 함수
def levelorder(root):
    if root is None:
        return

    queue = CircularQueue(100)  # 큐의 크기 지정
    queue.enqueue(root)  # 루트 노드를 큐에 넣음

    while not queue.isEmpty():
        # 큐에서 노드를 하나 꺼내고, 그 노드의 key 값 출력
        node = queue.dequeue()
        if node is not None:
            print(node.key, end=' ')
            
            # 왼쪽 자식이 있으면 큐에 넣음
            if node.left:
                queue.enqueue(node.left)
                
            # 오른쪽 자식이 있으면 큐에 넣음
            if node.right:
                queue.enqueue(node.right)

if __name__ == "__main__":
    # 초기 데이터 삽입
    node = [7, 8, 9, 2, 1, 5, 3, 6, 4]
    root = None
    for i in node:
        n = BSTNode(i)
        if root is None:
            root = n
        else:
            root = insert_avl(root, n)

        print("AVL(%d): " % i, end="")
        levelorder(root)
        print()

    # 트리 정보 출력
    print("\n노드의 개수 =", count_node(root))
    print("단말의 개수 =", count_leaf(root))
    print("트리의 높이 =", calc_height(root))

    # 삭제 연산 테스트
    keys_to_delete = [9, 5, 7]
    for key in keys_to_delete:
        print(f"\nDeleting {key}...")
        root = delete_avl(root, key)
        print("AVL Tree after deleting %d: " % key, end="")
        levelorder(root)
        print()

    # 삭제 후 트리 정보 출력
    print("\n노드의 개수 =", count_node(root))
    print("단말의 개수 =", count_leaf(root))
    print("트리의 높이 =", calc_height(root))
