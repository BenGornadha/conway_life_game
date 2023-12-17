import dataclasses


@dataclasses.dataclass(frozen=True)
class Dimension:
    number_of_row: int
    num_of_columns: int
