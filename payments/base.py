from abc import ABC, abstractmethod

class Payment(ABC):
    """
    Bu sınıf soyut ödeme sınıfımız.
    Tüm ödeme Yöntemleri bu sınıftan türemelidir.

    """

    @abstractmethod
    def pay(self,amount:float) -> str:
        pass
