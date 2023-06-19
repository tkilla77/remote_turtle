import threading
import turtle

class TurtleWrapper(turtle.RawTurtle):
    speed_increment = 10
    max_speed = 50
    min_speed = 0

    def __init__(self, screen, shape):
        super().__init__(screen, shape, undobuffersize=0)
        self.speed = 0
    
    def move(self, acceleration: str):
        match acceleration:
            case 'accel': change = TurtleWrapper.speed_increment
            case 'break': change = -TurtleWrapper.speed_increment
        
        self.speed = max(TurtleWrapper.min_speed,
                                           min(TurtleWrapper.max_speed,
                                               self.speed + change))
        self.forward(self.speed)

class TkDisplay:
    def __init__(self, width: int = 2000, height: int = 1500):
        self.canvas = turtle.ScrolledCanvas(master=None, width=width, height=height, canvwidth=width, canvheight=height)
        self.screen = turtle.TurtleScreen(self.canvas)
        thd = threading.Thread(target=self.screen.mainloop)   # gui thread
        thd.daemon = True
        thd.start()
        self.players = {}
    
    def new_player(self, name: str) -> turtle.RawTurtle:
        if name in self.players:
            raise Exception(f"Player name already taken: {name}")
        player = TurtleWrapper(self.screen, shape='turtle')
        self.players[name] = player
        return player
    
    def remove_player(self, name: str) -> None:
        player = self.players.pop(name)
        player.ht()
    
    def get_player(self, name: str) -> turtle.RawTurtle:
        return self.players[name]

