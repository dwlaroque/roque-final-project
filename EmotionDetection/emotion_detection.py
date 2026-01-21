import requests
import json

def get_dominant_emotion(emotions):
    if not emotions:
        raise ValueError("Emotions dictionary is empty.")
    return max(emotions, key = emotions.get)

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = {"raw_document": { "text": text_to_analyze }}

    try:
        response = requests.post(url, json = obj, headers = headers)
    except Exception:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }
    
    #If Error 400 or blank input:
    if getattr(response, "status_code", None) == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }

    try:
        formatted_response = json.loads(response.text)
        prediction = formatted_response['emotionPredictions']
    
        # Access Main Emotion Score
        emotions = prediction[0]['emotion']

        # Access Individual Emotion Score
        anger_score = prediction[0]['emotion']['anger']
        disgust_score = prediction[0]['emotion']['disgust']
        fear_score = prediction[0]['emotion']['fear']
        joy_score = prediction[0]['emotion']['joy']
        sadness_score = prediction[0]['emotion']['sadness']
    
        #Modified Output Format
        emotions = {
            "anger": anger_score,
            "disgust": disgust_score,
            "fear": fear_score,
            "joy": joy_score,
            "sadness": sadness_score
        }
    
        dominant_emotion = max(emotions, key = emotions.get)
        emotions["dominant_emotion"] = dominant_emotion
        return emotions

    except Exception:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None
        }