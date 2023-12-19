from flask import request
from . import PredictVideo, main_bp


@main_bp.route('/')
def home():
    print("unch")
    return "unch"
    # return render_template('home.html')


@main_bp.route('/upload_video', methods=['POST'])
def upload_video():
    # if 'video' not in request.files:
    #     return False

    # video_file = request.files['video']
    # result = PredictVideo(video_file)
    # return result

    file = request.files['video']
    # If the user does not select a file, the browser submits an

    if file:
        # file.save('contoh' + '/' + file.filename)
        PredictVideo(file)
        return 'File uploaded successfully'

    return 'Gagal'
