
# C
## 강의 목표
- cnt, total 변수를 활용하여 이중 for문에서 데이터 집계 방법을 이해합니다.

## 외부 변수를 이용한 이중 for문
- 이전에 배운 이차원 배열을 조금 더 자세히 다뤄봅시다. 영화관 좌석을 구하는 방법을 설명해드리겠습니다. 이차원 배열로 표현된 영화관 좌석에서 'X'로 표시된 빈 좌석의 개수를 세기 위해서는 어떤 방법을 써야 할까요?

### cnt 변수의 개요
- cnt 변수는 반복문 내에서 특정 조건을 만족하는 개수를 세는 데 사용되는 변수입니다.
- 일반적으로 cnt 변수는 0으로 초기화되며, 반복문을 통해 조건이 만족될 때마다 1씩 증가합니다. 이를 통해 조건을 만족하는 요소의 총 개수를 쉽게 계산할 수 있습니다.
- 물론 변수의 이름은 자유롭게 지정할 수 있습니다.

__기본구조__
```c
#include <stdio.h>

int main() {
    int cnt = 0;
    for(int i = 0; i < 행 수; i++) {
        for(int j = 0; j < 열 수; j++) {
            if(조건) {
                cnt++;
            }
        }
    }
    printf("조건을 만족하는 요소의 개수는 %d개입니다.\n", cnt);
    return 0;
}
```

## 실습 예제: 이중 for문과 cnt 변수 사용하기
### 실습 목표
- cnt 변수를 활용하여 이중 for문에서 특정 조건을 만족하는 요소의 개수를 세는 방법을 익힙니다.
### 예제 1: O, X로 이루어진 이차원 배열에서 X의 갯수 세기
```c
#include <stdio.h>

int main() {
    char seat[3][5] = {
        {'O', 'X', 'O', 'O', 'O'},
        {'X', 'O', 'X', 'X', 'X'},
        {'O', 'X', 'O', 'O', 'X'}
    };
    int cnt = 0;

    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 5; j++) {
            if(seat[i][j] == 'X') {
                cnt++;
            }
        }
    }

    printf("%d개\n", cnt);
    return 0;
}
```

출력:
```c
7개
```
### 예제 2. 행과 열이 모두 짝수인 요소의 개수 세기
```c
#include <stdio.h>

int main() {
    int rows = 5;
    int cols = 5;
    int cnt = 0;

    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++) {
            if(i % 2 == 0 && j % 2 == 0) {
                cnt++;
            }
        }
    }

    printf("행과 열이 모두 짝수인 요소의 개수는 %d개입니다.\n", cnt);
    return 0;
}
```

출력:
```c
행과 열이 모두 짝수인 요소의 개수는 9개입니다.
```
### 예제 3: 특정 조건을 만족하는 리스트 요소의 개수 세기
```c
#include <stdio.h>

int main() {
    int matrix[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };
    int cnt = 0;

    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            if(matrix[i][j] > 5) {
                cnt++;
            }
        }
    }

    printf("5보다 큰 수의 개수는 %d개입니다.\n", cnt);
    return 0;
}
```

출력:
```c
5보다 큰 수의 개수는 4개입니다.
```
### 예제 4: 2차원 배열 생성과 cnt 변수 활용하기
```c
#include <stdio.h>

int main() {
    int rows = 3;
    int cols = 3;
    int cnt = 0;
    int matrix[3][3];

    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++) {
            matrix[i][j] = cnt;
            cnt++;
        }
    }

    printf("생성된 2차원 배열:\n");
    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++) {
            printf("%d ", matrix[i][j]);
        }
        printf("\n");
    }

    return 0;
}
```

출력:
```c
생성된 2차원 배열:
0 1 2
3 4 5
6 7 8
```

total 변수의 개요

total 변수란?
- total 변수는 반복문 내에서 특정 조건을 만족하는 요소들의 합계를 계산하는데 사용되는 변수입니다.
- 일반적으로 total 변수는 0으로 초기화되며, 반복문을 통해 조건이 만족 될 때마다 해당 요소의 값을 total에 더해줍니다. 이를 통해 조건을 만족하는 요소들의 총 합계를 쉽게 계산할 수 있습니다.
- 물론 변수의 이름은 자유롭게 지정할 수 있습니다.

__기본구조__
```c
#include <stdio.h>

int main() {
    int total = 0;
    for(int i = 0; i < 행 수; i++) {
        for(int j = 0; j < 열 수; j++) {
            if(조건) {
                total += 요소의 값;
            }
        }
    }
    printf("조건을 만족하는 요소들의 합계는 %d입니다.\n", total);
    return 0;
}
```
예제 설명
```c
#include <stdio.h>

int main() {
    int matrix[3][3] = {
        {1, 2, 3},
        {4, 5, 6},
        {7, 8, 9}
    };

    int total = 0;
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            if(matrix[i][j] % 2 == 0) { // 짝수인 경우
                total += matrix[i][j];
            }
        }
    }
    printf("짝수의 합계는 %d입니다.\n", total);
    return 0;
}
```
출력:
```c
짝수의 합계는 20입니다.
```

## 실습 예제: 이중 for문과 total 변수 사용하기
### 실습 목표
- total변수를 활용하여 이중 for문에서 특정 조건을 만족하는 요소의 합계를 세는 방법을 익힙니다.
### 예제 1: 2차원 리스트 내 홀수들의 합계 계산
```c
#include <stdio.h>

int main() {
    int matrix[3][3] = {
        {10, 3, 5},
        {2, 9, 11},
        {14, 15, 1}
    };

    int total = 0;
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            if(matrix[i][j] % 2 == 1) {  // 홀수인 경우
                total += matrix[i][j];
            }
        }
    }

    printf("홀수들의 합계는 %d입니다.\n", total);
    return 0;
}
```

출력:
```c
홀수들의 합계는 44입니다.
```

### 예제 2: 특정 범위의 수 합계 계산
```c
#include <stdio.h>

int main() {
    int matrix[3][3] = {
        {1, 5, 10},
        {6, 20, 3},
        {7, 8, 2}
    };

    int total = 0;
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            if(matrix[i][j] >= 5 && matrix[i][j] <= 10) {  // 값이 5 이상 10 이하인 경우
                total += matrix[i][j];
            }
        }
    }

    printf("5 이상 10 이하 수들의 합계는 %d입니다.\n", total);
    return 0;
}
```

출력:
```c
5 이상 10 이하 수들의 합계는 36입니다.
```
### 정리
- cnt 변수는 이중 for 문 내에서 특정 조건을 만족하는 요소의 개수를 세는 데 사용됩니다.
- total 변수는 이중 for문 내에서 특정 조건을 만족하는 요소들의 합계를 계산하는데 사용됩니다.
- 이중 for문을 활용하면 이차원 배열이나 매트릭스와 같은 데이터 구조를 효과적으로 탐색하고 처리할 수 있습니다.
- 빈복문과 조건문을 적절히 결합하여 다양한 데이터 집계 작업을 수행할 수 있습니다.












