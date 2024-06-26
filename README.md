# Eureka (동국대학교 산업 IAI 연구실)  
## 최종 목표
산업 현장 영상으로부터 실시간으로 위험 요소 및 상황을 탐지하고, 경로 예측을 통해 객체 요소 간 충돌을 예측하여 통합 위험도 산출  
<H1 align="center"><font color="green">
YOLOv7 Object Detection with DeepSORT Tracking</font></H1>

## 본 Repository
#### 해당 시점의 위험도를 판단하기 위한 객체 탐지 & 추적
###### 탐지 객체
- person, forklift, helmet

###### 탐지 상황
- UA-10 : 지게차 이동 통로에 사람이 있는 상황
- UA-12 : 포크에 사람 탑승 금지 미준수 상황
- UA-13 : 화물의 적재상태 불량 및 붕괴된 상황
- falling : 작업자 부상 상황


## Steps to run Code  

### 환경 만들기
- Create anaconda environment
```
conda create -n {env name} python=3.9
```

### 초기 세팅 방법!

- Clone the repository
```
git clone https://github.com/imsohungrynow/Eureka_yolov7_deepsort.git
```
- Goto the cloned folder.
```
cd Eureka_yolov7_deepsort
```
- Install the requirements
```
pip install -r requirements.txt
```
### 가중치 파일
[Deepsort .pb 파일](https://drive.google.com/drive/folders/1bw8JRDOHJoo0Tlb2leswPdCUObU1igSA?usp=drive_link)  
[YOLOv7 .pt 파일](https://drive.google.com/drive/folders/1oA3fO3xlSxbzHaqAyOAZI5WsEc9tQJh1?usp=drive_link)
- 각각 tracking_video.py 파일에 detector와 tracker 에 할당

## code run
### ./tracking_video.py 진입

#### 객체 탐지를 위한 Yolo 가중치 파일 경로 설정
```
detector.load_model('path_{.pt}') 
```

### 실행하고 싶은 목적에 따라 주석처리하여 실행
- data 경로
  - IO_data/output/{video name}  

#### local video 탐지 및 추적 
아래 코드 실행 
```
tracker.track_video("Local_video_path", output="Local_output_path",show_live = False, skip_frames = 0, count_objects = False, verbose=1)

```
#### real-time 탐지 및 추적
- webcam 연결
아래 코드 실행
```
tracker.track_video(0, output="Local_output_path",show_live = True, skip_frames = 0, count_objects = False, verbose=1)
```

### RESULTS
1. ./IO_data/output
- 객체 탐지 및 추적화 된 video
2. ./track/result
- Frame, ID, X, Y (x, y == Bounding box의 중앙좌표) 의 excel file

#### Person detection

## References
1. [YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors](https://github.com/WongKinYiu/yolov7)
2. [Simple Online and Realtime Tracking with a Deep Association Metric (Deep SORT)](https://github.com/nwojke/deep_sort)
