from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/v1/humanize', methods=['POST'])
def humanize_text():
    api_key = request.args.get('api_key')
    data = request.get_json()
    
    # Security Check
    if api_key != "STARK_99":
        return jsonify({"error": "Payment Required"}), 403

    original_text = data.get("text", "")
    
    # AI Logic (Yahan hum text ko change karenge)
    # Abhi ke liye hum sirf ek simple example dikha rahe hain
    humanized_text = original_text.replace("is", "definitely is").replace("very", "extremely")
    
    return jsonify({
        "status": "Success",
        "original": original_text,
        "humanized": humanized_text,
        "ai_score": "0% (Pure Human)"
    })

if __name__ == '__main__':
    app.run(debug=True)