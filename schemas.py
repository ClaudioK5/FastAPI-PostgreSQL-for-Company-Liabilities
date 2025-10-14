from pydantic import BaseModel


class LiabilityItemCreate(BaseModel):

    name: str
    amount: float
    due_date: str
    category: str
    is_paid: bool = False

class LiabilityItem(BaseModel):

    id: int
    name: str
    amount: float
    due_date: str
    category: str
    is_paid: bool = False

    class Config:

        orm_mode = True