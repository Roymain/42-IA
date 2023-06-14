from abc import ABC, abstractmethod


class Character(ABC):
    """
    A class to represent a person.
    """

    def __init__(self, name, alive=True):
        """
        init function
        """
        assert type(name) == str, "name not avalaible"
        self.first_name = name
        self.is_alive = alive

    @abstractmethod
    def die(self):
        """
        dead function
        """
        self._is_alive = False


class Stark(Character):
    """
    A class to represent a stark, inherits to class character.
    """
    def __init__(self, name, alive=True):
        """
        init function
        """
        super().__init__(name, alive)

    def die(self):
        """
        dead function
        """
        self.is_alive = False
