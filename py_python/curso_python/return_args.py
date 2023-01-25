# -*- coding: utf-8 -*-

def find_volume(length=1, width=1, depth=1):
    """
    Find the volumen of a cube

    Args:
    length -- length in centimeters (default 1)
    width -- width in centimeters (default 1)
    depth -- depth in centimeters (default 1)

    Return:
    length * width * depth -- volumen
    """
    return length * width * depth

result = find_volume(width=10)
print(result)
