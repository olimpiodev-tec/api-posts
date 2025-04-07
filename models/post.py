class Post:
    def __init__(self, post_id, author, title):
        self.post_id = post_id
        self.author = author
        self.title = title

    def to_json(self):
        return {
            "post_id": self.post_id,
            "author": self.author,
            "title": self.title
        }