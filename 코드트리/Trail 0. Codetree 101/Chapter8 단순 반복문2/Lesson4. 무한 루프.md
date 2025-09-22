# C
## 강의 목표
- while 문을 이용한 무한 루프를 이해합니다.
- break를 이용한 무한 루프의 탈출과 활용법을 이애합니다.

## 무한 루프와 탈출
### 무한 루프란?
- 무한 루프는 조건이 항상 참(true, 1)이어서 종료되지 않는 루프를 의미합니다.
예
```c
#include <stdio.h>

int main() {
    while(1) {
        printf("무한 루프\n");
    }

    return 0;
}
```
실행 예시
```python
무한 루프
무한 루프
무한 루프
...
```
- 이 코드는 사용자가 프르그램을 강제로 종료하지 않는 한 계속해서 "무한 루프"를 출력합니다.

### 탈출 방법
- break문을 사용하여 반복문을 종료할 수 있습니다.
```c
#include <stdio.h>

int main() {
    int user_input;

    while(1) {
        printf("종료하려면 0을 입력하세요: ");
        scanf("%d", &user_input);

        if (user_input == 0) {
            break;
        }

        printf("입력한 값: %d\n", user_input);
    }

    return 0;
}
```
실행 예시
```c
종료하려면 0을 입력하세요: 1
입력한 값: 1
종료하려면 0을 입력하세요: 100
입력한 값: 100
종료하려면 0을 입력하세요: 0
```
0을 입력하면 루프가 종료됩니다.

### 조건을 이용한 반복 제어
- 무한 루프 안에서 특정 조건을 만나면 반복을 종료하는 방법을 배웠습니다. 하지만, while 문의 반복 조건을 잘 설정해 break 문 없이 반복하는 방식도 자주 사용됩니다.
- 조건을 이용한 반복 제어는 특정 조건이 만족 될 때까지 반복을 계속함으써 유동적인 반복 횟수를 설정할 수 있게 해줍니다.

예제: 사용자로부터 양수를 입력받기
```c
#include <stdio.h>

int main() {
    int num = -1; // 첫번째 조건 검사를 통과하기 위한 초기값 설정

    while (num <= 0) {
        printf("양수를 입력하세요: ");
        scanf("%d", &num);

        if (num <= 0) {
            printf("양수가 아닙니다. 다시 시도하세요.\n");
        }
    }

    printf("입력한 양수: %d\n", num);

    return 0;
}
```
실행 결과
```c
양수를 입력하세요: -5
양수가 아닙니다. 다시 시도하세요.
양수를 입력하세요: -15
양수가 아닙니다. 다시 시도하세요.
양수를 입력하세요: 10
입력한 양수: 10
```
#### 사용자 입력을 통한 반복 제어
- 사용자의 입력에 따라 반복을 계속하거나 종료할 수 있습니다.

예제: 로그인 시도 제한
```c
#include <stdio.h>
#include <string.h>

int main() {
    char correct_password[] = "cpp123";
    char password[50];
    int attempts = 0;
    int max_attempts = 3;

    while (attempts < max_attempts) {
        printf("비밀번호를 입력하세요: ");
        scanf("%s", password);

        if (strcmp(password, correct_password) == 0) {
            printf("로그인 성공!\n");
            break;
        } else {
            attempts++;
            printf("비밀번호가 틀렸습니다. %d회 남았습니다.\n", max_attempts - attempts);
        }
    }

    if (attempts >= max_attempts) {
        printf("로그인 시도 횟수를 초과했습니다.\n");
    }

    return 0;
}
```
실행 결과 예시
```c
비밀번호를 입력하세요: wrongpass
비밀번호가 틀렸습니다. 2회 남았습니다.
비밀번호를 입력하세요: wrongpass
비밀번호가 틀렸습니다. 1회 남았습니다.
비밀번호를 입력하세요: cpp123
로그인 성공!
```

### 실습: while문을 활용한 간단한 프로그램 작성
실습 목표
- while 문을 사용하여 다양한 조건을 기반으로 반복 작업을 수행해봅니다.
1. 시작 수 n을 입력받습니다.
2. n이 1이 될 때까지 다음을 반복합니다.
	- n이 짝수이면 n을 2로 나눕니다.
	- n이 홀수이면 n에 3을 곱하고 1을 더합니다.
	- 각 단계의 n값을 출력합니다.


```c
#include <stdio.h>

int main() {
    int n;

    printf("시작 수를 입력하세요: ");
    scanf("%d", &n);

    printf("3n + 1 과정:\n");
    // n이 1이 아닌 동안 무한히 반복되는 while문
    while (n != 1) {
        printf("%d -> ", n);

        if (n % 2 == 0) {
            n = n / 2;
        } else {
            n = 3 * n + 1;
        }
    }
    printf("%d\n", n); // 마지막 1 출력

    return 0;
}
```
실행 결과 예시
```c
시작 수를 입력하세요: 6
3n + 1 과정:
6 -> 3 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
```

### 정리
- 무한 루프는 조건이 항상 참(true, 1)이어서 종료되지 않은 반복 구조입니다.
- break문을 사용하여 무한 루프 또는 다른 반복문을 종료할 수 있습니다.
- 조건을 이용한 반복 제어를 통해 유동적인 반복 횟술르 설정할 수 있으며, 사용자 입력을 기반으로 반복을 제어할 수 있습니다.

