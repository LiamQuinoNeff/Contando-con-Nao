# -*- coding: utf-8 -*-
import os
import sys
import subprocess
from naoqi import ALProxy
import time
from PIL import Image  # del módulo PIL de Python 2: `pip install PIL` si no lo tienes


ROBOT_IP = "192.168.108.36"
ROBOT_PORT = 9559
temp_path = "temp.jpg"

# Capturar imagen desde la cámara del NAO
try:
    video = ALProxy("ALVideoDevice", ROBOT_IP, ROBOT_PORT)
    name_id = video.subscribeCamera("python_client", 0, 2, 11, 30)
    nao_image = video.getImageRemote(name_id)
    video.unsubscribe(name_id)


    if nao_image is None:
        print("Error: no se pudo capturar imagen desde NAO")
        sys.exit(1)

    width = nao_image[0]
    height = nao_image[1]
    array = nao_image[6]

    # Convertir la imagen a formato RGB y guardar como JPEG
    image = Image.frombytes("RGB", (width, height), array)
    image.save(temp_path, "JPEG")
    print("Imagen guardada en", temp_path)

except Exception as e:
    print("Error capturando imagen desde NAO:", e)
    sys.exit(1)

# Ejecutar el script que detecta dedos
try:
    result = subprocess.check_output(["C:/Python312/python.exe", "detectnumber.py", temp_path])
    result = result.strip()
except Exception as e:
    print("Error ejecutando detectnumber.py:", e)
    sys.exit(1)

# Comunicación con NAO
tts = ALProxy("ALTextToSpeech", ROBOT_IP, ROBOT_PORT)

try:
    if result.isdigit():
        fingers_up = int(result)
        print("You are showing {} fingers.".format(fingers_up))
        tts.say("Estas mostrando " + str(fingers_up) + " deditos.")
    else:
        print("Could not detect fingers.")
        tts.say("Could not detect fingers.")
except Exception as e:
    print("Error corriendo el modelo:", e)
    tts.say("Error running model.")


