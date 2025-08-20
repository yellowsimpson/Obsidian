**다른 변수로부터 변수 값 변경**
변수 a의 값에 다른 변수 b에 있는 값을 가져와 넣어주는 것 역시 가능합니다. 최종 결과가 2가 아닌 3임에 유의하자

```python
a, b = 5, 3
print("A is", a)

a = b
print("A is", a)

a = 2
print("B is", b)
```
출력 결과
```python
A is 5
A is 3
B is 3
```