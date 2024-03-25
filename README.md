# Autononmous-drone
## 개요
이 프로젝트는 Tello 드론과 Python, YOLO(You Only Look Once) 실시간 객체 감지 알고리즘을 통합하여 고도의 컴퓨터 비전 기능을 구현하고 학습하고자 하였다. 본 시스템은 동적 환경에서 실시간으로 객체 추적 및 얼굴 인식을 수행하며, 색상 추적, 거리 측정 등의 기능을 제공하며 

## 기술 스택
- **Python**: 강력한 프로그래밍 언어로서 알고리즘 설계 및 구현에 사용됩니다.
- **Tello SDK**: 드론의 통제 및 데이터 스트리밍을 위한 인터페이스입니다.
- **OpenCV**: 실시간 컴퓨터 비전을 구현하는 데 사용되는 라이브러리입니다.

## 기능
- **얼굴 추적**: 카메라 데이터를 분석하여 실시간으로 얼굴을 감지하고 추적합니다.
- **객체 추적**: 원하는 색상에 맞는 객체를 추출하여 그 객체를 따라 응답을 조절합니다.
- **거리 측정**: 객체와의 거리를 측정하여 상황에 따른 응답을 조절합니다.

## 성과
이 프로젝트는 실제 환경에서의 테스트를 거쳐 그 유효성이 검증되었습니다. 또한, 통합된 기술 스택은 복잡한 환경에서의 유연한 대응을 가능하게 하며, 스스로 파라미터를 조정하고 그 환경에서 가장 최적화된 값을 찾아보는 값진 경험을 통해서 이후 엔지니어로 성장하는 데 좋은 발판이 되는 개인프로젝트 였다.

## 실행
# 키보드에 따른 드론 제어 및 이미지 스트리밍 실행
project1-keyboardcontrolimagecapture.py

[![tello 자율비행 영상](http://img.youtube.com/vi/vpjdDePQwO4/0.jpg)](https://www.youtube.com/watch?v=vpjdDePQwO4)

# 얼굴 추적을 위해 실행
python FaceTracking.py
[![얼굴인식](https://github.com/wjstndlr/Autononmous-drone/assets/123084818/b47eb75a-ac88-4891-8285-4d16e4aed64b)](https://www.youtube.com/shorts/v4aAWXBdpA8)

# 객체 추적을 위해 실행
python ObjectTracking.py

[![tello 자율비행 영상](http://img.youtube.com/vi/IkuxG3oZ6kA/0.jpg)](https://www.youtube.com/watch?v=IkuxG3oZ6kA)

# 색상 추적을 위해 실행
python ColorPicker.py

# 거리 측정을 위해 실행
python FaceDistanceMeasurement.py
