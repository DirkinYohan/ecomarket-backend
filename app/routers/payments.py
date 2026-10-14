import stripe
from fastapi import APIRouter, HTTPException

stripe.api_key = "sk_test_51NX..."

router = APIRouter(prefix="/api/v1/payments", tags=["Payments"])


@router.post("/create-intent")
async def create_payment_intent(amount: int, currency: str = "usd"):
  # --- FIX APLICADO PARA EL BUG ECO-101-B1 ---
  if amount <= 0:
    raise HTTPException(
        status_code=400,
        detail="El monto debe ser un entero positivo superior a 0.",
    )
  # -------------------------------------------

  try:
    intent = stripe.PaymentIntent.create(
        amount=amount,
        currency=currency,
        metadata={"integration": "ECO-101"},
    )
    return {"client_secret": intent.client_secret, "id": intent.id}
  except Exception as e:
    raise HTTPException(status_code=400, detail=str(e))