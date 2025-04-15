# Emotion Detection Web Application

This repository contains a Flask-based web application for detecting emotions in text using a pre-trained NLP model. The application leverages Hugging Face's `transformers` library to analyze text and identify emotions such as joy, anger, sadness, fear, and more.

---

## Features

- **Emotion Detection**: Analyze user-provided text and detect the dominant emotions.
- **Interactive Web Interface**: A user-friendly interface built with HTML, CSS, and JavaScript.
- **Pre-trained Model**: Uses the `j-hartmann/emotion-english-distilroberta-base` model from Hugging Face.
- **Responsive Design**: Optimized for both desktop and mobile devices.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/emotion-detection.git
   cd emotion-detection
   ```
2. Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

3. Install the required dependencies:
pip install -r requirements.txt

4. Download the pre-trained model: The application will automatically download the j-hartmann/emotion-english-distilroberta-base model when you run it for the first time.

## Usage
1. Start the Flask server:
python server.py

2. Open your browser and navigate to:
http://127.0.0.1:5000/

3. Enter text in the input field and click "Run Sentiment Analysis" to detect emotions.

## File Structure:
``` bash
Emotion Detection/
│
├── templates/
│   └── index.html          # HTML file for the web interface
│
├── static/
│   └── mywebscript.js      # JavaScript file for handling user interactions
│
├── [emotion_detection.py]      # Contains the emotion detection logic
├── [server.py]                 # Flask server implementation
├── [test_emotion_detection.py] # Unit tests for the emotion detection function
├── requirements.txt            # Python dependencies
└── [README.md]                 # Project documentation
```

## Technologies Used
- Backend: Flask (Python)
- Frontend: HTML, CSS, JavaScript
- NLP Model: Hugging Face transformers
- Styling: Custom CSS with responsive design

## Testing
Run the unit tests to ensure the application works as expected:
python -m unittest [test_emotion_detection.py]

## Future Enhancements
- Add support for multiple languages.
- Provide a detailed breakdown of emotion scores.
- Integrate with a database to store analysis history.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments
- Hugging Face for providing the pre-trained NLP model.
- Flask for the lightweight web framework.
- Bootstrap for responsive design inspiration.