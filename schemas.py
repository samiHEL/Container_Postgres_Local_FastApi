import datetime as _dt
import pydantic as _pydantic

class _BaseContact(_pydantic.BaseModel):
    first_name: str

class Contact(_BaseContact):
    id: int

    class Config:
        orm_mode = True
class CreateContact(_BaseContact):
    pass