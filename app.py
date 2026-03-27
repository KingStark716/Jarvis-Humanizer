import os
import google.generativeai as genai
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Aapki provide ki hui API Key
genai.configure(api_key="AIzaSyCsahJbwZS0rAkGZ2birqpE5tuVlCzbAFI")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/humanize', methods=['POST'])
def humanize():
    try:
        data = request.json
        user_text = data.get('text', '')

        if not user_text:
            return jsonify({'error': 'Please provide some text!'}), 400

        # 2026 ka sab se stable aur fast model
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        prompt = f"Act as a professional writer. Rewrite the following text to make it sound 100% human, conversational, and bypass AI detectors. Keep the original meaning:\n\n{user_text}"
        
        response = model.generate_content(prompt)
        
        return jsonify({'humanized': response.text})
    
    except Exception as e:
        # Is se humein pata chale ga ke exact masla kya hai
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
