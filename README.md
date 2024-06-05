# Eureka (동국대학교 산업 IAI 연구실)
<H1 align="center">
YOLOv7 Object Detection with DeepSORT Tracking </H1>

## Eureka Prj 목표
산업 현장 영상으로부터 실시간으로 위험 요소 및 상황을 탐지하고, 경로 예측을 통해 객체 요소 간 충돌을 예측하여 통합 위험도 산출

## 본 Repository
해당 시점의 위험도를 판단하기 위한 객체 탐지 & 추적


## Steps to run Code  
### 초기 세팅 방법!

- Clone the repository
```
git clone https://github.com/imsohungrynow/Eureka_yolov7_deepsort.git
```
- Goto the cloned folder.
```
cd Eureka_yolov7_deepsort
```
- Install the dependecies
```
pip install -r requirements.txt
```

### code run
```
- After downloading the DeepSORT Zip file from the drive, unzip it go into the subfolders and place the deep_sort_pytorch folder into the YOLOv7-DeepSORT-Object-Tracking folder

- Downloading a Sample Video from the Google Drive
```
gdown "https://drive.google.com/uc?id=1rjBn8Fl1E_9d0EMVtL24S9aNQOJAveR5&confirm=t"
```

- Run the code with mentioned command below.

- For yolov7 object detection + Tracking
```
python deep_sort_tracking_id.py --weights yolov7.pt  --img 640  --source test1.mp4  
```


### RESULTS

#### Person detection

## References
1. [YOLOv7: Trainable bag-of-freebies sets new state-of-the-art for real-time object detectors](https://github.com/WongKinYiu/yolov7)
2. [Simple Online and Realtime Tracking with a Deep Association Metric (Deep SORT)](https://github.com/nwojke/deep_sort)
