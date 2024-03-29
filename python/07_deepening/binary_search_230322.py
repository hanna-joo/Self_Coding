# 백준 온라인 저지 2343, 시간 제한 2초
# 기타 레슨 동영상을 블루레이로 만들어 판매하려고 한다.
# 블루레이에는 총 N개의 레슨이 들어가는데 녹화할 때 레슨의 순서가 바뀌면 안 된다.
# M개의 블루레이에 모든 기타 레슨 동영상을 녹화하려고 하는데, 블루레이의 크기는 최소로 하고 모두 같은 크기로 만들려고 한다.
# 각 레슨의 길이가 분 단위로 주어질 때 가능한 블루레이 크기 중 최솟값을 구하는 프로그램을 작성하시오.
# N(1<=N<=100,000) M(1<=M<=N) 레슨길이(1<=레슨길이<=10,000)

# 필요 변수 선언 및 초기화
lesson_cnt, bluray_max = map(int, input().split())
lesson = list(map(int, input().split()))
start, end = max(lesson), sum(lesson)

# 이진 탐색
while start <= end:
    mid = (start+end)//2
    bluray_cnt = 0
    lesson_sum = 0
    for i in lesson:
        if lesson_sum + i > mid:
            bluray_cnt += 1
            lesson_sum = 0
        lesson_sum += i
    if lesson_sum != 0:
        bluray_cnt += 1
    if bluray_cnt > bluray_max:
        start = mid + 1
    else:
        end = mid - 1

# 정답 출력
print(start)