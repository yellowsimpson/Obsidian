

thread를 사용하는 이유?

`thread`를 사용하는 이유는 **하나의 프로그램 안에서 동시에 여러 작업을 수행하기 위해서**예요. 조금 더 풀어서 설명하면:

1. 병렬(동시) 실행

- 프로그램이 순차적으로 한 줄씩만 실행된다면, 오래 걸리는 작업(예: 파일 다운로드, 네트워크 통신, 센서 데이터 읽기 등)을 하는 동안 다른 작업은 멈추게 돼요. 
- 스레드를 사용하면 이런 작업들을 **동시에 실행**시켜서, 한쪽이 기다리는 동안 다른 쪽이 계속 진행될 수 있어요.

2. 프로그램 응답성 향상

- GUI 프로그램에서 버튼을 눌렀을 때, 내부에서 오래 걸리는 계산을 메인 스레드에서 처리하면 UI가 "멈춘 것처럼" 보여요.
- 이 계산을 **별도의 스레드**로 넘기면, 메인 스레드는 계속 UI 이벤트를 처리해서 프로그램이 끊기지 않고 매끄럽게 반응할 수 있어요.

3. 멀티코어 CPU 활용

- CPU가 코어가 여러 개인 경우, 스레드를 사용하면 **여러 코어에서 병렬 실행**이 가능해져 성능이 향상돼요.
- 특히 C, C++, Java 같은 언어에서는 연산량이 큰 작업을 나눠 스레드별로 처리하면 실행 속도가 훨씬 빨라질 수 있어요.  
    (단, 파이썬은 GIL(Global Interpreter Lock) 때문에 CPU 연산에서는 완전 병렬 실행이 안 되지만, I/O 작업에는 효과적임)
    
4. 구조적 장점

- 코드 구조를 단순화할 수 있어요.  
    예를 들어 "센서 읽기 → 제어 → 통신"을 한 스레드에서 순서대로 돌리는 대신,  
    **센서 읽기 스레드 / 제어 스레드 / 통신 스레드**로 나누면 각 기능이 독립적으로 동작하고 유지보수가 쉬워져요.
    
👉 요약  
스레드를 사용하는 이유는 **동시에 여러 작업을 처리해서 프로그램의 속도와 응답성을 높이고, 멀티코어를 활용할 수 있기 때문**이에요.


성능을 높이는 과정에서 
1. lifecycle -> node에는 lifecycle이 있다.
2. thread
3. 플러그인
4. 동기식/비동기식
5. 통신은 뭘 짜 봤는지
6. 서버 클라이언드 방법이 뭔지
7. tcp/ip 차이점이 뭔지
취업 면접에서 물어봄

등에 대해서 고려해본다.

- topic
- service
- node
의 차이점 잘 알아야되


클라이언드가 동작할려면 서버가 레디(동작) 상태에 있어야된다.
액션 서버 만들고
액션 클라이언트 만들고
동작되는지 확인



인터페이스 만들때는 항상 cmake로 만들어야된다.

![[실습 이미지.png]]




- 서비스 인터페이스
```python
import rclpy
from rclpy.node import Node
from my_interfaces_pkg.srv import CustomService
								# 직접 정의한 서비스 타입

class CustomServiceServer(Node):
    def __init__(self):
        super().__init__('custom_service_server')
        self.srv = self.create_service(CustomService, 'custom_service', self.service_callback)

    def service_callback(self, request, response):
        response.output = f"Received: {request.input}" # -> input
	        self.get_logger().info(f'Input: {request.input}, Output: {response.output}') # -> output
        return response
        #여기에 우리가 원하는 기능을 넣으 주면 됨
		#        


def main(args=None):
    rclpy.init(args=args)
    node = CustomServiceServer()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```



![[실습 사진.png]]

