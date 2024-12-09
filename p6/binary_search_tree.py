class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


class BSTMap:
    def __init__(self):
        self.root = None

    # 노드 삽입 메소드
    def insert(self, key, value):
        self.root = self._insert_value(self.root, key, value)

    def _insert_value(self, node, key, value):
        if node is None:
            return Node(key, value)
        if key < node.key:
            node.left = self._insert_value(node.left, key, value)
        elif key > node.key:
            node.right = self._insert_value(node.right, key, value)
        return node

    # 중위 순회 (과정 출력)
    def _inorder(self, node):
        if node:
            yield from self._inorder(node.left)
            print(f"방문: {node.key}")
            yield node.key
            yield from self._inorder(node.right)

    # 전위 순회 (과정 출력)
    def _preorder(self, node):
        if node:
            print(f"방문: {node.key}")
            yield node.key
            yield from self._preorder(node.left)
            yield from self._preorder(node.right)

    # 후위 순회 (과정 출력)
    def _postorder(self, node):
        if node:
            yield from self._postorder(node.left)
            yield from self._postorder(node.right)
            print(f"방문: {node.key}")
            yield node.key

    # 순회 과정 출력 메소드
    def display_with_steps(self, msg="BSTMap:", order=1):
        # order 값에 따라 순회 방식 선택
        order_name = {1: "중위 순회 (Inorder)", 2: "전위 순회 (Preorder)", 3: "후위 순회 (Postorder)"}
        print(f"{msg} ({order_name.get(order, 'BSTMap')}):")

        if order == 1:  # 중위 순회
            result = list(self._inorder(self.root))
        elif order == 2:  # 전위 순회
            result = list(self._preorder(self.root))
        elif order == 3:  # 후위 순회
            result = list(self._postorder(self.root))
        else:
            print("잘못된 순회 방식입니다.")
            return

        print(f"순회 결과: {result}")


# 테스트 프로그램
data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]
bst_map = BSTMap()

# 데이터 삽입
for key in data:
    bst_map.insert(key, None)

# 사용자 입력으로 순회 방식 선택 및 과정 출력
while True:
    print("\n## 순회 방식 선택 ##")
    print("1: 중위 순회 (Inorder)")
    print("2: 전위 순회 (Preorder)")
    print("3: 후위 순회 (Postorder)")
    print("0: 종료")
    try:
        order = int(input("순회 방식을 선택하세요 (0-3): "))
        if order == 0:
            print("프로그램을 종료합니다.")
            break
        if order not in [1, 2, 3]:
            print("잘못된 입력입니다. 1, 2, 3 중에서 선택해주세요.")
            continue
        bst_map.display_with_steps("트리 순회 과정", order=order)
    except ValueError:
        print("숫자를 입력해주세요.")
