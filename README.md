# Contando con NAO 🤖✋

Este proyecto implementa un sistema de reconocimiento de lenguaje de señas básico (conteo de dedos) utilizando el robot humanoide NAO. A través de OpenCV y visión por computadora, el robot es capaz de identificar cuántos dedos están levantados y anunciar el resultado mediante síntesis de voz.

## 🧠 Objetivo de la Implementación

- Automatizar el reconocimiento de lenguaje de señas manual básico (conteo de dedos) en el robot NAO.
- Integrar visión por computadora en Python/OpenCV con servicios de hardware del robot (cámara y TTS).
- Demostrar cómo desplegar y ejecutar un modelo ligero de IA en un entorno de robótica humanoide.

## 🏗️ Componentes de la Arquitectura

El sistema se compone de dos scripts principales:

### `nao_main.py`
- Se conecta al robot NAO usando la API `naoqi`.
- Captura una imagen desde la cámara frontal del robot.
- Guarda la imagen como archivo JPEG temporal.
- Invoca `detectnumber.py` para procesar la imagen.
- Utiliza `ALTextToSpeech` para anunciar el número de dedos detectados.

### `detectnumber.py`
- Lee la imagen JPEG generada.
- Convierte a escala de grises y aplica desenfoque Gaussiano.
- Segmenta la mano con umbral binario (Otsu).
- Detecta contornos y calcula defectos de convexidad.
- Estima la cantidad de dedos levantados y la imprime por consola.

## ⚙️ Requisitos

### Hardware
- Robot NAO con NAOqi 2.x

### Software
- Python 2.7 o 3.3+  
- Bibliotecas necesarias:
  - `opencv-python`
  - `numpy`
  - `Pillow`
  - `naoqi` (SDK de SoftBank Robotics)

## 🚀 Instrucciones de Instalación

1. **Clonar el repositorio**
   ```
   git clone https://github.com/LiamQuinoNeff/Contando-con-Nao.git
   cd Contando-con-Nao
   ```
   
2. **Configurar entorno Python**
   - Asegúrate de tener las librerías necesarias instaladas:
   ```
   pip install opencv-python numpy Pillow naoqi
   ```
   
4. **Configurar conexión con el robot NAO**
   - Presiona el botón central del NAO para obtener su IP.
   - Edita el archivo `nao_main.py` y reemplaza las variables `ROBOT_IP` y `ROBOT_PORT` con los valores correspondientes.
     
5. **Verificar permisos y entorno**
  - Si usas un entorno virtual, actívalo antes de ejecutar el script.
  - Asegúrate de que los paquetes estén accesibles desde el intérprete Python que usa NAO.

## ▶️ Uso
Con el robot NAO encendido y conectado a la red, ejecuta:
`python nao_main.py`
El robot capturará una imagen, contará los dedos y lo anunciará en voz alta.

## 📹 Demostración
[🎥 Video de presentación](https://upcedupe-my.sharepoint.com/:v:/g/personal/u202122430_upc_edu_pe/ESzSLuvzXg1JixBV3Kkq2tYBTPrh_vWqk3x4m5c4X7oIjg?e=bvWq6C&nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZy1MaW5rIiwicmVmZXJyYWxBcHBQbGF0Zm9ybSI6IldlYiIsInJlZmVycmFsTW9kZSI6InZpZXcifX0%3D)

## 👥 Autores
Proyecto desarrollado por estudiantes de la Universidad Peruana de Ciencias Aplicadas - Curso: Machine Learning - Sección 399
- Nathaly Eliane Anaya Vadillo - U202210644
- Freddy Alejandro Cuadros Contreras - U20221C488
- Salvador Diaz Aguirre - U202216148
- Marsi Figueroa Larragán - U202220990
- José Guillermo Melgar Puertas - U202111660
- Ariana Graciela Quelopana Puppo - U202122430
- Liam Mikael Quino Neff - U20221E167
