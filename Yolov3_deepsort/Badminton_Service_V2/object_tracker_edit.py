import time, random
import numpy as np
from absl import app, flags, logging
from absl.flags import FLAGS
import cv2
import matplotlib.pyplot as plt
import tensorflow as tf
from yolov3_tf2.models import (
    YoloV3
)
from yolov3_tf2.dataset import transform_images
from yolov3_tf2.utils import draw_outputs, convert_boxes

from deep_sort import preprocessing
from deep_sort import nn_matching
from deep_sort.detection import Detection
from deep_sort.tracker import Tracker
from tools import generate_detections as gdet
# from PIL import Image
from player import *
import threading

from tkinter import *
import time
import queue

##################################################################################################################
# Global Variables, can be translated to database if it becomes production
lcw = "Lee Chong Wei"
swh = "Son Wan Ho"
lyd = "Lee Yong Dae"
kgj = "Kim Gi Jung"
ksh = "Ko Sung Hyun"
yys = "Yo Yeon Seong"
csg = "Choi Sol Gyu"
wcl = "Wang Chi-Lin"
chl = "Chen Hung-Lin"

lcw_height = 1.72
swh_height = 1.77
lyd_height = 1.76
kkj_height = 1.79
ksh_height = 1.79
yys_height = 1.81
csg_height = 1.81
wcl_height = 1.86
chl_height = 1.77
##################################################################################################################
player_names1 = ["Player 1",lcw,swh,lyd,kgj,ksh,yys,csg,wcl,chl]
player_names2 = ["Player 2",lcw,swh,lyd,kgj,ksh,yys,csg,wcl,chl]
player_names3 = ["Player 3",lcw,swh,lyd,kgj,ksh,yys,csg,wcl,chl]
player_names4 = ["Player 4",lcw,swh,lyd,kgj,ksh,yys,csg,wcl,chl]
player_names5 = ["Player 4",lcw,swh,lyd,kgj,ksh,yys,csg,wcl,chl]
player_heights = [lcw_height,swh_height,lyd_height,kkj_height,ksh_height,yys_height,csg_height]
##################################################################################################################

q = queue.Queue()

print("If no player is present, please at least select None")
def submit():
    global name_1,name_2,name_3,name_4,name_5,height_1,height_2,height_3,height_4,height_5
    name_1 = clicked1.get()
    name_2 = clicked2.get()
    name_3 = clicked3.get()
    name_4 = clicked4.get()
    name_5 = clicked5.get()
    height_1 = playercheck(name_1)
    height_2 = playercheck(name_2)
    height_3 = playercheck(name_3)
    height_4 = playercheck(name_4)
    height_5 = playercheck(name_5)
    # print(name_1,height_1,name_2,height_2,name_3,height_3,name_4,height_4,name_5,height_5)
    return(name_1,height_1,name_2,height_2,name_3,height_3,name_4,height_4,name_5,height_5)

def playercheck(selection):
    if selection == "Lee Chong Wei":
        return lcw_height
    elif selection == "Son Wan Ho":
        return swh_height
    elif selection == "Lee Yong Dae":
        return swh_height
    elif selection == "Kim Gi Jung":
        return kkj_height
    elif selection == "Ko Sung Hyun":
        return ksh_height
    elif selection == "Yo Yeon Seong":
        return yys_height
    elif selection == "Choi Sol Gyu":
        return csg_height
    elif selection == "Wang Chi-Lin":
        return wcl_height
    elif selection == "Chen Hung-Lin":
        return chl_height
    elif "None" or "Select Player" or "Player 1" or "Player 2" or "Player 3" or "Player 4":
        return 1
    else:
        return 1

def playerselection():
    window = Tk()
    window.geometry('400x400')
    window.title("Player Selection")
    label1 = Label(window, text="Player 1: ")
    label1.config(width=10, font=('Helvetica', 10))
    label2 = Label(window, text="Player 2: ")
    label2.config(width=10, font=('Helvetica', 10))
    label3 = Label(window, text="Player 3: ")
    label3.config(width=10, font=('Helvetica', 10))
    label4 = Label(window, text="Player 4: ")
    label4.config(width=10, font=('Helvetica', 10))
    label5 = Label(window, text="If no player is present, please")
    label6 = Label(window, text="at least select Player<Num>")
    global label7, clicked1, clicked2, clicked3, clicked4, clicked5
    label7 = Label(window, text="Test")
    label7.config(width=10, font=('Helvetica', 10))
    label1.grid(row=0,column=0)
    label2.grid(row=1,column=0)
    label3.grid(row=2,column=0)
    label4.grid(row=3,column=0)
    label5.grid(row=5,column=0)
    label6.grid(row=5,column=1)
    label7.grid(row=4,column=0)
    clicked1 = StringVar()
    clicked1.set("Select Player")
    clicked2 = StringVar()
    clicked2.set("Select Player")
    clicked3 = StringVar()
    clicked3.set("Select Player")
    clicked4 = StringVar()
    clicked4.set("Select Player")
    clicked5 = StringVar()
    clicked5.set("Select Player")
    drop1 = OptionMenu(window, clicked1, *player_names1)
    drop1.config(width=20, font=('Helvetica', 10))
    drop2 = OptionMenu(window, clicked2, *player_names2)
    drop2.config(width=20, font=('Helvetica', 10))
    drop3 = OptionMenu(window, clicked3, *player_names3)
    drop3.config(width=20, font=('Helvetica', 10))
    drop4 = OptionMenu(window, clicked4, *player_names4)
    drop4.config(width=20, font=('Helvetica', 10))
    drop5 = OptionMenu(window, clicked5, *player_names5)
    drop5.config(width=20, font=('Helvetica', 10))
    drop1.grid(row=0,column=1)
    drop2.grid(row=1,column=1)
    drop3.grid(row=2,column=1)
    drop4.grid(row=3,column=1)
    drop5.grid(row=4,column=1)
    labelTest1 = Label(text="", font=('Helvetica', 8), fg='red')
    labelTest1.grid(row=4,column=1)
    labelTest2 = Label(text="", font=('Helvetica', 8), fg='red')
    labelTest2.grid(row=5,column=1)
    labelTest3 = Label(text="", font=('Helvetica', 8 ), fg='red')
    labelTest3.grid(row=6,column=1)
    labelTest4 = Label(text="", font=('Helvetica', 8), fg='red')
    labelTest4.grid(row=7,column=1)
    window.mainloop()
