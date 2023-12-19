from flask import Blueprint, request
from PredictVideo import PredictVideo
main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def home():
    print()
    # return render_template('home.html')

@main_bp.route('/upload_video', methods=['POST'])
def upload_video():
    if 'video' not in request.files:
        return False
    
    video_file = request.files['video']
    result = PredictVideo(video_file)
    return result