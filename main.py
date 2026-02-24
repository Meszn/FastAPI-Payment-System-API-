from fastapi import FastAPI, HTTPException
from models.payment_request import PaymentRequest
from services.payment_service import PaymentService
from payments.credit_card import CreditCard
from payments.paypal import PayPal
from payments.cash import CashPayment

app = FastAPI(title="Abstraction Payment API")

def get_payment_method(method: str):
    """
    Factory-like yapı.
    Soyutlama sayesinde kolayca genişletilebilir.
    """
    if method == "credit":
        return CreditCard()
    elif method == "paypal":
        return PayPal()
    elif method == "cash":
        return CashPayment()
    else:
        raise HTTPException(status_code=400, detail="Invalid payment method")

@app.post("/pay")
def make_payment(request: PaymentRequest):

    payment_method = get_payment_method(request.method)
    service = PaymentService(payment_method)

    result = service.process(request.amount)

    return {
        "status": "success",
        "message": result
    }