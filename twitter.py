class Twitter(object):

    version = "2.4"

    def __init__(self):
        self.tweets = []

    def tweet (self, message):
        self.tweets.append(message)



