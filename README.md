# 2020faceDetectingThermometer
2020 소프트웨어 산출물 대회<br>
아두이노를 이용한 얼굴 인식 체온계<br>
## Development languages
python, C
## Crafting materials
ArduinoUNO, RGB_LED, Thermometer, Button
## Development tools
ATOM, ARDUINO, VScode
## Production motive
Currently, in order to prevent the spread of COVID-19 in all schools, a fever check is performed before meal time and recorded. However, there is a problem that this process is not only very cumbersome because it is all done manually, but it is also easy to write false information. Therefore, the team attempted to solve these problems by replacing a system that automatically measures body temperature and records the student's information and body temperature, and manually performs a heat check. Furthermore, it was difficult to analyze the data because it was previously written by essay, but it is expected that it will be improved through this work.
## Work sumamry
When creating the work, Arduino was used to measure temperature and take pictures. In order to measure a person's body temperature, a non-contact infrared temperature sensor was used. In addition, in the process of identifying who the person is, the person was photographed with Arducam and the face was recognized using the Microsoft Face API.
This is a device that measures a person's body temperature in a non-contact manner, identifies who the person is, and records the name and body temperature. Through this work, you can check the heat more conveniently. If you press the button on the device in front of the camera, the body temperature is measured and a picture is taken at the same time. And based on this photo, who is identified, and the name and body temperature are recorded. Previously, it was cumbersome because a person manually measured the body temperature and then wrote the measurement time and his or her name manually, but this work can solve these problems. In addition, since the time to measure and record body temperature is drastically reduced, it will be useful in places where there are a lot of people, such as college entrance exams, schools, and hospitals. Further, it is expected that it will be of great help to the epidemiological investigation of COVID-19 if the data recorded in this way is systematically analyzed.
If this work is put into practice, questions may be raised regarding the protection of personal information, such as a photograph of each person's face, visitation status, and body temperature. Therefore, a function to delete information stored when a certain time has elapsed has been added to reduce this worry.
<br>
<br>
<img src="https://github.com/KoYejune0302/2020faceDetectingThermometer/blob/main/source/seulgi1.jpg?raw=true">
