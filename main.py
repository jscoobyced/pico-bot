from oled import Oled
from eyes import Eyes
from head import Head
import uasyncio

async def play(display, motor):
    display.create_frames(Eyes.frames)
    print('Starting animation')
    await display.animate(Eyes.around, 3)
    await display.animate(Eyes.blink, 3)
    await display.animate(Eyes.around)
    await display.animate(Eyes.straight)
    await motor.run()
    print('Done')

pico_eye = Oled(0, 128, 64, 16, 17)
pico_head = Head()

uasyncio.run(play(pico_eye, pico_head))

