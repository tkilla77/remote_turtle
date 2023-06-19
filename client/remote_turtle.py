import socketio


class RemoteTurtle:
    def __init__(self):
        self.sio = socketio.AsyncClient()
    
    async def connect(self, url='http://localhost:5000'):
        await self.sio.connect(url)
        print('my sid is', self.sio.sid)
        await self.sio.emit('join', ('1me', 'tkilla'))

    async def forward(self):
        await self.sio.emit('move', ('1me', 'tkilla', 'forward', 'accel'))

    async def left(self):
        await self.sio.emit('move', ('1me', 'tkilla', 'left', 'accel'))

    async def right(self):
        await self.sio.emit('move', ('1me', 'tkilla', 'right', 'accel'))

    async def wait(self):
        await self.sio.wait()
    
    async def disconnect(self):
        await self.sio.disconnect()