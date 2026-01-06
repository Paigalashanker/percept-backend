from flask import Flask, request, jsonify
import requests

app = Flask(__name__)


API_KEY = "###########"


AI_API_URL = "https://api.example-ai.com/analyze"

@app.route("/analyze", methods=["POST"])
def analyze_emotion():
    data = request.json
    text = data.get("text", "")

    



    text_lower = text.lower()

    if "excited" in text_lower or "happy" in text_lower or "love" in text_lower:
        emotion = "Happy 💖✨"
    elif "sad" in text_lower or "cry" in text_lower:
        emotion = "Sad 💧🌧️"
    elif "angry" in text_lower or "hate" in text_lower:
        emotion = "Angry 🔥⚡"
    else:
        emotion = "Neutral 🌿⚪"

    return jsonify({
        "input_text": text,
        "emotion": emotion
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
