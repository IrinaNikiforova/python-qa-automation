from datetime import date, datetime

from pydantic import BaseModel


class Address(BaseModel):
    street: str
    house_number: str | None
    city: str
    state: str | None
    country: str
    postal_code: str | None


class UserMeResponse(BaseModel):
    id: str
    provider: str | None
    first_name: str
    last_name: str
    phone: str | None
    dob: date
    email: str
    totp_enabled: bool
    created_at: datetime
    address: Address