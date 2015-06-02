from app import app
from flask import render_template


@app.route('/')
def template_test():
    return render_template('template.html', motd="For help or commands type !help")
