
# Python
## 문자열이란?
- 문자열은 문자의 모음으로 이루어진 자료형입니다.
- 작은 따옴표(' ')나 큰 따옴표(" ")로 감싸서 표현할 수 있습니다.
- 문자열은 한 번 생성하면 그 안의 글자를 직접 변경할 수 없는 __불변성(immutable)__ 자료형입니다.
- 파이썬은 다양한 문자열 메서드와 연산자를 제공하여 문자열을 쉽게 다룰 수 있습니다.

#### 기본 구조
- 문자열은 작은 따옴표' 나 큰 따옴표 "로 감쌀 수 있습니다. 여러 줄로 이루어진 문자열은 삼중 따옴표 """ 나 ""를 사용합니다.
```python
greeting = "Hello, World!"       # 큰 따옴표로 감싼 문자열
single_quote = 'Python은 재미있어요.'  # 작은 따옴표로 감싼 문자열
multiline = """이것은
여러 줄로
작성된 문자열입니다."""  # 삼중 따옴표를 이용한 여러 줄 문자열
empty_str = ""  # 빈 문자열
```

## 문자열의 선언과 초기화
- 문자열은 직접 값을 나열하여 생성할 수 있습니다.
```python
message = "안녕하세요!"  # 문자열 직접 할당
```

- str( ) 함수를 사용하여 다른 데이터 타입을 문자열로 변환할 수 있습니다.

```python
number = 123
text = str(number)
print(text)  # 출력: "123"
```

- 빈 문자열도 생성할 수 있습니다.

```python
empty = ""  # 빈 문자열

```

## 문자열 인덱싱
### 인덱싱: 특정 문자 접근
- 문자열에서 특정 문자는 인덱스를 사용하여 접근할 수 있습니다. 인덱스는 0부터 시작합니다.
```python
text = "Python"
print(text[0])  # 출력: P
print(text[3])  # 출력: h
```
- 파이썬은 음수 인덱스도 지원하며, -1부터 시작하여 뒤에서부터 접근합니다.
```python
text = "Python"
print(text[-1]) # 출력: n
print(text[-4]) # 출력: t
```
- 인덱스가 문자열 범위를 초과하면 IndexError가 발생합니다.
```python
print(text[6])  # 오류 발생
```

### 값 수정: 문자열의 변경
- 문자열은 불변(immutalbe) 자료형이므로 직접 수정할 수 없습니다.
- 문자열을 변경하려면 새로운 문자열을 생성해야 합니다.
```python
text = "Python"
# 특정 문자를 변경하려고 시도 (오류 발생)
text[0] = "J"  # 오류 발생
```

### 문자열 덧셈(문자열 연결)
- 문자열 덧셈은 + 연산자를 사용하여 두 개 이상의 문자열을 연결합니다.
```python
str1 = "Hello, "
str2 = "World!"
print(str1 + str2)  # 출력: Hello, World!
```
- 여러 문자열을 연결 할 때도 + 연산자를 연달아 사용할 수 없습니다.
- 단, 문자열과 숫자 등 다른 데이터 타입은 바로 연결 할 수 없으므로, 필요시 형변환이 필요합니다.

### 문자열 곱셈(문자열 반복)
- 문자열 곱셈은 * 연산자를 사용하여 특정 문자열을 지정된 횟수만큼 반복합니다. 
```python
str1 = "Hi "
print(str1 * 4)  # 출력: Hi Hi Hi Hi 
```
- 반복 횟수는 정수값으로 지정하며, 음수 값을 사용할 수 없습니다.
- 문자열 곱셈은 문자열의 패턴을 간편하게 나타낼 수 있어, 반복되는 문자열 생성에 유용합니다.
### 문자열의 슬라이싱
-> 슬라이싱(Slicing)은 파이썬에서 문자열의 특정 부분만을 쉽게 추출하는 방법입니다. 예를 들어, 긴 문자열에서 원하는 부분만 따로 사용하거나 확인할 때 유용하게 쓰입니다.

