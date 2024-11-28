# AVL 트리 균형 조정을 위한 회전 함수
from BinaryTree import calc_height  # calc_height 함수가 BinaryTree.py에 있다고 가정
from BinSrchTree import *  # 필요한 클래스나 함수 가져오기

def calc_height_diff(n):
    if n is None:
        return 0
    return calc_height(n.left) - calc_height(n.right)

def rotateLL(A):
    B = A.left
    A.left = B.right
    B.right = A
    return B

def rotateRR(A):
    B = A.right
    A.right = B.left
    B.left = A
    return B

def rotateLR(A):
    B = A.left
    A.left = rotateRR(B)
    return rotateLL(A)

def rotateRL(A):
    B = A.right
    A.right = rotateLL(B)
    return rotateRR(A)

def reBalance(parent):
    hDiff = calc_height_diff(parent)
    if hDiff > 1:
        if calc_height_diff(parent.left) > 0:
            parent = rotateLL(parent)
        else:
            parent = rotateLR(parent)
    elif hDiff < -1:
        if calc_height_diff(parent.right) < 0:
            parent = rotateRR(parent)
        else:
            parent = rotateRL(parent)
    return parent

# AVL 트리 삽입
def insert_avl(parent, node):
    if node.key < parent.key:
        if parent.left is not None:
            parent.left = insert_avl(parent.left, node)
        else:
            parent.left = node
        return reBalance(parent)
    elif node.key > parent.key:
        if parent.right is not None:
            parent.right = insert_avl(parent.right, node)
        else:
            parent.right = node
        return reBalance(parent)
    else:
        print("중복된 키 에러")

# AVL 트리 삭제
def delete_avl(parent, key):
    if parent is None:
        return None

    # 삭제하려는 키를 찾음
    if key < parent.key:
        parent.left = delete_avl(parent.left, key)
    elif key > parent.key:
        parent.right = delete_avl(parent.right, key)
    else:
        # 리프 노드일 경우 삭제
        if parent.left is None and parent.right is None:
            return None
        # 자식이 하나만 있는 경우
        elif parent.left is None:
            return parent.right
        elif parent.right is None:
            return parent.left
        # 자식이 둘 다 있는 경우: 후속자(오른쪽 서브트리에서 최소값)를 찾음
        else:
            successor = find_min(parent.right)
            parent.key = successor.key
            parent.right = delete_avl(parent.right, successor.key)

    # 삭제 후 균형 복구
    return reBalance(parent)
