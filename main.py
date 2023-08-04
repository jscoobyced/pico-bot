from oled import Oled
from eyes import Eyes
from head import Head
from items import Items
import uasyncio

async def play_eyes(display, pico_items):
    display.create_frames(Eyes.frames)
    print('Starting eyes animation')
    await display.animate(Eyes.around, 3)
    await display.animate(Eyes.blink, 3)
    await display.animate(Eyes.around)
    await display.animate(Eyes.straight)
    print('Done playing eyes animation')
    pico_items.remove()

async def play_head(motor, pico_items):
    print('Starting head animation')
    await motor.init()
    await motor.left(Head.MEDIUM)
    await motor.down(Head.SHORT)
    await motor.right(Head.MEDIUM)
    await motor.up(Head.MEDIUM)
    await motor.front()
    await motor.stop()
    print('Done playing head animation')
    pico_items.remove()

async def play_all(display, motor, items):
    items.add()
    items.add()
    uasyncio.create_task(play_eyes(display, items))
    uasyncio.create_task(play_head(motor, items))
    while items.has_more():
        await uasyncio.sleep_ms(50)
    print("Program completed.")

pico_eye = Oled(0, 128, 64, 16, 17)
pico_head = Head()
pico_items = Items()

def main():
    try:
        uasyncio.run(play_all(pico_eye, pico_head, pico_items))
    except KeyboardInterrupt:
        print('Interrupted.')
    except Error:
        print('Error occured.')
    finally:
        uasyncio.new_event_loop()
        
main() 