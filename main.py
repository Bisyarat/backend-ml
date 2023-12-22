# app.py
import os
from flask import Flask
from src import main_bp
from flask import request ,jsonify
from PredictVideo import PredictVideo

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'credentials/ServiceKeyCloudGCP.json'

ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mkv', 'mov'} 
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main_bp.route('/upload_video', methods=['POST'])
def upload_video():
    file = request.files['video']
    
    if file and allowed_file(file.filename):
    
        predict_video_instance = PredictVideo()
        result_predict , url_video = predict_video_instance.predict_and_upload(file)
        
        return jsonify({
                    "data" : {
                        "result_accuracy" : result_predict,
                        "url_video" : url_video
                    }       
                })

    return 'File not allowed or file not found!'

@main_bp.route('/', methods=['GET'])
def index():
    return 'Backend Bisyarat'


app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True)
