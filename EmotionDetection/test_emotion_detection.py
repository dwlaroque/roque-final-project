import unittest
from emotion_detection import emotion_detector

class TestDominantEmotion(unittest.TestCase):
    
    def test_dominant_emotions(self):
        test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]

        for text, expected in test_cases:
            with self.subTest(text=text, expected=expected):
                result = emotion_detector(text)
                self.assertIsInstance(result, dict, "emotion_detector should return a dict")
                self.assertIn("dominant_emotion", result, "Result must include 'dominant_emotion'")
                self.assertEqual(
                    result["dominant_emotion"], expected,
                    f"Text: {text!r} → Expected {expected!r} but got {result['dominant_emotion']!r}"
                )


if __name__ == "__main__":
    unittest.main()
