from abc import ABC, abstractproperty


class IShape(ABC):
    @abstractproperty
    def area():
        pass
