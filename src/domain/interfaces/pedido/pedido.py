from dataclasses import dataclass
from dataclasses_json import dataclass_json, LetterCase


# Documentation: https://docs.python.org/3/library/dataclasses.html#dataclasses.dataclass
@dataclass_json(letter_case=LetterCase.CAMEL)
@dataclass(init=True)
class Pedido:
    id: int
    title: str
