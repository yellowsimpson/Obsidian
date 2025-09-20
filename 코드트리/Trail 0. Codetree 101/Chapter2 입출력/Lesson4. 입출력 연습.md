

# C
## 강의 목표
- 변수와 연산자를 이용하여 기본적인 계산을 수행할 수 있습니다.
- 연산자의 다양한 활용 예시를 통해 실생활 문제를 해결할 수 있습니다.

## 연산자의 다양한 활용 예시
- 연산자는 C언에서 데이터를 처리하고 계산을 수행하는 기본 도구입니다. 이번 강의에서는 두개와 세개의 수의 합과 평균을 계산하는 예제를 통해 연산자의 기본적인 사용법을 익히겠습니다.
### 두개와 세개의 수의 합과 평균 계산
두개의 수를 더하고, 그 합을 2로 나누어 평균을 구합니다.
```c
#include <stdio.h>

int main() {
    // 두 개의 수
    int num1 = 15;
    int num2 = 25;

    // 합 계산
    int total = num1 + num2;
    printf("합: %d\n", total);  // 출력: 합: 40

    // 평균 계산
    double average = (double)total / 2;
    printf("평균: %.2lf\n", average); // 출력: 평균: 20.00

    return 0;
}
```

### 세개의 수의 합과 평균 계산
세 개의 수를 더하고, 그 합을 3으로 나누어 평균을 구합니다.
```c
#include <stdio.h>

int main() {
    // 세 개의 수
    int num1 = 10;
    int num2 = 20;
    int num3 = 30;

    // 합 계산
    int total = num1 + num2 + num3;
    printf("합: %d\n", total);  // 출력: 합: 60

    // 평균 계산
    double average = (double)total / 3;
    printf("평균: %.2lf\n", average); // 출력: 평균: 20.00

    return 0;
}
```
### 응용 예제: 두 개의 수를 입력받아 합과 평균 계산하기
사용자가 두개의 수를 입력하면, 합과 평균을 계산하는 프로그램을 작성할 수 있습니다.
```c
#include <stdio.h>

int main() {
    // 사용자로부터 두 개의 수 입력받기
    int num1_input, num2_input;

    printf("첫 번째 수를 입력하세요: ");
    scanf("%d", &num1_input);

    printf("두 번째 수를 입력하세요: ");
    scanf("%d", &num2_input);

    double num1 = (double)num1_input;
    double num2 = (double)num2_input;

    double total = num1 + num2;
    double average = total / 2;

    printf("합: %.2lf\n", total);
    printf("평균: %.2lf\n", average);

    return 0;
}
```
실행 예시
```c
첫 번째 수를 입력하세요: 25
두 번째 수를 입력하세요: 60
합: 85.00
평균: 42.50
```
이런한 방식으로, 두개의 수의 합과 평균을 쉽게 계산할 수 있습니다.

### 추가 예시: BMI 계산하기
연산자의 활용 예시를 하나 더 살펴보겠습니다. BMI(체질량 지수)를 계산하는 프로그램을 작성해보겠습니다.

```c
#include <stdio.h>

int main() {
    // 몸무게와 키를 입력받습니다.
    double weight;
    printf("몸무게(kg)를 입력하세요: ");
    scanf("%lf", &weight);

    double height;
    printf("키(m)를 입력하세요: ");
    scanf("%lf", &height);

    // BMI를 계산합니다.
    double bmi = weight / (height * height);

    // 결과를 출력합니다.
    printf("당신의 BMI는 %.2lf 입니다.\n", bmi);

    return 0;
}
```
실행 예시
```c
몸무게(kg)를 입력하세요: 70
키(m)를 입력하세요: 1.75
당신의 BMI는 22.86 입니다.
```
BMI 계산 예제는 연산자를 활용하여 실생화에서 유용한 정보를 도출하는 방법을 보여줍니다. 이처럼 연산자는 다양한 문제를 해결하는데 필수적인 도구입니다.
## 정리
- 변수를 통해 데이터를 저장하고, 다양한 연산자를 사용하여 계산을 수행할 수 있습니다.
- 합과 평균 계산을 예시로 연산자의 기본적인 활용법을 배웠습니다.



