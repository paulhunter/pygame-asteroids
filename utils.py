import random
from pygame import Vector2

class Utils:
    """Utils
    General utilities and helpers, a catch-all for shared code.
    """

    @staticmethod
    def random_vector2(length = 1):
        """random_vector2
        Create a uniformily random vector with axial values within the range
        [-length, length]
        """
        return Vector2(
            random.uniform(-length, length),
            random.uniform(-length, length)
        )
