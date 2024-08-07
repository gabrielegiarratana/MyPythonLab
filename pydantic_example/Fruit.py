from typing import Annotated, Dict, List, Literal, Tuple

from annotated_types import Gt

from pydantic_example import BaseModel


class Fruit(BaseModel):
    name: str
    color: Literal["red", "green"]
    weight: Annotated[float, Gt(0)]
    bazam: Dict[str, List[Tuple[int, bool, float]]]


if __name__ == "__main__":
    print(
        Fruit(
            name="Apple",
            color="red",
            weight=4.2,
            bazam={"foobar": [(1, True, 0.1)]},
        )
    )
    # > name='Apple' color='red' weight=4.2 bazam={'foobar': [(1, True, 0.1)]}
