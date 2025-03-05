Practice Quiz #4: Counting the Number of Switch Sensor Pressing and Playing Buzzer in Polling Approach

- Polling 방식으로 Switch Sensor를 0.1초 간격으로 센싱하여 Switch Sensor가 눌리면 "Pressed.\n"를 출력하고, Buzzer를 1초 동안 울린다. (Pressed는 눌릴 때만 출력한다)
- 수행을 시작한 이후로, 스위치 센서가 눌린 횟수와 Buzzer가 울린 횟수를 Buzzer가 꺼질 때 마다 출력하시오.
- 스위치 센서가 눌린 횟수는 interrupt handler에서 센다.
- 예를 들어, 스위치 센서가 5번 눌리고, Buzzer가 3번 울렸다면, 다음과 같이 출력된다:

- "Pressed 5 times and Buzzed 3 times."

- 제출자료는 C 소스 코드 하나 (텍스트 코드로 그냥 붙여도 됨)