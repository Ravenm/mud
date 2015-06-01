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
    if message["data"].startswith("!"):
        print "Command!"
    else:
        emit('communication', message, broadcast=True)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