#### 슬라이싱의 기본 문법
```python
문자열[start:end]
```
- start: 슬라이싱은 시작할 위치의 인덱스입니다. 이 인덱스는 포함됩니다.
- end: 슬라이싱을 끝낼 위치의 인덱스입니다. 이 인덱스는 포함되지 않습니다. 즉, end 바로 전에 있는 요소까지만 추출됩니다.
예시:
```python
text = "Python is fun"
print(text[1:4])  # 출력: yth
```

#### start 혹은 end 생략하기
-> 슬라이싱에서는 start 나 end를 생략할 수 있습니다.
- start 생략: 문자열의 첫 번째 요소(인덱스 0)부터 시작합니다.
- end 생략: 문자열의 마지막 요소까지를 의미합니다.
- 둘 모두 생략할 경우 문자열의 처음부터 끝까지 전체를 의미합니다.
```python
text = "Python is fun"
print(text[:5])  # 출력: Pytho
print(text[2:])  # 출력: thon is fun
print(text[:])   # 출력: Python is fun
```
또한, 음수 인덱스를 사용하여 문자열의 끝에서부터 슬라이싱 범위를 지정할 수도 있습니다.
```python
text = "Python is fun"
print(text[-5:])  # 출력: s fun
```

#### 간격(step) 지정하기
-> 슬라이싱 문법에서는 start, end 외에도 step(간격)을 지정할 수 있습니다. 기본적으로 step의 값은 1이지만, 2이상을 주면 해당 간격만큼 건너뛰며 추출합니다.
```python
text = "Python is fun"
print(text[::2])  # 출력: Pto sfn
```
또한 step에 음수 값을 주면 리스트를 거꾸로 뒤집에서 추출할 수 있습니다.
```python
text = "Python is fun"
print(text[::-1])  # 출력: nuf si nohtyP
```
## 문자열 주요 메서드
### upper(), lower(): 대소문자 변환
- upper(): 문자열의 모든 문자를 대문자로 변환합니다.
- lower(): 문자열의 모든 문자를 소문자로 변환합니다.
  
```python
text = "Python Programming"
print(text.upper())  # 출력: "PYTHON PROGRAMMING"
print(text.lower())  # 출력: "python programming"
```
### strip(), lstrip(), rstrip() : 공백문자 제거
- strip(): 문자열 양쪽에 있는 공백문자를 제거합니다. 제거되는 문자로는 공백문자()뿐만 아니라 줄바꿈 문자\n, 탭 문자 \t 도 제거됩니다.
```python
text = "   Hello, World!   "
print(text.strip())  # 출력: "Hello, World!"
```
- lstrip(): 문자열 왼쪽에서 공백과 지정한 문자를 제거합니다.
```python
text = "   Hello, World!   "
print(text.lstrip())  # 출력: "Hello, World!   "
```
- rstrip(): 문자열 오른쪽에서 공백과 지정한 문자를 제거합니다.
```python
text = "   Hello, World!   "
print(text.rstrip())  # 출력: "   Hello, World!"
```
참고: strip()은 양쪽 공백을 모두 제거하지만, 경우에 따라 왼쪽 또는 오른쪽 공백만 제거하는 것이 더 유용할 수 있습니다. 이럴 때 lstrip() 또는 rstrip()을 사용하는 것이 좋습니다.

```

## 문자열 처리 함수
-> C 언어에서는 string.h 헤더 파일에 문자열을 다루는 다양한 함수가 제공됩니다.
### 문자열 길이 계산(strlen)
- strlen(문자열)은 문자열의 길이를 변환합니다.
- \0 (널 문자)는 길이에 포함되지 않습니다.


```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "C Programming";

    printf("문자열 길이: %lu\n", strlen(str));
    return 0;
}
```
출력
```c
문자열 길이: 13
```

### 문자열 복사(strcpy)
- strcpy(대상문자열, 원본문자열);
	-> 원본 문자열을 대상 문자열로 복사합니다.

출력 예시
```
복사된 문자열: Hello

