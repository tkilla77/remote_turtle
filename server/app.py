import json
from flask import Flask, render_template
from flask_socketio import SocketIO
import turtle_display

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

games = {}

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@socketio.event
def join(game: str, player: str):
    # FIXME access control
    if game not in games:
        display = turtle_display.TkDisplay()
        games[game] = display
    else:
        display = games[game]
    display.new_player(player)
    return { 'game' : game, 'player' : player}

@socketio.event
def move(game: str, player: str, steering: str, speed: str):
    # FIXME access / session control
    turtle = games[game].get_player(player)
    match steering:
        case 'left': turtle.left(-45)
        case 'right': turtle.left(45)
    turtle.move(speed)

if __name__ == '__main__':
    socketio.run(app)