import asyncio
import io
import glob
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
# To install this module, run:
# python -m pip install Pillow
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person

# This key will serve all examples in this document.
KEY = "fa886e006ae64c50b7a053ec52130f5d"

# This endpoint will be used in all examples in this quickstart.
ENDPOINT = "https://leekyohyun.cognitiveservices.azure.com/"

face_client = FaceClient(ENDPOINT, CognitiveServicesCredentials(KEY))

# Base url for the Verify and Facelist/Large Facelist operations
IMAGE_BASE_URL = 'https://raw.githubusercontent.com/KoYejune0302/2020faceDetectingThermometer/main/'



# The source photos contain this person
source_image_file_names = os.listdir('/Users/leekyohyun/Documents/GitHub/2020faceDetectingThermometer/source')
# Create a list to hold the target photos of the same person
target_image_file_names = os.listdir('/Users/leekyohyun/Documents/GitHub/2020faceDetectingThermometer/target')

for i in range(len(source_image_file_names)):
    print(source_image_file_names[i])



'''
# Detect face(s) from source image 1, returns a list[DetectedFaces]
# We use detection model 2 because we are not retrieving attributes.
detected_faces1 = face_client.face.detect_with_url(IMAGE_BASE_URL + source_image_file_name1, detectionModel='detection_02')
# Add the returned face's face ID
source_image1_id = detected_faces1[0].face_id
print('{} face(s) detected from image {}.'.format(len(detected_faces1), source_image_file_name1))

# Detect face(s) from source image 2, returns a list[DetectedFaces]
detected_faces2 = face_client.face.detect_with_url(IMAGE_BASE_URL + source_image_file_name2, detectionModel='detection_02')
# Add the returned face's face ID
source_image2_id = detected_faces2[0].face_id
print('{} face(s) detected from image {}.'.format(len(detected_faces2), source_image_file_name2))
'''


# List for the source face IDs (uuids)
source_detected_faces_ids = []
# Detect faces from target image url list, returns a list[DetectedFaces]
for image_file_name in source_image_file_names:
    # We use detection model 2 because we are not retrieving attributes.
    source_detected_faces = face_client.face.detect_with_url(IMAGE_BASE_URL + 'source/' + image_file_name, detectionModel='detection_03')
    # Add the returned face's face ID
    source_detected_faces_ids.append(source_detected_faces[0].face_id)
    print('{} face(s) detected from image {}.'.format(len(source_detected_faces), image_file_name))



# List for the target face IDs (uuids)
target_detected_faces_ids = []
# Detect faces from target image url list, returns a list[DetectedFaces]
for image_file_name in target_image_file_names:
    # We use detection model 2 because we are not retrieving attributes.
    target_detected_faces = face_client.face.detect_with_url(IMAGE_BASE_URL + 'target' + image_file_name, detectionModel='detection_03')
    # Add the returned face's face ID
    target_detected_faces_ids.append(target_detected_faces[0].face_id)
    print('{} face(s) detected from image {}.'.format(len(target_detected_faces), image_file_name))

# Verification example for faces of the same person. The higher the confidence, the more identical the faces in the images are.
# Since target faces are the same person, in this example, we can use the 1st ID in the detected_faces_ids list to compare.
'''
verify_result_same = face_client.face.verify_face_to_face(source_detected_faces_ids[0], target_detected_faces_ids[0])
print('Faces from {} & {} are of the same person, with confidence: {}'
    .format(source_image_file_names[0], target_image_file_names[0], verify_result_same.confidence)
    if verify_result_same.is_identical
    else 'Faces from {} & {} are of a different person, with confidence: {}'
        .format(source_image_file_names[0], target_image_file_names[0], verify_result_same.confidence))
'''

for i in range(len(source_image_file_names)):
    verify_result_same = face_client.face.verify_face_to_face(source_detected_faces_ids[i], target_detected_faces_ids[1])
    print('Faces from {} & {} are of the same person, with confidence: {}'
        .format(source_image_file_names[i], target_image_file_names[1], verify_result_same.confidence)
        if verify_result_same.is_identical
        else 'Faces from {} & {} are of a different person, with confidence: {}'
            .format(source_image_file_names[i], target_image_file_names[1], verify_result_same.confidence))


