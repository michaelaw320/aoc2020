from dataclasses import dataclass

with open("../input/Day5/input") as f:
    lines = [line for line in f]


@dataclass
class Seat:
    row: int
    col: int
    id: int

    @classmethod
    def parse(cls, line: str):
        line = line.replace("F", "0")
        line = line.replace("B", "1")
        line = line.replace("L", "0")
        line = line.replace("R", "1")
        row = int(line[:7], 2)
        col = int(line[7:], 2)
        return cls(
            row=row,
            col=col,
            id=(row * 8 + col),
        )


seats = [Seat.parse(line) for line in lines]

sorted_seats = sorted(seats, key=lambda x: x.id, reverse=False)

min_id = sorted_seats[0].id
max_id = sorted_seats[-1].id
ids = {seat.id for seat in sorted_seats}
all_ids = {i for i in range(min_id, max_id)}

print(f"Missing ID: {all_ids - ids}")