```

### 문자열 연결(strcat)
- strcat(대상문자열, 추가할 문자열);
	-> 대상문자열 원본에 추가할문자열을 이어붙입니다.

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[20] = "Hello, ";
    char str2[] = "World!";

    strcat(str1, str2);
    printf("연결된 문자열: %s\n", str1);
    return 0;
}
```
출력
```c
연결된 문자열: Hello, World!
```

### 문자열 비교(strcmp)
- strcmp(str1, str2)
	-> 문자열을 사전순으로 비교한 결과값을 반환합니다.
- str1 이 크면 양수
- str1 과 str2가 동일하면 0
- str1이 작으면 음수
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "Apple";
    char str2[] = "Banana";

    int result = strcmp(str1, str2);

    if (result == 0) 
        printf("두 문자열이 같습니다.\n");
    else if (result < 0) 
        printf("%s이(가) %s보다 사전순으로 앞에 위치합니다.\n", str1, str2);
    else 
        printf("%s이(가) %s보다 사전순으로 뒤에 위치합니다.\n", str1, str2);
    
    return 0;
}
```
출력
```c
Apple이(가) Banana보다 사전순으로 앞에 위치합니다.
```

### 부분 문자열 추출(strncpy)
- strncpy(대상문자열, 원본 문자열, 길이);
	-> 원본문자열에서 특정 길이만큼을 앞에서부터 대상문자열에 복사합니다.
	
```c
#include <stdio.h>
#include <string.h>

int main() {
    char src[] = "Hello, World!";
    char dest[6];

    strncpy(dest, src, 5);
    // dest: {'H', 'e', 'l', 'l', 'o'}
    dest[5] = '\0';  // 수동으로 NULL 문자 추가
    // dest: {'H', 'e', 'l', 'l', 'o', '\0'}
    printf("부분 문자열: %s\n", dest);
    
    return 0;
}
```


출력
```c
부분 문자열: Hello
```

## 문자열 배열이란?
- 여러 개의 문자열을 하나의 배열로 관리하고 싶을 때 사용합니다.
- C에서 2차원 char 배열 형태로 선언하며, 이는 1차원 배열의 확장으로 생각할 수 있으며 대괄호 [ ]를 두번 사용하여 선언합니다.

### 선언과 초기화
```c
char names[3][20] = { //3 -> 문자열 갯수, 20 -> 각 문자열의 최대 19글자 + 끝을 표시하는 \0까지 저장 가능한 크기
    "Alice",
    "Bob",
    "Charlie"
};
```
출력 결과
```c
names[0] = Alice
names[1] = Bob
names[2] = Charlie
```

### 사용자 입력 예제
```c
#include <stdio.h>

int main() {
    char fruits[3][20];

    for(int i = 0; i < 3; i++){
        scanf("%s", fruits[i]);
    }

    printf("입력된 과일 목록:\n");
    for(int i = 0; i < 3; i++){
        printf("%s\n", fruits[i]);
    }
    return 0;
}
```
- scanf("%s", fruits[i]);  는 문자열을 입력받아 fruits[i]에 저장합니다. (\0 문자 포함)
- 문자열 입력 시 공백 문자(띄어쓰기, 탭, 줄바꿈 등)를 만나면 입력이 종료되므로, 단어 단위로만 입력됩니다.

입력:
```c
Apple Banana Cherry
```
출력 결과:
```c
입력된 과일 목록:
Apple
Banana
Cherry
```

## 정리
- C에서는 char 배열을 사용하여 문자열을 저장합니다.
- scanf()와 fegets()를 사용하여 문자열을 입력받을 수 있습니다.
- string.h 라이브러리를 활용하여 문자열을 복사(strcpy), 연결(strcat), 비교(strcmp)할 수 있습니다.
- 문자열을 안전하게 다루기 위해 배열 크기와 NULL 문자(\0)를 고려해야 합니다.



# C
## 문자열이란?
- C언어에서 문자열은 문자형 배열(char 배열)을 사용하여 표현됩니다.
- 이때 문자열 마지막( \0 )을 넣어줌으로써 문자열 끝을 잘 표기해 줘야합니다.

## 문자열의 선언과 초기화
- char형 배열을 선언하는 것은 이전에 배운 배열의 선언과 동일합니다.
- 이때 초기화는 일반적인 배열의 초기화 방법을 따를 수도 있으며 (이 경우 \0을 명시적으로 포함해야함에 유의해야합니다.)
- 큰따옴표(" ")로 감싸 표현할 수도 있습니다.

```C
#include <stdio.h>

