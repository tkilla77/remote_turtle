from flask_socketio import SocketIO

class SocketDisplay:
    def __init__(self, socket: SocketIO):
        self.socket = socket
        self.players = {}

    def new_player(self, name: str):
        if name in self.players:
            raise Exception(f"Player name already taken: {name}")
        player = SocketTurtle(self)
        self.players[name] = player
        return player
    
    def remove_player(self, name: str):
        player = self.players.pop(name)
        player.ht()
    
    def get_player(self, name: str):
        return self.players[name]
    
    def forward(self, distance):
        self.socket.emit('move', distance)
    
    def left(self):
        self.socket.emit('left', 45)

    def right(self):
        self.socket.emit('right', 45)

class SocketTurtle:
    speed_increment = 10
    max_speed = 50
    min_speed = 0

    def __init__(self, display: SocketDisplay):
        self.display = display
        self.speed = 0

    def forward(self, acceleration: str):
        match acceleration:
            case 'faster': change = SocketTurtle.speed_increment
            case 'slower': change = -SocketTurtle.speed_increment
        
        self.speed = max(SocketTurtle.min_speed,
                         min(SocketTurtle.max_speed,
                             self.speed + change))
        self.display.forward(self.speed)
    
    def left(self):
        self.display.left()

    def right(self):
        self.display.right()
