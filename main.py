from oled import Oled
from eyes import Eyes
import uasyncio

async def play(display):
    display.create_frames(Eyes.frames)
    print('Starting animation')
    await display.animate(Eyes.around, 3)
    await display.animate(Eyes.blink, 3)
    await display.animate(Eyes.around)
    await display.animate(Eyes.straight)
    print('Done')

eye = Oled(0, 128, 64, 16, 17)

uasyncio.run(play(eye))

