from .base import Payment

class CashPayment(Payment):
    def pay(self, amount:float) -> str:
        return f"{amount} TL kapıda ödeme seçildi."
