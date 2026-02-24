from .base import Payment

class PayPal(Payment):

    def pay(self, amount: float) -> str:
        return f"{amount} TL PayPal ile ödendi."
