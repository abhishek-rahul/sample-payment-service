from datetime import date

from app.models.coupon import Coupon
from app.services.discount_policy import apply_coupon_discount
from app.services.payment_validator import validate_amount


def calculate_final_amount(
    amount: float,
    coupon: Coupon | None = None,
    today: date | None = None,
) -> float:
    validate_amount(amount)

    current_date = today or date.today()
    return apply_coupon_discount(amount, coupon, current_date)
