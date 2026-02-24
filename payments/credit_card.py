from .base import Payment

class CreditCard(Payment):

    def pay(self,amount:float) -> str:
        return f"{amount} TL Kredi kartı ile ödendi."
