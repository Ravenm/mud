from flask import Flask, render_template, session
from flask.ext.socketio import SocketIO, emit


app = Flask(__name__)
app.config['SECRET_KEY'] = '\x8e \x99\xe2\xc0\xda\xe1\xcdQ\xcb$\x05\xcf\xca\x1e|\xdb\xfa\xb4\x1f\xbd\xbc&\xb2'
socketio = SocketIO(app)


@app.route('/')
def template_test():
    return render_template('template.html', motd="For help or commands type !help")


@socketio.on("communication", namespace="/mud")
def communicate(message):
    if 'logged' in session:
        if message["data"].startswith("!"):
            print "Command!"
        else:
            message["name"] = session["name"]
            emit('communication', message, broadcast=True)
    elif message["data"].startswith("!register"):
        try:
            name = message["data"].split()[1]
        except IndexError:
            server_communication("Please include a username with your request: !register USERNAME")
            return
        session["logged"] = True
        session["name"] = name
    elif message["data"].startswith("!login"):
        try:
            name = message["data"].split()[1]
        except IndexError:
            server_communication("Please include a username with your request: !login USERNAME")
            return
        session["logged"] = True
        session["name"] = name
    else:
        server_communication("Please login or register with !login USERNAME or !register USERNAME")


def server_communication(msg, broadcast=False):
    emit('communication', {"name": "Server", "data": msg}, broadcast=broadcast)
