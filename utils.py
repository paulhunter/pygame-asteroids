import random
from pygame import Vector2

class Utils:

    @staticmethod
    def random_vector2(length = 1):
        return Vector2(
            random.uniform(0, length),
            random.uniform(0, length)
        )