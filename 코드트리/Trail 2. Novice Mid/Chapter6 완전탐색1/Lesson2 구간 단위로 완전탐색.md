**모이자**
- 한 자리를 정하여 완전탐색

다음은 어떻게 문제를 풀 수 있을까?
```
5개의 숫자 [1, 5, 2, 6, 8]이 주어졌을 때
이 중 단 하나의 숫자만 두 배로 해서, 인접한 숫자간의 차이의 합이 최대가 되도록 해보세요.
```
이 문제를 단순하게, 모든 위치의 숫자를 2배씩 해보는 완전탐색을 진행해 볼 수 있다.
```
1. 첫 번째 숫자 1에 2배를 하는 경우
[2, 5, 2, 6, 8]이 되므로, 인접한 숫자간의 차이의 합은 3 + 3 + 4 + 2 = 12가 됩니다.

2. 두 번째 숫자 5에 2배를 하는 경우
[1, 10, 2, 6, 8]이 남게 되므로, 인접한 숫자간의 차이의 합은 9 + 8 + 4 + 2 = 23이 됩니다.

3. 세 번째 숫자 2에 2배를 하는 경우
[1, 5, 4, 6, 8]이 남게 되므로, 인접한 숫자간의 차이의 합은 4 + 1 + 2 + 2 = 9가 됩니다.

4. 네 번째 숫자 6에 2배를 하는 경우
[1, 5, 2, 12, 8]이 남게 되므로, 인접한 숫자간의 차이의 합은 4 + 3 + 10 + 4 = 21이 됩니다.

5. 다섯 번째 숫자 8에 2배를 하는 경우
[1, 5, 2, 6, 16]이 남게 되므로, 인접한 숫자간의 차이의 합은 4 + 3 + 4 + 10 = 21이 됩니다.

따라서 최대는 23이 됩니다.
```

코드는 다음과 같이 작성해 볼 수 있다.
```python
n = 5
arr = [1, 5, 2, 6, 8]

max_sum = 0
for i in range(n):
    arr[i] *= 2

    sum_diff = 0
    for j in range(n - 1):
        sum_diff += abs(arr[j + 1] - arr[j])

    max_sum = max(max_sum, sum_diff)
    arr[i] //= 2

print(max_sum)

>> 23
```
이처럼 각 자리에 대해 상황을 일일이 가정해보고 진행해보는 완전탐색 방법을 이용하면, 문제를 깔끔하게 해결할 수 있다.

Side note
다음 코드의 결과는 어떻게 될까?
```python
n = 5
arr = [-6, -5, -2, -10, -15]

max_val = 0
for i in range(n):
    if arr[i] > max_val:
        max_val = arr[i]

print(max_val)
```
결과는 0이 나옵니다. 그 이유는 원소가 전부 0보다 작기 때문에, if 조건을 만족하는 경우가 생기지 않는다.


```python
import sys

INT_MAX = sys.maxsize
INT_MIN = -sys.maxsize

n = 5
arr = [-6, -5, -2, -10, -15]

max_val = INT_MIN
for i in range(n):
    if arr[i] > max_val:
        max_val = arr[i]

min_val = INT_MAX
for i in range(n):
    if min_val > arr[i]:
        min_val = arr[i]

print(max_val, min_val)

>> -2 -15
```