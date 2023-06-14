class calculator:

    def __init__(self, nlist):
        """
        init function
        """
        assert all(isinstance(n, float) for n in nlist), "not a float list"
        self.lst = nlist

    def __add__(self, object) -> None:
        '''doc +'''
        self.lst = [i + object for i in self.lst]
        print(self.lst)

    def __mul__(self, object) -> None:
        '''doc *'''
        self.lst = [i * object for i in self.lst]
        print(self.lst)

    def __sub__(self, object) -> None:
        '''doc -'''
        self.lst = [i - object for i in self.lst]
        print(self.lst)

    def __truediv__(self, object) -> None:
        '''doc /'''
        assert object != 0, "can t devide by 0"
        self.lst = [i / object for i in self.lst]
        print(self.lst)
