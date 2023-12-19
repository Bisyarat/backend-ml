from flask import Flask

app = Flask(__name__)

@app.route('/proses-cinta')
def index():
    return "hello world"

 
if __name__ == '__main__':
    app.run(debug=True)