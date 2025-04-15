from transformers import pipeline

# Load the emotion detection pipeline
emotion_pipeline = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=None)

def emotion_detector(text_to_analyze):
    """
    Function to detect emotions in the given text using a Hugging Face pre-trained model.

    Args:
        text_to_analyze (str): The text to analyze for emotions.

    Returns:
        list: A list of dictionaries containing the detected emotions and their scores.
    """
    try:
        # Use the emotion pipeline to analyze the text
        results = emotion_pipeline(text_to_analyze)

        # Flatten the results if they are nested
        if isinstance(results, list) and len(results) > 0 and isinstance(results[0], list):
            results = results[0]

        return results

    except Exception as e:
        print(f"Error in emotion_detector: {e}")
        raise
