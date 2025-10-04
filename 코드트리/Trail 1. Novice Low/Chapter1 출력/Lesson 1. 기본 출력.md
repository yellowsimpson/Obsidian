
**출력**
python에서는 출력의 경우 print라는 함수를 사용할 수 있다.
다음과 같이 print 함수 안에 문자열을 넣게 되면, 해당 문자열이 화면에 출력된다.
```python
print("Hello")
```
python에서 문자열은 크게 4가지 방법으로 표현할 수 있다.
1. 큰 따옴표 " 사용
```python
"Hello World"
```
2. 작은 따옴표 ' 사용
```python
'Hello World'
```
3. 큰 따옴표 3개를 연속으로 """ 사용
```python
"""Hello World"""
```
4. 작은 따옴표 3개 연속으로 ''' 사용
```python
'''Hello World'''
```
**문장 출력**
python에서 문장을 출력 할때는 다음과 같이 문자열을 그대로 출력 해도 됨
```python
print("Hello World!")
```
**문자열에 특수 문자 포함시키기**
python에서 문장열은 ", ', """, '''로 표현할 수 있다. 이때 만약 다음처럼 '와 같은 문자를 포함하는 문장을 출력하기 위해서는 어떻게 해야될까?

```python
print('Let's do it')
```

*방법1*
이런 경우 " "로 문장을 감싸준다.

```python
print("Let's do it")
```
*방법2*
print문 가운데 '를 넣을려면 \를 붙여 줘야한다.

```python
print('Let\'s do it')
```
*방법3*
'''를 붙여 다.
```python
print('''Let's do it''')
```

**2줄 출력**
*방법1*
걍 2줄 쓴다
```python
print("Hello World")
print("Python is Fun")
```
*방법2*
\n를 붙여준다
```python
print("Hello World\nPython is Fun")
```
*방법3*
'''를 사용
```python
print('''Hello World
	Python is Fun''')
```
**숫자 출력**
print 안에 문자열이 아닌 숫자를 넣어줘도 해당 숫자 그대로 출력하게 하는 법
```python
print(3) #숫자
```
```python
print("3") #문자열
```

**공백을 사이에 두고 출력**
숫자 사이에 , 넣어주면 됨
```python
print(3, 5)

print(3, 5) -> 3 5
print(3, 5, sep=":") -> 3:5
print(3, 5, sep=" ") -> 3 5
```

```python
print(3)
print(5)


>>>3
   5
```
이 경우 처럼 print 함수를 2번 사용하는데 공백을 사이에 두고 출력하는 방법
```python
print(3, end = " ")
print(5)

>>> 3 5
```

