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

    def create_frames(self, frames):
        print('Loading frames')
        for frame in frames:
            with open(frame, 'rb') as f:
               f.readline()
               f.readline()
               f.readline()
               self.frames.append(bytearray(f.read()))

    async def display_frame(self, frame, duration):
        fb = framebuf.FrameBuffer(frame, self.width, self.height, framebuf.MONO_HLSB)
        self.display.blit(fb, 0,0)
        self.display.show()
        await uasyncio.sleep_ms(duration)

    async def clear(self):
        self.display.fill(0)
        self.display.show()

    async def animate(self, animation, count = 1):
        for loop in range(count):
            for row in animation:
                await self.display_frame(self.frames[row[0]], row[1])
            await self.clear()

