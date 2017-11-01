"""Provides an object to store each answer a user gives.

Each answer has a topic and content that can be both set and retrieved.
"""

__author__ = 'Mike'
__version__ = '1.0'


class Answer:
    def __init__(self, topic="", content=""):
        self.topic = topic
        self.content = content

    def set_topic(self, topic):
        self.topic = topic

    def set_content(self, content):
        self.content = content

    def get_topic(self):
        return self.topic

    def get_content(self):
        return self.content
