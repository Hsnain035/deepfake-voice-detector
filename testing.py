import unittest
from model import extract_features

class TestAudio(unittest.TestCase):

    def test_feature_extraction(self):

        features = extract_features("sample.wav")

        self.assertEqual(len(features), 40)

if __name__ == "__main__":
    unittest.main()