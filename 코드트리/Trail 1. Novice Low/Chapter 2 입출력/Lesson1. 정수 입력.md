
**입력**
python3에서는 input()이라는 함수를 통해 항상 한줄 단위로 입력 받을 수 있다.
```python
a = input()

print(f"A is {a}")
```
입력받은걸 바로 int로 적을려면 아래 와 같이 적으면 된다.
```python
a = int(input())
print(a + 1)
```

**실수 입력**
문자열을 실수형으로 type을 바꾸기 위해서는 float라는 함수로 감싸주면 된다
```python
a = input()
a = float(a)

print(a + 0.58)
```
출력 결과
```python
>> 3.79

4.37
```

