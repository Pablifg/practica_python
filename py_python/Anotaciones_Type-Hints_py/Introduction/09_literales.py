# LITERALES -> podemos verlos como enums
# Definir listado de posibles opciones que puede ser la variable. Limitamos opciones que puede ser la variable
# A partir de +3.11 python
from typing import Literal

def set_background_color(color: Literal['red', 'green', 'blue', 'white', 'black']):
    pass


def make_user(username:str, email:str, gender: Literal['M', 'F']):
    pass


def open_handler(file: str, mode: Literal['r', 'rb', 'w', 'wb']):
    pass
    
