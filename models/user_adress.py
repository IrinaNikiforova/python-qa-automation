from datetime import date, datetime

from pydantic import BaseModel


class Address(BaseModel):
    street: str
    house_number: str | None
    city: str
    state: str | None
    country: str
    postal_code: str | None