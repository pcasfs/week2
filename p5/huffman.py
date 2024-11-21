class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):                #연산 매서드 정의
        return self.freq < other.freq

    def __le__(self, other):
        return self.freq <= other.freq

    def __gt__(self, other):
        return self.freq > other.freq

    def __ge__(self, other):
        return self.freq >= other.freq

    def __eq__(self, other):
        return self.freq == other.freq


# Min Heap 삽입 알고리즘
def heappush_min(heap, n):
    heap.append(n)          # 맨 마지막 노드로 삽입
    i = len(heap) - 1       # 노드 n의 위치
    while i != 1:           # 루트가 아니면 up-heap 진행
        pi = i // 2         # 부모 노드의 위치
        if n >= heap[pi]:   # 부모보다 크거나 같으면 종료
            break
        heap[i] = heap[pi]  # 부모를 아래로 이동
        i = pi              # i가 부모 위치로 이동
    heap[i] = n             # 마지막 위치에 삽입

# Min Heap 삭제 알고리즘
def heappop_min(heap):
    size = len(heap) - 1
    if size == 0:
        return None

    root = heap[1]
    last = heap[size]
    pi = 1
    i = 2

    while i <= size:
        if i < size and heap[i].freq > heap[i+1].freq:
            i += 1  # 더 작은 자식 선택
        if last.freq <= heap[i].freq:
            break
        heap[pi] = heap[i]
        pi = i
        i *= 2

    heap[pi] = last
    heap.pop()
    return root

# Huffman Tree 생성
def build_huffman_tree_min_heap(char_freq):
    heap = [None]  # 1-based index를 위한 더미 노드
    for char, freq in char_freq.items():
        heappush_min(heap, Node(char, freq))

    while len(heap) > 2:  # 루트 노드가 하나 남을 때까지
        left = heappop_min(heap)
        right = heappop_min(heap)
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heappush_min(heap, merged)

    return heappop_min(heap)  # 최종 루트 반환

# Huffman 코드 생성
def generate_huffman_codes(node, current_code, codes):
    if node is None:
        return
    if node.char is not None:  # 리프 노드인 경우
        codes[node.char] = current_code
    generate_huffman_codes(node.left, current_code + "0", codes)
    generate_huffman_codes(node.right, current_code + "1", codes)

# 입력 문자열을 Huffman Encoding
def encode_string(input_str, codes):
    encoded_output = ""
    for char in input_str:
        if char not in codes:
            raise ValueError("illegal character")
        encoded_output += codes[char]
    return encoded_output

# 압축률 계산
def calculate_compression_rate(input_str, encoded_str):
    original_bits = len(input_str) * 8
    encoded_bits = len(encoded_str)
    compression_rate = ((original_bits - encoded_bits) / original_bits) * 100
    return compression_rate

# 메인 함수
def main():
    char_freq = {
        'k': 10, 'o': 5, 'r': 2, 'e': 15,
        'a': 18, 't': 4, 'c': 7, 'h': 11
    }

    print("Please a word: ", end="")
    while True:
        try:
            input_str = input().strip()
            if not input_str:
                print("Error: Input cannot be empty.")
                return
            if any(char not in char_freq for char in input_str):
                print("illegal character")
                print("Please a word: ", end="")
            else:
                break
        except Exception as e:
            print(f"Error: {e}")

    # Min-Heap 기반 Huffman Tree 구성
    root = build_huffman_tree_min_heap(char_freq)

    # Huffman 코드 생성
    codes = {}
    generate_huffman_codes(root, "", codes)
    print("Huffman Codes:", codes)  # Huffman 코드 출력

    # 입력 문자열 인코딩
    try:
        encoded_str = encode_string(input_str, codes)
    except ValueError as e:
        print(e)
        return

    # 압축률 계산
    compression_rate = calculate_compression_rate(input_str, encoded_str)

    # 결과 출력
    print(f"결과 비트 열: {encoded_str}")
    print(f"압축률: {compression_rate:.2f}%")

if __name__ == "__main__":
    main()
