import json
from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html', async_mode=socketio.async_mode)

@socketio.event
def hello(name):
    print('received name: ' + str(name))
    return f"Hello, {name['data']}"

if __name__ == '__main__':
    socketio.run(app)