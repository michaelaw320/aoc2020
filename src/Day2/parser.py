import re

from dataclasses import dataclass

with open("../input/Day2/input") as f:
    lines = [line for line in f]

input_pattern = re.compile("(\d+)-(\d+) (.): (.*)")


@dataclass
class Password:
    min_len: int
    max_len: int
    letter: str
    password: str

    @classmethod
    def parse(cls, item: str):
        match = input_pattern.split(item)
        return cls(int(match[1]), int(match[2]), str(match[3]), str(match[4]))

    def is_valid(self) -> bool:
        occurences = self.password.count(self.letter)
        return self.min_len <= occurences <= self.max_len


passwords = [Password.parse(line) for line in lines]

valid_count = 0

for password in passwords:
    if password.is_valid():
        valid_count += 1

print(f"Valid Passwords: {valid_count}")
