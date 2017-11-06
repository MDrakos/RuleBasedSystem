"""Provides an object to store each answer a user gives.

Each answer has a topic and content that can be both set and retrieved.
"""

__author__ = 'Mike'
__version__ = '1.0'


class Answer:
    def __init__(self, topic="", content=""):
        """
        Creates a new answer object

        :param topic: string of topic
        :param content: string of answer value
        """
        self.topic = topic
        self.content = content

    def set_topic(self, topic):
        """
        Sets topic of answer

        :param topic: string of topic
        """
        self.topic = topic

    def set_content(self, content):
        """
        Sets content of answer

        :param content: string of content
        """
        self.content = content

    def get_topic(self):
        """
        Returns the topic

        :return: topic string
        """
        return self.topic

    def get_content(self):
        """
        Returns the content of an answer

        :return: content string
        """
        return self.content
