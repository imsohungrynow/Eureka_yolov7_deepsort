from detection_helpers import *
from tracking_helpers import *
from bridge_wrapper import *

detector = Detector() # it'll detect ONLY [person,horses,sports ball]. class = None means detect all classes. List info at: "data/coco.yaml"
detector.load_model('C:/Users/hjw62/Desktop/유레카/yolov7-deepsort-tracking/yolov7.pt',) # pass the path to the trained weight file

tracker = YOLOv7_DeepSORT(reID_model_path="./deep_sort/model_weights/mars-small128.pb", detector=detector)


# 영상 경로
tracker.track_video("C:/Users/hjw62/Desktop/유레카/yolov7-deepsort-tracking/IO_data/input/video/eth_video.mp4", output="C:/Users/hjw62/Desktop/유레카/yolov7-deepsort-tracking/IO_data/output/eth_video_indus.mp4",show_live = False, skip_frames = 0, count_objects = False, verbose=1)

# live webcam
# tracker.track_video(0, output="C:/Users/hjw62/Desktop/유레카/yolov7-deepsort-tracking/IO_data/output/3.mp4",show_live = True, skip_frames = 0, count_objects = False, verbose=1)

# 사람만 tracking path를 그려보자 > 완료