int main() {
    // 명시적으로 '\0' 포함해야합니다.
    char str1[3] = {'H', 'i', '\0'};

    // 배열크기를 명시하지 않아도 자동으로 계산되어 배열크기가 5가 됩니다.
    char str2[] = {'I', ' ', 'a', 'm' '\0'};

    // 큰따옴표를 이용하면 `\0`를 명시적으로 표현하지않아도 자동으로 포함됩니다.
    char str3[10] = "Hello";
    // str3[0] = 'H'
    // str3[1] = 'e'
    // str3[2] = 'l'
    // str3[3] = 'l'
    // str3[4] = 'o'
    // str3[5] = '\0'

    // 이러한 경우도 str2와 마찬가지로 자동으로 배열크기가 6이 됩니다. (널 문자 포함)
    char str4[] = "World";

    // 문자열은 입출력시 형식 지정자 %s를 사용합니다.
    printf("%s %s %s %s\n", str1, str2, str3, str4);
    return 0;
}
```

출력
```c
Hi I am Hello World
```

## 문자열 입력 및 출력
### scanf()를 사용한 문자열 입력
- scanf("%s", 변수명); 을 사용하면 공백 문자(띄어쓰기, 탭, 줄바꿈 등)을 포함하지 않는 단어 하나를 입력받을 수 있습니다.
- 다른 변수를 입력받는것과 다르게 & 표기를 포함하지 않아도 됩니다.
```c
#include <stdio.h>

int main() {
    char name[50];
    
    printf("이름을 입력하세요: ");
    scanf("%s", name);  // & 없어도 됨

    printf("입력된 이름: %s\n", name);
    return 0;
}
```
실행 예시
```c
이름을 입력하세요: 홍길동
입력된 이름: 홍길동

```
### fgets() 를 사용한 입력
- fgets(문자열배열, 최대 크기, stdin); 을 사용하면 줄 바꿈을 제외한 공백 문자(띄어쓰기, 탭)을 포함한 문자열 입력이 가능합니다.
- 한 줄 입력 이라고 부르기도 합니다.

```c
#include <stdio.h>

int main() {
    char sentence[100];

    printf("문장을 입력하세요: ");
    fgets(sentence, sizeof(sentence), stdin);

    printf("입력된 문장: %s\n", sentence);
    return 0;
}
```
실행 예시
```c
문장을 입력하세요: 나는 홍길동
입력된 문장: 나는 홍길동
```

## 문자열 처리 함수
-> C 언어에서는 string.h 헤더 파일에 문자열을 다루는 다양한 함수가 제공됩니다.
### 문자열 길이 계산(strlen)
- strlen(문자열)은 문자열의 길이를 변환합니다.
- \0 (널 문자)는 길이에 포함되지 않습니다.


```c
#include <stdio.h>
#include <string.h>

int main() {
    char str[] = "C Programming";

    printf("문자열 길이: %lu\n", strlen(str));
    return 0;
}
```
출력
```c
문자열 길이: 13
```

### 문자열 복사(strcpy)
- strcpy(대상문자열, 원본문자열);
	-> 원본 문자열을 대상 문자열로 복사합니다.

출력 예시
```
복사된 문자열: Hello

