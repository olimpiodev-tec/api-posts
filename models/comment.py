class Comment:
    def __init__(self, comment_id, post_id, description):
        self.comment_id = comment_id
        self.post_id = post_id
        self.description = description

    def to_json(self):
        return {
            'comment_id': self.comment_id,
            'post_id': self.post_id,
            'description': self.description
        }