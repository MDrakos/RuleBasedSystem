class Answer:
    def __init__(self, topic, content):
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
