# DAY 1 & 2

- 날짜 : 2022.10.13



### 1. 두 수의 합

```python
def solution(num1, num2):
    return num1 + num2
```

### 2. 두 수의 차

```python
def solution(num1, num2):
    return num1 - num2
```

### 3. 두 수의 곱

```python
def solution(num1, num2):
    return num1 - num2
```

### 4. 몫 구하기

```python
def solution(num1, num2):
    return num1 // num2
```

### 5. 두 수의 나눗셈

```python
def solution(num1, num2):
    return int((num1 / num2) * 1000)
```

### 6. 숫자 비교

```python
def solution(num1, num2):
    return int((num1 / num2) * 1000)
```

### 7. 분수의 덧셈

- 첫 번째
  - 1부터 올라가면서 제거하는 방법

```python
def solution(denum1, num1, denum2, num2):
    num3 = num1 * num2
    denum3 = denum1 * num2 + denum2 * num1
    while denum3 % 2 == 0 and num3 % 2 == 0:
        denum3 /= 2
        num3 /= 2
    for i in range(3, 1000, 2):
        while denum3 % i == 0 and num3 % i == 0:
            denum3 /= i
            num3 /= i
    return [denum3, num3]
```

- 두 번째
  - 최대 공약수로 나누면 더 나눌 필요가 없기 때문에 최대 공약수를 찾아서 나누는 방법

```python
def solution(denum1, num1, denum2, num2):
    num = num1 * num2
    denum = (denum1 * num2 + denum2 * num1)
    for i in range(min(denum, num), 0, -1):
        if denum % i == 0 and num % i == 0:
            denum /= i
            num /= i
            break
    return [denum, num]
```

### 8. 배열 두 배

```python
def solution(numbers):
    return [2*x for x in numbers]
```

```python
def solution(numbers):
    return list(map(lambda x : 2*x, numbers))
```

