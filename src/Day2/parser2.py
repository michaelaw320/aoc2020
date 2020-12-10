import re

from dataclasses import dataclass

with open("../input/Day2/input") as f:
    lines = [line for line in f]

input_pattern = re.compile("(\d+)-(\d+) (.): (.*)")


@dataclass
class Password:
    pos_a: int
    pos_b: int
    letter: str
    password: str

    @classmethod
    def parse(cls, item: str):
        match = input_pattern.split(item)
        return cls(int(match[1]), int(match[2]), str(match[3]), str(match[4]))

    def is_valid(self) -> bool:
        is_valid_pos_a = self.password[self.pos_a-1] == self.letter
        is_valid_pos_b = self.password[self.pos_b-1] == self.letter
        return is_valid_pos_a ^ is_valid_pos_b

passwords = [Password.parse(line) for line in lines]

valid_count = 0

for password in passwords:
    if password.is_valid():
        valid_count += 1

print(f"Valid Passwords: {valid_count}")
