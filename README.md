# 2020faceDetectingThermometer
2020 소프트웨어 산출물 대회<br>
아두이노를 이용한 얼굴 인식 체온계<br>
## 사용언어
python, C
## 사용도구
ArduinoUNO, RGB_LED, Thermometer, Button
## 개발툴
ATOM, ARDUINO, VScode
## 제작동기
현재 모든 학교에서 COVID-19의 확산을 막기 위하여 식사 시간 전 발열 체크를 진행하여 기록하고 있다. 하지만 이 과정은 모두 수동으로 이루어지기에 무척이나 번거로울 뿐만 아니라 허위로 기재하는 것도 수월하다는 문제점이 있다. 이에 본 팀은 자동으로 체온을 측정하고 해당 학생의 정보와 체온을 기록하는 장비를 만들어 수동으로 발열 체크를 진행하는 시스템을 대체함으로써 이러한 문제점들을 해결하고자 하였다. 더 나아가 이전에는 수필로 작성된 자료였기에 자료 분석이 어려웠으나 이 작품을 통하여 개선될 것이라 예상한다.
## 작품요약
작품을 만들 때 온도 측정 및 사진 촬영을 위하여 아두이노를 사용하였다. 사람의 체온을 측정하기 위해서는 비접촉식 적외선 온도 센서를 이용하였다. 또한, 그 사람이 누구인지 식별하기 위한 과정에서 Arducam으로 사람을 촬영하고 해당 사진을 Microsoft Face API를 이용하여 얼굴을 인식하였다. 
이 작품 사람의 체온을 비접촉식으로 측정한 뒤, 그 사람이 누구인지를 식별하고 이름과 체온을 기록하는 장치이다. 이 작품을 통하여 더욱 편리하게 발열 체크를 할 수 있다. 카메라 앞에 서서 장치의 버튼을 누르면 체온이 측정됨과 동시에 사진이 촬영된다. 그리고 이 사진을 바탕으로 누구인지를 식별하고 이름과 체온이 기록된다. 이전까지는 사람이 직접 체온을 측정한 후 측정 시각과 자신의 이름을 수기로 작성하기 때문에 번거로움이 있었으나 이 작품을 통하여 이러한 문제를 해결할 수 있다. 또한 체온을 측정하고 기록하는 시간이 대폭 줄어들기에 대학수학능력시험, 학교, 병원과 같이 사람이 많이 몰리는 장소에서 유용하게 쓰일 수 있을 것이다. 더 나아가 이렇게 체계적으로 기록된 데이터를 분석하게 된다면 COVID-19의 역학 조사에 큰 도움이 될 것이라 예상한다. 
이 작품이 실용화된다면 각자의 얼굴이 담긴 사진, 방문 여부, 체온 등과 같은 개인정보의 보호에 대하여 의문이 제기될 수 있다. 그래서 일정 시간이 지났을 때 저장했던 정보를 삭제하는 기능을 추가하여 이러한 걱정을 줄일 수 있도록 하였다.
<br>
<br>
<img src="https://github.com/KoYejune0302/2020faceDetectingThermometer/blob/main/source/seulgi1.jpg?raw=true">
