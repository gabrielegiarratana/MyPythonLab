from datetime import datetime
from typing import Tuple

from pydantic_example import BaseModel


class Delivery(BaseModel):
    timestamp: datetime
    dimensions: Tuple[int, int]


if __name__ == "__main__":
    m = Delivery(timestamp="2020-01-02T03:04:05Z", dimensions=["10", "20"])
    print(repr(m.timestamp))
    # > datetime.datetime(2020, 1, 2, 3, 4, 5, tzinfo=TzInfo(UTC))
    print(m.dimensions)
    # > (10, 20)
