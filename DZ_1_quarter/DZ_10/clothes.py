from abc import ABC, abstractmethod


class clothes(ABC):
    def __init__(self, args):
        self.args = args

    @abstractmethod
    def sum_clothes(self):
        pass


class coat(clothes):

    @property
    def sum_clothes(self):
        return self.args / 6.5 + 0.5


class suit(clothes):

    @property
    def sum_clothes(self):
        return self.args * 2 + 0.3


palto = coat(56)
kostum = suit(33)

print(palto.sum_clothes)
print(kostum.sum_clothes)