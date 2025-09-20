# Python


# C
## 강의 목표
- 여러 줄에 걸쳐 입력받는 방법을 익힙니다.

## 여러 데이터 입력받기
- C에서 입력 값은 scanf 함수를 사용하여 입력받습니다. 여러 데이터를 입력받을 때는 각 변수에 대해 scanf를 여러 번 호출하면 됩니다.
```c
#include <stdio.h>

int main() {
    int age;
    double height;

    scanf("%d", &age);
    scanf("%lf", &height);

    printf("나이: %d\n", age);
    printf("키: %.1lf", height);

    return 0;
}
```
입력
```c
30 175.5
```
출력
```c
나이: 30
키: 175.5
```
- 위 코드를 사용하여 아래의 예시처럼 두 줄로 받더라도 정상적으로 입력받을 수 있습니다.
- 이는 scanf가 공백문자를 자동으로 무시하기 때문입니다. 따라서 숫자 입력 사이에 띄어쓰기 혹은 줄바꿈이 있더라도 정상적으로 값을 읽어옵니다. 
입력
```c
30 
175.5
```
출력
```c
나이: 30
키: 175.5
```
- scanf 함수는 여러 데이터를 한줄로 입력받을 수도 있습니다. 예를 들어, 다음과 같이 작성할 수 있습니다.
```c
#include <stdio.h>

int main() {
    int age;
    double height;
    char gender;

    scanf("%d %lf %c", &age, &height, &gender);

    printf("나이: %d\n", age);
    printf("키: %.1lf\n", height);
    printf("성별: %c", gender);

    return 0;
}
```
입력
```c
30 175.5 M
```
출력
```c
나이: 30
키: 175.5
성별: M
```
## 응용 예제: 두줄에 걸쳐 입력받은 정수를 더하기
- 두 줄에 걸쳐 각각 정수를 입력받고, 그 값을 더하여 결과를 출력하는 예제입니다.
```c
#include <stdio.h>

int main() {
    int num1, num2;

    scanf("%d %d", &num1, &num2);

    printf("두 수의 합은 %d입니다.\n", num1 + num2);

    return 0;
}
```
입력
```c
5
10
```
출력
```c
두 수의 합은 15입니다.
```
## 정리
- C에서 scanf 함수는 공백, 탭, 줄바꿈 문자를 기준으로 입력을 구분하여 각 값에 맞는 변수에 저장합니다.
- 여러 데이터를 연속으로 입력받을 때는 scanf를 한 번만 적고, 각 데이터의 형식에 맞는 포맷 지정자(%d, %lf, %c등)를 사용하여 한줄에 


