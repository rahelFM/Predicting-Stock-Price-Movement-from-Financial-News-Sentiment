import unittest
import pandas as pd
import sys
import os

# Add the root directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Now you can import from src
from src.sentiment import compute_sentiment

class TestSentiment(unittest.TestCase):

    def test_sentiment_score_range(self):
        df = pd.DataFrame({"headline": ["Great profits", "Bad losses", "Neutral news"]})
        result = compute_sentiment(df)
        self.assertTrue(result['sentiment_score'].between(-1, 1).all())

if __name__ == '__main__':
    unittest.main()
