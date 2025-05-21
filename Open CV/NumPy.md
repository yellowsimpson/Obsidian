
NumPy의 기본 속성
1. ndim: 차원(축)의 수
2. shape: 각 차원의 크기(튜플)
3. size: 전체 요소의 개수, shape의 각 항목의 곱
4. dtype: 요소의 데이터 타입
5. itemsize: 각 요소의 바이트 크기

ndarray ->N-Dimensional Array의 약자
이미지를 3차원 배열 '행 X 열 X 채널'

```
numpy.array(list [, dtype]): 지정한 값들로 NumPy 배열 생성
list: 배열 생성에 사용할 값을 갖는 파이썬 리스트 객체
dtype: 데이터 타입
-> int8, int16, int32, int64: 부호 있는 정수
-> uint8, uint16, uint32, uint64: 부호 없는 정수
-> float16, float32, float64, float128: 부동 소수점을 갖는 실수
-> complex64, complex128, complex256: 부동 소수점을 갖는 복소수
-> bool: 볼
```


```
import numpy as np

a = np.array([1,2,3,4])
print(a)
print(a.dtype)
print(a.shape)

#[1 2 3 4]
#int64
#(4,)

b = np.array([[1,2,3,4], [5,6,7,8]])
print(b)
print(b.dtype)
print(b.shape)

#[[1 2 3 4]
#[5 6 7 8]]
#int64
#(2, 4)

c = np.array([1, 2, 3.14, 4])
print(c)
print(c.dtype)
print(c.shape)

#[1.   2.   3.14 4.  ]
#float64
#(4,)

#만역 uint8의 데이터 타입으로 출력하고 싶으면 아래와 같이 적으면됨
a = np.uint([1,2,3,4])
print(a.dtype)

#uint8
```

*초기값 지정하는 방법*
```
numpy.empty(shape [, dtype]): 초기화 되지 않은 값
numpy.zeros(shape [, dtype]): 0으로 초기화 된 배열
numpy.ones(shape [, dtype]): 1로 초기화된 배열 생성
numpy.full(shape, fill_value [, dtype]): fill_value로 초기화된 배열 생성
```

ndarray.fill(value): 배열의 모든 요소를 value로 채움
```
a = np.array([[1,2,3,4], [5, 6, 7, 8]])
a.fill(255)
print(a)

#[[255 255 255 255]
 [255 255 255 255]]
```