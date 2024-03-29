# 데이터 자료구조
## 1. 구간 합 : O(1)
## 2. 투 포인터 : O(nlogn)
## 3. 슬라이딩 윈도우 : O(n)
- 윈도우를 한 칸씩 이동하며 현재 상태 리스트 업데이트
  - 제거된 칸과 새로 추가된 칸만 반영해서 확인하고 업데이트
  - 윈도우 전체를 스캔할 필요 없이 앞 뒤만 확인하면 되기 때문에 효율적
- 슬라이딩 윈도우를 덱으로 구현하면 정렬 효과
  - 덱(deque) : 양방향 큐로 양쪽 방향에서 엘리먼트를 append 하거나 pop 가능
  - 일반적인 리스트는 양끝 엘리먼트에 접근하여 append, pop하는 경우 O(n) 소요
  - 데크의 경우 양끝 엘리먼트에 접근하여 append, pop하는 경우 O(1) 소요
  - `deque.append(item)`, `deque.appendleft(item)`, `deque.pop()`, `deque.popleft()`
## 4. 스택과 큐
- 스택(stack) : 삽입과 삭제 연산이 후입선출로 이루어지는 자료구조
  - 삽입과 삭제가 한 쪽(top)에서만 일어남
  - 파이썬에서는 list로 구현
  - `s.append(data)`, `s.pop()`, `s[-1]`
  - 깊이 우선 탐색(Depth First Search), 백트래킹 종류의 코딩에 효과적
- 큐(queue) : 삽입과 삭제 연산이 선입선출로 이루어지는 자료구조
  - 삽입(rear)과 삭제(front)가 양방향으로 일어남
  - 파이썬에서는 deque로 구현
  - `q.append(data)`, `q.popleft()`, `q[0]`
  - 너비 우선 탐색(Breadth First Search)에서 자주 사용
- 우선순위 큐(priority queue) : 값이 들어간 순서와 상관없이 우선순위가 높은 데이터가 먼저 나오는 자료구조, 
  - 일반적으로 heap 으로 구현
    - collections.queue.PriorityQueue 내부적으로 heap 모듈 사용
  - 기본적으로 정렬 기준은 오름차순 정렬
    - 정렬 기준 직접 정의해서 적용 가능 (오름차순 정렬보다 우선 적용)
  - `q.put((우선순위, data))`, `q.get()`, `q.empty()`, `q.full()` `q.qsize()`
## 5. 해시
- 해시(hash) : O(1) ~ O(N)
  - 데이터 다루는 기법 중 하나로, 임의의 값(key)을 고정 길이(value)로 변환하는 것
- 해시 함수(hash function)
  - 임의의 길이의 데이터를 고정된 길이의 데이터로 매핑하는 함수
  - 매핑 전의 원래 데이터 값은 key, 매핑 후의 데이터 값은 hash(=hash value=hash code)
- 해시 테이블(hash table)
  - 연관배열 구조를 이용하여 key에 value을 저장하는 자료구조
  - key와 value의 쌍으로 데이터를 저장하는 자료구조 (Python - Dictionary)
  - 특징
    - 저장 : 순차 저장되지 않음, key 중복 불가, value 중복 가능
    - 조회 : key를 통해 value를 얻음
    - 수정 : 수정 가능한 자료구조
    - 충돌 : 모든 경우에 충돌 발생 시 O(N), 충돌 발생하지 않을 시 O(1)
  - 장점
    - 저장, 검색 속도가 빠름
    - key에 대한 value가 있는지 중복 확인 쉬움
  - 단점
    - 저장 공간이 상대적으로 많이 필요
    - 여러 key에 해당하는 주소가 동일한 경우 충돌을 해결하기 위한 별도의 자료구조 필요 (충돌 해결 알고리즘)
  - 구조
    - key : 고유한 값, 해시 함수의 input
    - hash function : hash로 변경하여 저장소를 효율적으로 운영 가능, 해시 충돌 확률 줄이는 함수 만드는 것이 중요
    - hash : 해시 함수의 결과물로 저장소(bucket, slot)에서 value와 매칭되어 저장
    - value : 저장소에 최종적으로 저장되는 값으로 key와 매칭되어 저장, 삭제, 검색, 접근 가능