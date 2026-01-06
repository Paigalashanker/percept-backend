from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

API_KEY = os.environ.get("GROQ_API_KEY")

@app.route("/analyze", methods=["POST"])
def analyze_emotion():
    data = request.json
    text = data.get("text", "").lower()

    if any(word in text for word in ["love", "care", "miss", "crush"]):
        emotion = "Love ❤️🌸"
    elif any(word in text for word in ["excited", "thrilled", "can't wait"]):
        emotion = "Excited 🌟🔥"
    elif any(word in text for word in ["happy", "joy", "smile"]):
        emotion = "Happy 💖✨"
    elif any(word in text for word in ["sad", "cry", "lonely", "down"]):
        emotion = "Sad 💧🌧️"
    elif any(word in text for word in ["angry", "hate", "mad", "furious"]):
        emotion = "Angry 🔥⚡"
    elif any(word in text for word in ["fear", "scared", "afraid", "nervous"]):
        emotion = "Fear 😨⚠️"
    elif any(word in text for word in ["surprise", "shocked", "wow"]):
        emotion = "Surprise 😲✨"
    elif any(word in text for word in ["disgust", "gross", "dirty"]):
        emotion = "Disgust 🤢🚫"
    else:
        emotion = "Neutral 🌿⚪"

    return jsonify({
        "input_text": text,
        "emotion": emotion
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
