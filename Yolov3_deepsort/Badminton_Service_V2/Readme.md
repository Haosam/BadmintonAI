## Did an Update of the Badminton Service Repository

*For a Proper Understanding of this, please just read this [Badminton Service V1](https://github.com/Haosam/BadmintonAI/tree/master/Yolov3_deepsort/Badminton_Service)

### Changelog
- Added multithreading to enable GUI change of player with the video
- Dynamic Changing of the player (Not properly coded, but it works)
![Demo of how it works](data/demo.gif)

# *Current Usage of this code*
```
A) REPLACE object_tracker_edit.py in Badminton_Service (The older repo) with thie object_tracker_edit.py in this repo!
B) You may choose to remove player.py as it is not required


1) Run python object_tracker_edit.py --video ./data/video/b1.mp4 --output ./data/video/b1results.avi --weights ./weights/yolov3-custom.tf --num_classes 1 --classes ./data/labels/obj.names
2) Select any player for fun
3) Let video run and select player according to the players shown on the screen
4) Let video process
5) Done
```

### Current flaws of this code
- [ ] Multithreaded GUI was used, but not properly closed. When the window is X-ed prematurely, the code logs and error. After full video processed, video is developed and produced in the output folder, but it is not closed properly either
- [ ] Multiple player detections. If the player detection exceed more than 5 players, it will detect all the players as the same player. So for example, if 2 or more players walk out of the frame and back in, they are detected as Player 5,6,7,etc... I could write a 10-player preset in the GUI, but it would be meaningless if it exceeds again. I have not been able to figure out how to streamline the process on detecting Player 5, Player 6, Player 7, etc...
- [ ] Small dataset. Please train on your own dataset if mine is not working properly on your videos. Like I said before, I only trained on 400+ images
- [ ] Lesser FPS due to longer code. I think processing rate dropped...
