
from pydantic import BaseModel, Field


class FlightInput(BaseModel):
    Origin: str
    Dest: str

    CRSElapsedTime: float = Field(gt=0)
    Distance: float = Field(gt=0)

    OriginState: str
    DestState: str

    DepTimeBlk: str
    ArrTimeBlk: str

    DayofMonth: int = Field(ge=1, le=31)

    Month_sin: float
    Month_cos: float

    DayOfWeek_sin: float
    DayOfWeek_cos: float

    ArrTime_sin: float
    ArrTime_cos: float
