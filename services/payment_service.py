from payments.base import Payment

class PaymentService:
    """
    Service katmanı soyut sınıfa bağımlı.
    Concrete sınıfa değil. Yani temel sınıfa değil.
    """

    def __init__(self, payment: Payment):
        self.payment = payment

    def process(self, amount:float):
        return self.payment.pay(amount)
