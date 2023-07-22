from oled import Oled
import uasyncio

eye = Oled(0, 128, 64, 16, 17)
frames = ["EyeLeft.pbm","EyeRight.pbm",
          "EyeLeft.pbm","EyeRight.pbm",
          "EyeLeft.pbm","EyeRight.pbm",
          "EyeCenter.pbm","EyeClosed.pbm",
          "EyeCenter.pbm","EyeClosed.pbm",
          "EyeCenter.pbm","EyeClosed.pbm",
          "EyeCenter.pbm"]
frame_speed = [200,200,
               200,200,
               200,200,
               100,100,
               100,100,
               100,100,
               100]
eye.create_frames(frames, frame_speed)

async def play():
    print('Starting...')
    await eye.animate(2)
    print('Done')

uasyncio.run(play())

