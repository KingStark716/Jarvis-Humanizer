import os
import google.generativeai as genai
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Yahan apni asli API Key paste karein (Ya Vercel Environment Variable use karein)
GEMINI_API_KEY = "AIzaSyCsahJbwZS0rAkGZ2birqpE5tuVlCzbAFI"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('models/gemini-1.5-flash')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/v1/humanize', methods=['POST'])
def humanize_text():
    # Security Check jo humne pehle lagaya tha
    api_key = request.args.get('api_key')
    if api_key != "STARK_99":
        return jsonify({"error": "Unauthorized Access"}), 403

    data = request.get_json()
    original_text = data.get("text", "")

    try:
        # Asli AI Magic: Gemini ko instruction dena ke text humanize kare
        prompt = f"Rewrite the following text to make it sound 100% human, natural, and conversational. Ensure it bypasses AI detection but keeps the original meaning: {original_text}"
        response = model.generate_content(prompt)
        humanized_text = response.text
        
        return jsonify({
            "status": "Success",
            "original": original_text,
            "humanized": humanized_text,
            "ai_score": "0% (Pure Human)"
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

app = app

if __name__ == '__main__':
    app.run(debug=True)
