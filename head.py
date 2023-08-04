from sc08a import Sc08aController
import uasyncio as asyncio

class Head:
    _speed = 0
    _horizontal = 1
    _vertical = 2
    SHORT = 0
    MEDIUM = 1
    LONG = 2
    
    def __init__(self, speed = 0):
        self._controller = Sc08aController(0)
        self._speed = speed

    async def init(self):
        await self._controller.enable_channel()
        await self.front()

    async def stop(self):
        await self.front()
        await self._controller.close()

    async def front(self):
        await self.move(0, 0, self._horizontal)
        await self.move(0, 0, self._vertical)

    async def right(self, mode):
        await self.front()
        angle = self.get_angle(mode, False)
        await self.move(angle, self._speed, self._horizontal)

    async def left(self, mode):
        await self.front()
        angle = self.get_angle(mode, True)
        await self.move(angle, self._speed, self._horizontal)

    async def down(self, mode):
        await self.front()
        angle = self.get_angle(mode, True)
        await self.move(angle, self._speed, self._vertical)

    async def up(self, mode):
        await self.front()
        angle = self.get_angle(mode, False)
        await self.move(angle, self._speed, self._vertical)

    async def move(self, angle, speed, direction):
        await self._controller.set_angle(angle, speed, direction)

    def get_angle(self, mode, normal):
        coef = 1
        if not normal:
            coef = -1
        angle = 0
        if mode == self.SHORT:
            angle = 30 * coef
        elif mode == self.MEDIUM:
            angle = 60 * coef
        elif mode == self.LONG:
            angle = 90 * coef
        return angle