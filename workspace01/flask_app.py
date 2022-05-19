from flask import Flask
  
app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World\n'

@app.route('/other')
def other():
    return 'Other World\n'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)
