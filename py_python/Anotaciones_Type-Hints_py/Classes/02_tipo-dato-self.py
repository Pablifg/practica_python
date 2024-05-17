#self: Métodos de clase retorna objetos del mismo tipo de la clase.
## misma clase u objeto nueva pero de misma clase

# Self -> +3.11 python
from typing import Self


class User:

    def __init__(self, username: str, email: str) -> None:
        self.username: str = username
        self.email: str = email


    def copy(self) -> Self:
        return User(self.username, self.email)

    
    def get_user(self) -> Self:
        return self


    def __str__(self) -> str:
        return f'{self.username} - {self.email}'


# Instanciar objeto
cody = User('Layla', 'layla@info.com')
cody_copy = cody.copy()
cody_get = cody.get_user()
print(cody)
print(cody_copy)
print(id(cody))
print(id(cody_get))
