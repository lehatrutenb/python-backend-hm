from models import user

def select_top_users_by_rate(users: list[user.User], top_size: int) -> list[user.User]:
    return sorted(users, key=lambda user: -user.rate)[:top_size] # .get_rate() ?
