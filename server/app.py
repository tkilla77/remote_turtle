import json
from flask import Flask, render_template
from flask_socketio import SocketIO
import socket_display

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

games = {}

@app.route('/<game>')
def index(game: str):
    return render_template('index.html', async_mode=socketio.async_mode)

@socketio.event
def join(game: str, player: str):
    # FIXME access control
    if game not in games:
        display = socket_display.SocketDisplay(socketio)
        games[game] = display
    else:
        display = games[game]
    display.new_player(player)
    return { 'game' : game, 'player' : player}

@socketio.event
def move(game: str, player: str, direction: str, speed: str):
    # FIXME access / session control
    turtle = games[game].get_player(player)
    match direction:
        case 'left': turtle.left()
        case 'right': turtle.right()
    turtle.forward(speed)

if __name__ == '__main__':
    socketio.run(app)