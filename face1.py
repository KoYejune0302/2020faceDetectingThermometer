import asyncio
import io
import glob
import os
import csv
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO

from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person


KEY = "key"

ENDPOINT = "endpoint"

face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))


IMAGE_BASE_URL = 'https://raw.githubusercontent.com/KoYejune0302/2020faceDetectingThermometer/main/'

fd = open('output.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(fd,delimiter=',')
wr.writerow(['name','temperature','check'])
f = open('temperature.txt', 'r')


source_image_file_names = os.listdir('/Users/leekyohyun/Documents/GitHub/2020faceDetectingThermometer/source')

target_image_file_names = os.listdir('/Users/leekyohyun/Documents/GitHub/2020faceDetectingThermometer/target')


for i in range(len(source_image_file_names)):
    print(source_image_file_names[i])

for i in range(len(target_image_file_names)):
    print(target_image_file_names[i])



for i in range(len(source_image_file_names)):
    vs=source_image_file_names[i][-4:-1]
    if(vs=='.jp'):
        pass
    else:
        del source_image_file_names[i]

for i in range(len(target_image_file_names)):
    vt=target_image_file_names[i][-4:-1]
    if(vt=='.jp'):
        pass
    else:
        del target_image_file_names[i]





source_detected_faces_ids = []

for image_file_name in source_image_file_names:

    source_detected_faces = face_client.face.detect_with_url(IMAGE_BASE_URL + 'source/' + image_file_name, detectionModel='detection_03')

    source_detected_faces_ids.append(source_detected_faces[0].face_id)
    print('{} face(s) detected from image {}.'.format(len(source_detected_faces), image_file_name))




target_detected_faces_ids = []

for image_file_name in target_image_file_names:

    target_detected_faces = face_client.face.detect_with_url(IMAGE_BASE_URL + 'target/' + image_file_name, detectionModel='detection_03')

    target_detected_faces_ids.append(target_detected_faces[0].face_id)
    print('{} face(s) detected from image {}.'.format(len(target_detected_faces), image_file_name))





for i in range(len(target_image_file_names)):
    maxConfidenceList=[]
    maxConfidence=maxIndex=0
    for j in range(len(source_image_file_names)):
        verify_result_same = face_client.face.verify_face_to_face(target_detected_faces_ids[i], source_detected_faces_ids[j])
        maxConfidenceList.append(float(verify_result_same.confidence))
        maxConfidence=max(maxConfidenceList)
        maxIndex=maxConfidenceList.index(maxConfidence)
    print(source_image_file_names[maxIndex],target_image_file_names[i])
    name=source_image_file_names[maxIndex][0:-5]

    temperature = f.readline()
    if not temperature: break
    check='T'
    if float(temperature)>=37.5 :
        check = 'F'
    row=[str(name),str(temperature),str(check)]
    wr.writerow(row)

f.close()
#verify_result_same.confidence



'''
print('Faces from {} & {} are of the same person, with confidence: {}'
    .format(target_image_file_names[i], source_image_file_names[j], verify_result_same.confidence)
    if verify_result_same.is_identical
    else 'Faces from {} & {} are of a different person, with confidence: {}'
        .format(target_image_file_names[i], source_image_file_names[j], verify_result_same.confidence))
'''

#csv 작성
'''
fd = open('output.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(fd,delimiter=',')
wr.writerow(['name','temperature','check'])

f = open('temperature.txt', 'r')
i=1
while True:
    name = 'name'+str(i)
    i+=1
    temperature = f.readline()
    if not temperature: break
    check='T'
    if float(temperature)>=37.5 :
        check = 'F'
    row=[str(name),str(temperature),str(check)]
    wr.writerow(row)
f.close()
'''
