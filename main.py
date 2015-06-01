from flask import Flask, render_template
from flask.ext.socketio import SocketIO, emit


app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def template_test():
    return render_template('template.html', motd="For help or commands type !help")


@socketio.on("communication", namespace="/mud")
def communicate(message):
    print message
    emit('communication', {"message": "Received"})


@socketio.on('connect', namespace='/mud')
def test_connect():
    emit('communication', {'data': 'Connected'})


@socketio.on('disconnect', namespace='/mud')
def test_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    socketio.run(app)
