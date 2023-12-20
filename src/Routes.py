from flask import request
from . import main_bp
from .PredictVideo import PredictVideo

@main_bp.route('/upload_video', methods=['POST'])
def upload_video():
    file = request.files['video']
    if file:
        predict_video_instance = PredictVideo()
        score_predicted_vid = predict_video_instance.predict_video(file)
        return score_predicted_vid
    return 'Gagal memprediksi Video'
