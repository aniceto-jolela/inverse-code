"""This method returns personalized error message"""


class NonNumber(TypeError):
    """NOTE: Expect a TypeError for non-numeric inputs"""

    def __init__(self):
        super().__init__("Only Integer numbers is allowed.")
