# <variable>: <clase> = ...

class User:

    def __init__(self, username:str, email:str) -> None:
        self.username: str = username
        self.email: str = email


def make_user(username: str, email:str) -> User:
    return User(username, email)


cody: User = make_user('Layla', 'layla@example.com') # cody instancia de clase User
print(cody.username)
print(cody.email)
