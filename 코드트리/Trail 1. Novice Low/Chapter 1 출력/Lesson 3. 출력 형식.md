**출력 형식**
변수에 담긴 값을 원하는 형식에 맞춰 출력하기 위해서는 크게 3가지 방법이 있다.

1. 변수 포맷(%d, %s, ...)과 %를 사용
다음과 같이 문자열에 해당 변수의 type에 해당하는 표맷을 적어주고, 맨 뒤에는 %뒤에는 변수를 적어준다.

```python
a = 5
print("A is %d" % a)

b = "apple"
print("B is %s" % b)

print("A is %d and B is %s" % (a, b))
```

2. format 함수 사용
format 함수를 이용하면 직접 변수의 type을 명시하지 않더라도, 순서 혹은 이름을 명시하여 원하는 변수를 포맷에 맞춰 넣어줄 수 있다. 숫자를 적게되는 경우 format 함수에 적게되는 변수에 번호를 0번부터 붙였을 때 몇 번째 값이지를 명시하는 것이다. 숫자 대신 새로운 이름을 붙여 적는 것도 가능.
```python
a, b = 5, "apple"

print("A is {0}".format(a))
print("A is {new_a}".format(new_a=a))

print("B is {0}".format(b))
print("B is {new_b}".format(new_b=b))

print("A is {0} and B is {1}".format(a, b))
print("A is {new_a} and B is {new_b}".format(new_a=a, new_b=b))
print("B is {1} and A is {0}".format(a, b))
print("B is {new_b} and A is {new_a}".format(new_a=a, new_b=b))
```
출력 결과
```python
A is 5
A is 5
B is apple
B is apple
A is 5 and B is apple
A is 5 and B is apple
B is apple and A is 5
B is apple and A is 5
```
3. f 문자열 포맷을 이용
f 문자열을 이용할 수 있다.

```python
a, b = 5, "apple"

print(f"A is {a}")
print(f"B is {b}")
print(f"A is {a} and B is {b}")
```
출력 결과
```python
A is 5
B is apple
A is 5 and B is apple
```
