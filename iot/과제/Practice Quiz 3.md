Practice Quiz #3: Counting the Number of Touch Sensor Pressing and  Lightening Led

- Practice Quiz #1은 Polling 방식으로 Touch Sensor를 0.1초 간격으로 센싱하여 Touch Sensor가 눌리면 "Pressed"를 출력하고, Led를 1초 동안 킨다. (Pressed는 눌릴 때만 출력한다)
- Practice Quiz #2은 Interrupt 방식으로 Touch Sensor를 센싱하여 Touch Sensor가 눌리면 "Pressed"를 출력하고, Led를 1초 동안 킨다. 
- 수행을 시작한 이후로, Practice Quiz #1/#2 각각의 프로그램에서, 터치 센서가 눌린 횟수와 Led가 켜진 횟수를 Led가 꺼질 때 마다 출력하도록 프로그램을 수정하시오.
- Practice Quiz #1에서 터치 센서가 눌린 횟수는 interrupt handler에서 센다.
- 예를 들어, 터치 센서가 5번 눌리고, Led가 3번 켜졌다면, 다음과 같이 출력된다:

- "Pressed 5 times and Lightened 3 times."

==> 예상되는 바: Interrupt 방식에서는 Touch 센서가 눌린 횟수와 Led가 켜진 횟수가 동일한데, 

                         Polling 방식에서는 Touch 센서가 눌린 횟수보다 Led가 켜진 횟수가 더 작을 수 있다. (왜냐하면, Led가 켜져 있는 시간을 delay()를 통해 구현하는데, delay()되어 있는 동안에는 코드가 수행을 멈춘 상태이어, 센서 값을 읽을 수 없다.)