from datetime import datetime
import uuid


class Comment:
    def __init__(self, author_id: uuid.UUID, text: str):
        self.author_id = author_id
        self.text = text
        self.create_data = datetime.now()
        self.update_data = self.create_data
        self.like_count = 0

    def edit_comment(self, new_text: str):
        self.text = new_text
        self.update_data = datetime.now()

    def like(self):
        self.like_count += 1

    def dislike(self):
        self.like_count -= 1

    def __repr__(self):
        return "author_id: {id}, create_data: {cd}, "\
                "update_data: {ud}, like_count: {lc}".format(id=self.author_id, cd=self.create_data,\
                                                            ud=self.update_data, lc=self.like_count)
