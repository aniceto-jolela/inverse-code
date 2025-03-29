"""This method returns personalized error message"""


class NonNumber(TypeError):
    """NOTE: Expect a TypeError for non-numeric inputs"""

    def __init__(self):
        super().__init__("Only Integer numbers is allowed.")


class NonNegativeNumber(ValueError):
    """NOTE: Permitted values are higher than 0."""

    def __init__(self):
        super().__init__("Permitted values are higher than 0.")


class ExceededIndexNumber(IndexError):
    """NOTE: List index out of range"""

    def __init__(self):
        super().__init__("The index number has to be the same as the list [x]==[y].")
