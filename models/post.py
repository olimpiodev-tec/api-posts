class Post:
    def __init__(self, post_id, author, title, photo_path):
        self.post_id = post_id
        self.author = author
        self.title = title
        self.photo_path = photo_path

    def to_json(self):
        return {
            'post_id': self.post_id,
            'author': self.author,
            'title': self.title,
            'photo_path': self.photo_path
        }
