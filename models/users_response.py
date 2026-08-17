from datetime import date, datetime
from typing import List, Optional
from pydantic import BaseModel


class Address(BaseModel):
  street: Optional[str] = None
  house_number: Optional[str] = None
  city: Optional[str] = None
  state: Optional[str] = None
  country: Optional[str] = None
  postal_code: Optional[str] = None


class User(BaseModel):
  id: str
  provider: Optional[str] = None
  first_name: str
  last_name: str
  phone: Optional[str] = None
  dob: date
  email: str
  totp_enabled: bool
  created_at: datetime
  address: Address
  enabled: bool
  role: str
  failed_login_attempts: int


class UsersResponse(BaseModel):
  current_page: int
  data: List[User]