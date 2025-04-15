import unittest
from emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotions(self):
        # Test cases: input text and expected dominant emotion
        test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]

        for text, expected_emotion in test_cases:
            with self.subTest(text=text):
                # Call the emotion_detector function
                results = emotion_detector(text)

                # Find the dominant emotion (highest score)
                dominant_emotion = max(results, key=lambda x: x["score"])["label"]

                # Assert that the dominant emotion matches the expected emotion
                self.assertEqual(dominant_emotion, expected_emotion)

if __name__ == "__main__":
    unittest.main()