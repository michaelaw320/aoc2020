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

sorted_seats = sorted(seats, key=lambda x: x.id, reverse=True)

print(f"Seat with highest id: {sorted_seats[0]}")
