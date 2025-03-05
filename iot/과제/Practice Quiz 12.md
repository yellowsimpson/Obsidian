Practice Quiz 12- Remote Sensing of Sound Sensor via HTML(UI), Javascript, WebSocket, Flask, Flask SocketIO, and Plotly.

Remote Sensing of Sound Sensor via HTML(UI), Javascript, WebSocket, Flask, Flask SocketIO, and Plotly

Refer to Light Sensor Monitoring

 * flask_websocket_sensor_control.zip

    - app.py

    - templates/

        index.html

        iot_with_flask.js

==============

위 제공 소스에 있는 LED 제어는 하지 않음

Light 대신 Sound 센서에 대한 모니터링

"**Number of Measurements:"**의 텍스트 박스에 적힌 값의 횟수 만큼 **1**초 간격으로 **sound** 센서 값을 측정하여**,** 

Plotly로 그래프를 그려줌

X축은 시:분:초, Y축은 sound 센서 값