from app import app 

@app.route("/")
def index():
    reture "Hello from Flask"
