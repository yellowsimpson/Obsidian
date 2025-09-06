# Python
range()함수란?
	-> range()함수는 지정된 범위의 수를 생성하는 함수입니다.

for 문과 range()함수의 결합

```python
for i in range(5):
    print(i)
```

range 뜻

- range(값 1개일 때)
```
range(stop)
	  #끝값
```
- range(값 2개일 때)
```
range(start, stop)
	  #시작값, 끝값
```
- range(값 3개일 때)
```
range(start, stop, step)
	  #시작값, 끝값,  증가값
```

# C
for문 기본 예제
```c
#include <stdio.h>

int main() {
    int i;
    for (i = 0; i < 5; i++) {
        printf("%d\n", i);
    }
    return 0;
}
```

for (i = 0; i < 5; i++)
- 초기화: i = 0으로 반복 변수를 0으로 설정한다.
- 조건: i <5 조건이 참인 동안 반복한다.
- 증감: i++를 통해 매 반복마다 i의 값을 1씩 증가한다.


for 문 정리
- for(i = 0; i < stop; i++)
- for(i = start; i < stop; i++)
- for(i = start; i < stop; i += stop) 
# C++
for문 기본 구조
```c++
for (초기화; 조건; 증감) {
    // 실행할 코드
}
```
예시
```c++
int i;

for(i = 0; i < 10; i++){
    cout << i << "\n";
}
```