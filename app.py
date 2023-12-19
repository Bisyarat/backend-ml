# app.py

from flask import Flask
from src import main_bp

app = Flask(__name__)

# Registrasi blueprint
app.register_blueprint(main_bp)

# if __name__ == '__main__':
#     app.run(debug=True)
