from dataclasses import dataclass
from datetime import date


@dataclass
class Coupon:
    code: str
    discount_amount: float
    expires_at: date

    def is_expired(self, today: date) -> bool:
        return today > self.expires_at
