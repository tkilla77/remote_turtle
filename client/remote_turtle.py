import socketio


class RemoteTurtle:
    def __init__(self, name: str):
        self.sio = socketio.AsyncClient()
        self.name = name
    
    async def connect(self, url='http://localhost:5000'):
        await self.sio.connect(url)
        print('my sid is', self.sio.sid)
        await self.sio.emit('join', ('1me', self.name))

    async def straight(self, speed="keep"):
        await self.sio.emit('move', ('1me', self.name, 'forward', speed))

    async def left(self, speed="keep"):
        await self.sio.emit('move', ('1me', self.name, 'left', speed))

    async def right(self, speed="keep"):
        await self.sio.emit('move', ('1me', self.name, 'right', speed))

    async def wait(self):
        await self.sio.wait()
    
    async def disconnect(self):
        await self.sio.disconnect()