from flask import Flask

app = Flask(__name__)

@app.route('/')

def Hello():
    return "Hello World"

@app.route('/index')
def index():
    return " I am index"

if __name__ == "__main__":
    app.run(debug=True)
