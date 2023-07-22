from machine import Pin, I2C
import ssd1306
import framebuf
import uasyncio as uasyncio

class Oled:
    width=128
    height=64
    frames = []

    def __init__(self, id, width, height, sda_pin, scl_pin):
        self.width = width
        self.height = height
        self.id = id

        i2c = I2C(id, sda=Pin(sda_pin), scl=Pin(scl_pin))
        self.display = ssd1306.SSD1306_I2C(width, height, i2c)
        self.display.init_display()
        
    def display_text(self, text):
        self.display.text(text, 0, 0)
        self.display.show()

    def create_frames(self, frames, frame_speed):
        self.frame_speed = frame_speed
        for frame in frames:
            with open(frame, 'rb') as f:
               f.readline()
               f.readline()
               f.readline()
               self.frames.append(bytearray(f.read()))

    def next_frame(self, frame):
        fb = framebuf.FrameBuffer(frame, self.width, self.height, framebuf.MONO_HLSB)
        self.display.blit(fb, 0,0)
        self.display.show()

    async def clear(self):
        self.display.fill(0)
        self.display.show()

    async def animate(self, count):
        for i in range(count):
            speed = 0
            for frame in self.frames:
                self.next_frame(frame)
                await uasyncio.sleep_ms(self.frame_speed[speed])
                speed = speed + 1
            await self.clear()

