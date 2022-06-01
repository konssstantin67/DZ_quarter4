class road:

    def __init__(self, lenght, width, massa_2m, thickness):
        self._lenght, self._width, self._massa_2m, self.thickness = massa_2m / 1000, thickness, lenght, width

    def bitumen(self):
        return self._lenght * self._width * self._massa_2m * self.thickness

calc = road(33,1234,43,21)
print(calc.bitumen())