```

### 문자열 연결(strcat)
- strcat(대상문자열, 추가할 문자열);
	-> 대상문자열 원본에 추가할문자열을 이어붙입니다.

```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[20] = "Hello, ";
    char str2[] = "World!";

    strcat(str1, str2);
    printf("연결된 문자열: %s\n", str1);
    return 0;
}
```
출력
```c
연결된 문자열: Hello, World!
```

### 문자열 비교(strcmp)
- strcmp(str1, str2)
	-> 문자열을 사전순으로 비교한 결과값을 반환합니다.
- str1 이 크면 양수
- str1 과 str2가 동일하면 0
- str1이 작으면 음수
```c
#include <stdio.h>
#include <string.h>

int main() {
    char str1[] = "Apple";
    char str2[] = "Banana";

    int result = strcmp(str1, str2);

    if (result == 0) 
        printf("두 문자열이 같습니다.\n");
    else if (result < 0) 
        printf("%s이(가) %s보다 사전순으로 앞에 위치합니다.\n", str1, str2);
    else 
        printf("%s이(가) %s보다 사전순으로 뒤에 위치합니다.\n", str1, str2);
    
    return 0;
}
```
출력
```c
Apple이(가) Banana보다 사전순으로 앞에 위치합니다.
```

### 부분 문자열 추출(strncpy)
- strncpy(대상문자열, 원본 문자열, 길이);
	-> 원본문자열에서 특정 길이만큼을 앞에서부터 대상문자열에 복사합니다.
	
```c
#include <stdio.h>
#include <string.h>

int main() {
    char src[] = "Hello, World!";
    char dest[6];

    strncpy(dest, src, 5);
    // dest: {'H', 'e', 'l', 'l', 'o'}
    dest[5] = '\0';  // 수동으로 NULL 문자 추가
    // dest: {'H', 'e', 'l', 'l', 'o', '\0'}
    printf("부분 문자열: %s\n", dest);
    
    return 0;
}
```


출력
```c
부분 문자열: Hello
```

## 문자열 배열이란?
- 여러 개의 문자열을 하나의 배열로 관리하고 싶을 때 사용합니다.
- C에서 2차원 char 배열 형태로 선언하며, 이는 1차원 배열의 확장으로 생각할 수 있으며 대괄호 [ ]를 두번 사용하여 선언합니다.

### 선언과 초기화
```c
char names[3][20] = { //3 -> 문자열 갯수, 20 -> 각 문자열의 최대 19글자 + 끝을 표시하는 \0까지 저장 가능한 크기
    "Alice",
    "Bob",
    "Charlie"
};
```
출력 결과
```c
names[0] = Alice
names[1] = Bob
names[2] = Charlie
```

### 사용자 입력 예제
```c
#include <stdio.h>

int main() {
    char fruits[3][20];

    for(int i = 0; i < 3; i++){
        scanf("%s", fruits[i]);
    }

    printf("입력된 과일 목록:\n");
    for(int i = 0; i < 3; i++){
        printf("%s\n", fruits[i]);
    }
    return 0;
}
```
- scanf("%s", fruits[i]);  는 문자열을 입력받아 fruits[i]에 저장합니다. (\0 문자 포함)
- 문자열 입력 시 공백 문자(띄어쓰기, 탭, 줄바꿈 등)를 만나면 입력이 종료되므로, 단어 단위로만 입력됩니다.

입력:
```c
Apple Banana Cherry
```
출력 결과:
```c
입력된 과일 목록:
Apple
Banana
Cherry
```

## 정리
- C에서는 char 배열을 사용하여 문자열을 저장합니다.
- scanf()와 fegets()를 사용하여 문자열을 입력받을 수 있습니다.
- string.h 라이브러리를 활용하여 문자열을 복사(strcpy), 연결(strcat), 비교(strcmp)할 수 있습니다.
- 문자열을 안전하게 다루기 위해 배열 크기와 NULL 문자(\0)를 고려해야 합니다.



