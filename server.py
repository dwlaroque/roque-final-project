"""
Flask server for the emotion detector web application.
Handles user input and returns emotion analysis.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    """Render Main HTML page for user interface"""
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET"])
def emotion_detection():
    """
    Accept user text through GET, call emotion_detector(),
    handle invalid input, and return formatted output.
    """
    text_to_analyze = request.args.get("textToAnalyze", "")
    emotions = emotion_detector(text_to_analyze)

    if emotions.get("dominant_emotion") is None:
        return "Invalid text! Please try again."

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, "
        f"'fear': {emotions['fear']}, "
        f"'joy': {emotions['joy']}, "
        f"'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {emotions['dominant_emotion']}."
    )

    return response_text

if __name__ == "__main__":
    app.run(host = "localhost", port = 5002, debug = True)
