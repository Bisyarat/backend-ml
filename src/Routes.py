from flask import request ,jsonify
from . import main_bp
from .PredictVideo import PredictVideo

@main_bp.route('/upload_video', methods=['POST'])
def upload_video():
    file = request.files['video']
    if file:
        try:
            predict_video_instance = PredictVideo()
            predicted_vid = predict_video_instance.predict_video(file)
            response_data = {'message': 'File berhasil diunggah ke GCS', 'gcs_path': predicted_vid}
            return jsonify(response_data)
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found")
        except Exception as e:
            raise Exception(f"Error : {e}")
    return 'Gagal memprediksi Video'
