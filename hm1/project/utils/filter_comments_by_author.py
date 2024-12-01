from models import comment,user

def filter_comments_by_author(comments: list[comment.Comment], author: user.User) -> list[comment.Comment]:
    return list(filter(lambda comm: comm.author_id==author.id, comments)) # comm.get_author_id()?
