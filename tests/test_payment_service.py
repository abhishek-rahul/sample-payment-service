from datetime import date

import pytest

from app.models.coupon import Coupon
from app.services.payment_service import calculate_final_amount


def test_calculate_final_amount_without_coupon():
    final_amount = calculate_final_amount(amount=1200, today=date(2026, 1, 1))

    assert final_amount == 1200


def test_calculate_final_amount_with_valid_coupon():
    coupon = Coupon(code="SAVE200", discount_amount=200, expires_at=date(2026, 12, 31))

    final_amount = calculate_final_amount(amount=1200, coupon=coupon, today=date(2026, 1, 1))

    assert final_amount == 1000


def test_calculate_final_amount_rejects_zero_amount():
    with pytest.raises(ValueError, match="Amount must be greater than zero"):
        calculate_final_amount(amount=0, today=date(2026, 1, 1))


def test_calculate_final_amount_rejects_negative_amount():
    with pytest.raises(ValueError, match="Amount must be greater than zero"):
        calculate_final_amount(amount=-10, today=date(2026, 1, 1))
