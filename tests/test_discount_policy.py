from datetime import date

from app.models.coupon import Coupon
from app.services.discount_policy import apply_coupon_discount


def test_no_coupon_returns_same_amount():
    final_amount = apply_coupon_discount(amount=1000, coupon=None, today=date(2026, 1, 1))

    assert final_amount == 1000


def test_valid_coupon_applies_discount():
    coupon = Coupon(code="SAVE100", discount_amount=100, expires_at=date(2026, 12, 31))

    final_amount = apply_coupon_discount(amount=1000, coupon=coupon, today=date(2026, 1, 1))

    assert final_amount == 900


def test_expired_coupon_does_not_apply_discount():
    coupon = Coupon(code="OLD100", discount_amount=100, expires_at=date(2025, 12, 31))

    final_amount = apply_coupon_discount(amount=1000, coupon=coupon, today=date(2026, 1, 1))

    assert final_amount == 1000


def test_discount_cannot_make_amount_negative():
    coupon = Coupon(code="BIG500", discount_amount=500, expires_at=date(2026, 12, 31))

    final_amount = apply_coupon_discount(amount=100, coupon=coupon, today=date(2026, 1, 1))

    assert final_amount == 0
