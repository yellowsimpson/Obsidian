**공백을 사이에 두고 입력**
python에서 입력은 한 줄 단위로만 받을 수 있습니다.
만약 2개의 숫자를 한줄에 공백을 사이에 두고 받고 싶다면 코드를 어떻게 작성해야 될까요?
python에는 split()이라는 함수가 있습니다. 이 함수는 문자열을 특정 기준으로 잘라주는 함수입니다.
예를 들어 다음과 같이 split 함수를 그대로 사용하면, 공백을 기준으로 묹아ㅕㄹ을 잘라 각 잘려나간 단위가 하나의 원소가 되어 해당 원소들을 가지고 있는 하나의 list가 만들어집니다.


```python
a = input()
print(a.split())
```
출력 결과
```python
>> 13 17

['13', '17']
```

list라는 것은 여러 원소를 들고있는 묶음으로, list 안에 있는 각 원소를 참조하기 위해서는 원소의 번째 수 -1값을 대괄호 [] 와 같이 사용하여 가져올 수 있습니다.

예를 들어 다음 코드에서처럼 원소를 3개 들고 있는 arr라는 list에서 첫 번째 원소를 참조하기 위해서는 arr[0]으로, 2번째 원소는 arr[1], 3번째 원소는 arr[2]로 참조가 가능합니다.
```python
arr = [5, 6, 10]
print(f"First element is {arr[0]}")
print(f"Second element is {arr[1]}")
print(f"Third element is {arr[2]}")
```

출력 결과
```python
First element is 5
Second element is 6
Third element is 10
```
따라서 공백을 사이에 두고 두 정수를 입력받아 각각의 정수를 변수 n, m에 순서대로 넣어주고 싶다면 다음과 같은 코드를 작성해볼 수 있습니다. 그리고 두 정수의 곱을 최종적으로 구해주는 코드 작성 역시 가능해 보입니다. 하지만 최종적으로 n * m값을 구하려 할 때 다음의 에러를 목격하게 됩니다.

```python
a = input()
arr = a.split()
n = arr[0]
m = arr[1]

print(n)
print(m)
print(n * m)
```
출력 결과
```python
>> 13 17

13
17
---> print(n * m)

TypeError: can't multiply sequence by non-int of type 'str'
```
문자열 끼리는 곱하기 연산을 수행할 수 없다는 에러입니다. 이는 n,m 변수의 type이 정수가 아닌 문자열이라는 의미이므로, split을 진행한 이후 n, m에 리스트에 있는 원소를 담아 줄 때 int형으로 형변환을 해주는 것으로 해결이 가능합니다.
```python
a = input()
arr = a.split()
n = int(arr[0])
m = int(arr[1])

print(n)
print(m)
print(n * m)
```

출력 결과
```python
>> 13 17

13
17
221
```

*side note*
위의 코드에서 input()과 split() 코드를 다음과 같이 한줄로 이어 작성하는 것도 가능합니다.

```python
arr = input().split()
n = int(arr[0])
m = int(arr[1])

print(n)
print(m)
print(n * m)
```

