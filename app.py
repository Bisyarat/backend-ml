# app.py
import os
from flask import Flask
from src import main_bp

app = Flask(__name__)
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials/ServiceKeyCloudGCP.json'

app.register_blueprint(main_bp)

if __name__ == '__main__':
    app.run(debug=True)
