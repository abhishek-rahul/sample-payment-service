from datetime import date

from app.models.coupon import Coupon
from app.services.payment_service import calculate_final_amount


if __name__ == "__main__":
    coupon = Coupon(code="WELCOME100", discount_amount=100, expires_at=date(2099, 1, 1))
    amount = calculate_final_amount(amount=1000, coupon=coupon, today=date.today())
    print(f"Final amount: {amount}")
