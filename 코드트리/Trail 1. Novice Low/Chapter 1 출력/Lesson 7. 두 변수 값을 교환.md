**두 변수 값을 교환**
변수 a에 담겨있는 값과 변수 b에 있는 값을 서로 교환할 수는 없을까?
크게 2가지 방법이 있다.

*방법1. temp 이용*
언어와 무관하게 temp라는 추가 변수를 사용하여 두 변수 값을 교환 할 수 있다.
```python
a, b = 5, 3

temp = a
a = b
b = temp

print(f"A is {a} B is {b}")
```
출력 결과
```python
A is 3 B is 5
```
*방법2. , 를 이용하여 바로 교환하기*
python에서는 다음과 같이 ,를 이용하여 원하는 두 변수 값을 교환하는 것이 가능하다.
```python
a, b = 5, 3

a, b = b, a

print(f"A is {a} B is {b}")
```
출력 결과
```python
A is 3 B is 5
```
