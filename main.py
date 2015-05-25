from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def template_test():    
    return render_template('template.html', motd="For help or commands type !help")


if __name__ == '__main__':
    app.run(debug=True)
