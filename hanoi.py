import time
count = 0
def hanoi_tower(n,fr, tmp, to):
    global count #전역 변수로 선언
    if(n == 1):
        print("원판 1: %s --> %s" % (fr, to))
        count += 1
    
    else:
        hanoi_tower(n-1, fr, to, tmp)
        print("원판 %d: %s --> %s" % (n, fr, to))
        count += 1
        hanoi_tower(n-1, tmp, fr, to)
        
input = input("n을 입력하시오:")
n = int(input)

start_time = time.time()
hanoi_tower(n, 'A', 'B', 'C')
end_time = time.time()

print("함수 호출 횟수: ", count)
print("실행 시간:", end_time - start_time, "초")