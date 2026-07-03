from datetime import date

from app.models.coupon import Coupon


def apply_coupon_discount(amount: float, coupon: Coupon | None, today: date) -> float:
    if coupon is None:
        return amount

    if coupon.is_expired(today):
        return amount

    final_amount = amount - coupon.discount_amount
    return max(final_amount, 0)
