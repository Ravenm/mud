from flask import Flask


app = Flask(__name__)
app.config['SECRET_KEY'] = '\x8e \x99\xe2\xc0\xda\xe1\xcdQ\xcb$\x05\xcf\xca\x1e|\xdb\xfa\xb4\x1f\xbd\xbc&\xb2'

from app import views, communication
