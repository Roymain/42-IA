class calculator:

    def __init__(self, nlist):
        """
        init function
        """
        assert all(isinstance(n, float) for n in nlist), "not a float list"
        self.lst = nlist

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        '''doc *'''
        res = []
        res = sum([i * j for i, j in zip(V1, V2)])
        print(res)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        '''doc +'''
        res = []
        res = [float(i + j) for i, j in zip(V1, V2)]
        print(res)

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        '''doc -'''
        res = []
        res = [float(i - j) for i, j in zip(V1, V2)]
        print(res)
