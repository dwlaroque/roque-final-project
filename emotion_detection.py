import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    obj = {"raw_document": { "text": text_to_analyze }}
    response = requests.post(url, json = obj, headers = headers)
    formatted_response = json.loads(response.text)
    return formatted_response