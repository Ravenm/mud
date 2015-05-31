from flask import Flask, render_template
from flask_socketio import SocketIO, emit
app = Flask(__name__)
socketio = SocketIO(app)


@app.route('/')
def template_test():
    return render_template('template.html', motd="For help or commands type !help")


@socketio.on("communication", namespace="/mud")
def communicate(message):
    print message
    emit('communication', {"message": "Received"})


if __name__ == '__main__':
    app.run(host='0.0.0.0')
