from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    A class to represent a King, inherits to class Baratheon and lannister.
    """
    def __init__(self, name, alive=True):
        """
        init function
        """
        super().__init__(name, alive=alive)

    def die(self):
        """
        dead function
        """
        self.is_alive = False

    def get_eyes(self) -> str:
        '''eye getter'''
        return self.eyes

    def get_hairs(self) -> str:
        '''hairs getter'''
        return self.hairs

    def set_eyes(self, color):
        '''eyes setter'''
        self.eyes = color

    def set_hairs(self, color):
        '''hairs setter'''
        self.hairs = color
