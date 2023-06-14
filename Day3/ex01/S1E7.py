from S1E9 import Character


class Baratheon(Character):
    """
    A class to represent a Baratheo, inherits from class character.
    """
    def __init__(self, name, alive=True):
        """
        init function
        """
        super().__init__(name, alive=alive)
        self.family_name = "Barathon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """
        dead function
        """
        self.is_alive = False

    def __str__(self):
        '''doc'''
        return "Vector: ('%s', '%s', '%s')" \
            % (self.family_name, self.eyes, self.hairs)

    def __repr__(self):
        '''doc'''
        return "Vector: ('%s', '%s', '%s')" \
            % (self.family_name, self.eyes, self.hairs)


class Lannister(Character):

    def __init__(self, name, alive=True):
        """
        init function
        """
        super().__init__(name, alive=alive)
        self.family_name = "Lannister"
        self.eyes = "Blue"
        self.hairs = "light"

    def die(self):
        """
        dead function
        """
        self.is_alive = False

    def __str__(self):
        '''doc'''
        return "Vector: ('%s', '%s', '%s')" \
            % (self.family_name, self.eyes, self.hairs)

    def __repr__(self):
        '''doc'''
        return "Vector: ('%s', '%s', '%s')" \
            % (self.family_name, self.eyes, self.hairs)

    @classmethod
    def create_lannister(cls, name, alive):
        '''create a lannister'''
        return cls(name, alive)
