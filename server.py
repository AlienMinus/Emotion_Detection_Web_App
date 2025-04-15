from flask import Flask, request, jsonify, render_template
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/detect_emotion', methods=['POST'])
def detect_emotion():
    """
    Endpoint to detect emotions in the provided text.
    """
    try:
        data = request.get_json()
        text_to_analyze = data.get('text', '')

        if not text_to_analyze:
            return jsonify({"error": "No text provided"}), 400

        # Call the emotion_detector function
        results = emotion_detector(text_to_analyze)

        # Flatten the response to return a list of emotions with their scores
        if isinstance(results, list) and len(results) > 0 and isinstance(results[0], list):
            results = results[0]  # Extract the inner list if it's nested

        formatted_results = [{"label": res["label"], "score": res["score"]} for res in results]

        # Return the formatted results as JSON
        return jsonify(formatted_results)

    except Exception as e:
        # Log the error for debugging
        print(f"Error: {e}")
        return jsonify({"error": "An internal server error occurred"}), 500

# Error handler for 404 (Not Found)
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "The requested resource was not found"}), 404

# Error handler for 400 (Bad Request)
@app.errorhandler(400)
def bad_request_error(error):
    return jsonify({"error": "Bad request"}), 400

# Error handler for 500 (Internal Server Error)
@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "An internal server error occurred"}), 500

if __name__ == '__main__':
    app.run(debug=True)