##################################################################################################################
flags.DEFINE_string('classes', './data/labels/coco.names', 'path to classes file')
flags.DEFINE_string('weights', './weights/yolov3.tf',
                    'path to weights file')
flags.DEFINE_boolean('tiny', False, 'yolov3 or yolov3-tiny')
flags.DEFINE_integer('size', 416, 'resize images to')
flags.DEFINE_string('video', './data/video/test.mp4',
                    'path to video file or number for webcam)')
flags.DEFINE_string('output', None, 'path to output video')
flags.DEFINE_string('output_format', 'XVID', 'codec used in VideoWriter when saving video to file')
flags.DEFINE_integer('num_classes', 80, 'number of classes in the model')

##################################################################################################################
def main(_argv):
    # Definition of the parameters
    max_cosine_distance = 0.5
    nn_budget = None
    nms_max_overlap = 1.0
    
    #initialize deep sort
    model_filename = 'model_data/mars-small128.pb'
    encoder = gdet.create_box_encoder(model_filename, batch_size=1)
    metric = nn_matching.NearestNeighborDistanceMetric("cosine", max_cosine_distance, nn_budget)
    tracker = Tracker(metric)

    physical_devices = tf.config.experimental.list_physical_devices('GPU')
    if len(physical_devices) > 0:
        tf.config.experimental.set_memory_growth(physical_devices[0], True)

    if FLAGS.tiny:
        yolo = YoloV3Tiny(classes=FLAGS.num_classes)
    else:
        yolo = YoloV3(classes=FLAGS.num_classes)

    yolo.load_weights(FLAGS.weights)
    logging.info('weights loaded')

    class_names = [c.strip() for c in open(FLAGS.classes).readlines()]
    logging.info('classes loaded')

    try:
        vid = cv2.VideoCapture(int(FLAGS.video))
    except:
        vid = cv2.VideoCapture(FLAGS.video)

    out = None

    if FLAGS.output:
        # by default VideoCapture returns float instead of int
        width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(vid.get(cv2.CAP_PROP_FPS))
        codec = cv2.VideoWriter_fourcc(*FLAGS.output_format)
        out = cv2.VideoWriter(FLAGS.output, codec, fps, (width, height))
        list_file = open('detection.txt', 'w')
        frame_index = -1 
    
    fps = 0.0
    count = 0 
    while True:
        _, img = vid.read()

        img_in = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
        img_in = tf.expand_dims(img_in, 0)
        img_in = transform_images(img_in, FLAGS.size)

        t1 = time.time()
        boxes, scores, classes, nums = yolo.predict(img_in)
        classes = classes[0]
        names = []
        for i in range(len(classes)):
            names.append(class_names[int(classes[i])])
        names = np.array(names)
        converted_boxes = convert_boxes(img, boxes[0])
        features = encoder(img, converted_boxes)    
        detections = [Detection(bbox, score, class_name, feature) for bbox, score, class_name, feature in zip(converted_boxes, scores[0], names, features)]

        #initialize color map
        cmap = plt.get_cmap('tab20b')
        colors = [cmap(i)[:3] for i in np.linspace(0, 1, 20)]

        # run non-maxima suppresion
        boxs = np.array([d.tlwh for d in detections])
        scores = np.array([d.confidence for d in detections])
        classes = np.array([d.class_name for d in detections])
        indices = preprocessing.non_max_suppression(boxs, classes, nms_max_overlap, scores)
        detections = [detections[i] for i in indices]        

        # Call the tracker
        tracker.predict()
        tracker.update(detections)

        for track in tracker.tracks:
            if not track.is_confirmed() or track.time_since_update > 1:
                continue 
            submit()
            bbox = track.to_tlbr()
            class_name = track.get_class()
            color = colors[int(track.track_id) % len(colors)]
            color = [i * 255 for i in color]
            cv2.rectangle(img, (int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])), color, 1)
            cv2.rectangle(img, (int(bbox[0]), int(bbox[1]-30)), (int(bbox[0])+(len(class_name)+len(str(track.track_id)))*17, int(bbox[1])), color, -1)
            # if name_1 == "Select Player" or  name_2 == "Select Player" or name_3 == "Select Player" or name_4 == "Select Player" or name_5 == "Select Player" or height_1 == NameError or  height_2 == NameError or height_3 == NameError or height_4 == NameError or height_5 == NameError:
            #     cv2.putText(img, class_name + "-" + str(track.track_id),(int(bbox[0]), int(bbox[1]-10)),0, 0.75, (255,255,255),2)
            if class_name+str(track.track_id) == "Player1":
                cv2.putText(img, name_1 ,(int(bbox[0]), int(bbox[1]-10)),0, 0.75, (255,255,255),2)
                # print("1: ", int(bbox[3]))
                s_height0 = ((int(bbox[3])-(int(bbox[1])))/height_1)*1.15
                new_height_player1 = int(int(bbox[3])-int(s_height0))
                cv2.line(img, (int(bbox[0]), int(new_height_player1)), (int(bbox[2]), int(new_height_player1)), (0,255,0), 2)
            if class_name+str(track.track_id) == "Player2":
                cv2.putText(img, name_2,(int(bbox[0]), int(bbox[1])),0, 0.75, (255,255,255),2)
                # print("2: ", int(bbox[3]))
                s_height1 = ((int(bbox[3])-(int(bbox[1])))/height_2)*1.15
                new_height_player2 = int(int(bbox[3])-int(s_height1))
                cv2.line(img, (int(bbox[0]), int(new_height_player2)), (int(bbox[2]), int(new_height_player2)), (0,255,0), 2)
            if class_name+str(track.track_id) == "Player3":
                cv2.putText(img, name_3,(int(bbox[0]), int(bbox[1])),0, 0.75, (255,255,255),2)
                # print("2: ", int(bbox[3]))
                s_height2 = ((int(bbox[3])-(int(bbox[1])))/height_3)*1.15
                new_height_player3 = int(int(bbox[3])-int(s_height2))
                cv2.line(img, (int(bbox[0]), int(new_height_player3)), (int(bbox[2]), int(new_height_player3)), (0,255,0), 2)
            if class_name+str(track.track_id) == "Player4":
                cv2.putText(img, name_4,(int(bbox[0]), int(bbox[1])),0, 0.75, (255,255,255),2)
                # print("2: ", int(bbox[3]))
                s_height3 = ((int(bbox[3])-(int(bbox[1])))/height_4)*1.15
                new_height_player4 = int(int(bbox[3])-int(s_height3))
                cv2.line(img, (int(bbox[0]), int(new_height_player4)), (int(bbox[2]), int(new_height_player4)), (0,255,0), 2)
            if class_name+str(track.track_id) not in {'Player1','Player2','Player3','Player4'}:
                label7.configure(text=class_name+str(track.track_id))
                if class_name+str(track.track_id) == "Player"+str(track.track_id):
                    cv2.putText(img, name_5,(int(bbox[0]), int(bbox[1])),0, 0.75, (255,255,255),2)
                    # print("2: ", int(bbox[3]))
                    s_height4 = ((int(bbox[3])-(int(bbox[1])))/height_5)*1.15
                    new_height_player5 = int(int(bbox[3])-int(s_height4))
                    cv2.line(img, (int(bbox[0]), int(new_height_player5)), (int(bbox[2]), int(new_height_player5)), (0,255,0), 2)

            
        ### UNCOMMENT BELOW IF YOU WANT CONSTANTLY CHANGING YOLO DETECTIONS TO BE SHOWN ON SCREEN
        #for det in detections:
        #    bbox = det.to_tlbr() 
        #    cv2.rectangle(img,(int(bbox[0]), int(bbox[1])), (int(bbox[2]), int(bbox[3])),(255,0,0), 2)
        
        # print fps on screen 
        fps  = ( fps + (1./(time.time()-t1)) ) / 2
        cv2.putText(img, "FPS: {:.2f}".format(fps), (0, 30),
                          cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 255), 2)
        cv2.imshow('output', img)
        if FLAGS.output:
            out.write(img)
            frame_index = frame_index + 1
            list_file.write(str(frame_index)+' ')
            if len(converted_boxes) != 0:
                for i in range(0,len(converted_boxes)):
                    list_file.write(str(converted_boxes[i][0]) + ' '+str(converted_boxes[i][1]) + ' '+str(converted_boxes[i][2]) + ' '+str(converted_boxes[i][3]) + ' ')
            list_file.write('\n')

        # press q to quit
        if cv2.waitKey(1) == ord('q'):
            break
    vid.release()
    if FLAGS.output:
        out.release()
        list_file.close()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    try:
        x = threading.Thread(target=playerselection)
        x.start()
        y = threading.Thread(target=app.run(main))        
        y.start()
        # app.run(main)
    except SystemExit:
        pass
