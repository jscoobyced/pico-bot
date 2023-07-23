
class Eyes:
    image_left = "images/EyeLeft.pbm"
    image_right = "images/EyeRight.pbm"
    image_center = "images/EyeCenter.pbm"
    image_closed = "images/EyeClosed.pbm"
    frames = [image_left, image_right, image_center, image_closed]
    left=0
    right=1
    center=2
    closed=3
    speed_fast=100
    speed_normal=200
    speed_slow=500
    
    blink=[[center, speed_fast],[closed, speed_fast]]
    around=[[left, speed_normal],[right, speed_normal]]
    straight=[[center, speed_slow]]
