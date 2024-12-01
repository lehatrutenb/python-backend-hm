import uuid


class User:
    def __init__(self, name:str):
        self.id = uuid.uuid4()
        self.name = name
        self.comments_count = 0
        self.rate = 0
        self.is_banned = False

    def edit_name(self, new_name: str):
        self.name=new_name

    def increment_rate(self):
        self.rate += 1

    def ban_user(self):
        self.is_banned=True

    def unban_user(self):
        self.is_banned=False

    def __repr__(self):
        return "name: {nm}, author_id: {id}, "\
                "rate: {rt}, is_banned: {ib}, comments_count: {cc}"\
                    .format(nm=self.name, id=self.id, 
                            rt=self.rate, ib= self.is_banned, cc=self.comments_count)
