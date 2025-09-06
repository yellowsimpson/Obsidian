# Python
While문이란?
	-> While문은 주어진 조건이  참인 동안 반복적으로 코드를 실행하는 반복문입니다.

While문 기본 구조
```python
while 조건:
    실행할 코드
```
예제
```python
x = 100
num = 1

while num < x:
    print("현재 값:", num)
    num *= 2
```

# C
While문 기본 구조
```python
while (조건 검사) {
    실행
}
```
예제
```python
#include <stdio.h>

int main() {
    int x = 100;
    int num = 1;

    while (num < x) {
        printf("현재 값: %d\n", num);
        num *= 2;  // 값을 2배 증가
    }

    return 0;
}
```
