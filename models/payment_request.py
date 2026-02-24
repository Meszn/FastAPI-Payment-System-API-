from pydantic import BaseModel

class PaymentRequest(BaseModel):
    amount: float
    method: str
