from models import comment

def get_ordered_comments_by_likes(comments: list[comment.Comment]) -> list[comment.Comment]:
    return sorted(comments, key=lambda comment: -comment.like_count) # .get_like_count()?
