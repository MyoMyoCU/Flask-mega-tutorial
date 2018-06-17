from app import app

@app.route('/')
def hello():
    return " My dear say HI"

@app.route('/index')
def index():
    return " hello world "
    
