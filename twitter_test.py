import unittest

from SimpleUnitTest.twitter import Twitter


class TwitterTest(unittest.TestCase):

    def setUp(self):
        self.twitter = Twitter()

    def test_initial(self):
        self.assertTrue(self.twitter)

    def test_single_tweet(self):
        self.twitter.tweet('Test message')

        self.assertEqual(self.twitter.tweets, ['Test message'])


if __name__ == '__main__':
    unittest.main()