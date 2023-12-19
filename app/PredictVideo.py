import tensorflow as tf
import os
import cv2
import numpy as np
from sklearn.metrics import accuracy_score

class PredictVideo():
    MODEL_PATH = 'model.h5'
    TEMP_VIDEO_PATH = 'temp_video/'
    TEMP_IMAGES_PATH = 'temp_images'

    def __init__(self,video):
        model = self.load_model(self.MODEL_PATH)
        video_path = self.save_temp_video(video)
        frame_images_path = self.extract_frame(video_path)
        
        predictions = []
        labels = []
        
        for frame in os.listdir(frame_images_path):
            frame_path = os.path.join(frame_images_path,frame)
            
            image = cv2.imread(frame_path)
            image = cv2.resize(image, (224,224))
            
            img = image / 255
            
            img = np.expand_dims(img, axis=0)
            
            predicted_image = model.predict(img)
            
            predicted_class = np.argmax(predicted_image)
            
            true_label = (frame.split('_')[0])
            
            labels.append(true_label)
            predictions.append(predicted_class)
        
        accuracy = accuracy_score(predictions , labels)
        
        return accuracy
    
    def save_temp_video(self,video):
        video_path = self.TEMP_VIDEO_PATH + video.filename
        if not video.save(video_path):
            return False
        return video_path
    
    def extract_frame(self,video_path):
        filename = video_path.filename
        images_path = os.path.join(self.TEMP_IMAGES_PATH, filename)
        img_filename = filename.split('_')[0]
        
        try:
            if os.path.exists(images_path):
                os.makedirs(images_path)
            
            cap = cv2.VideoCapture(video_path)
            
            if not cap.isOpened():
                raise Exception("Gagal membuka video.")
            
            frame_count = 1
            while True:
                ret,frame = cap.read()
                
                if not ret:
                    break
                
                frame_filename = os.path.join(images_path, f"{img_filename}_{frame_count:04d}.jpg")
                cv2.imwrite(frame_filename, frame)
            
            cap.release()
            
            return images_path
        except Exception as e:
                print(f"Terjadi kesalahan: {e}")
    
        def load_model(self,model_path):
            model = tf.keras.models.load_model(model_path)
            return model

