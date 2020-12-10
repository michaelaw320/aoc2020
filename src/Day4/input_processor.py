from dataclasses import dataclass
from typing import Optional

# Make sure input file got extra newline as terminator
with open("../input/Day4/input") as f:
    lines = []
    buf = ""
    for line in f:
        if not line.strip():
            lines.append(buf.rstrip())
            buf = ""
        else:
            buf += line.strip() + " "

print(f"Scanned passports: {lines}")
print(f"Num of scanned passports: {len(lines)}")


@dataclass
class Passport:
    byr: str
    iyr: str
    eyr: str
    hgt: str
    hcl: str
    ecl: str
    pid: str
    cid: Optional[str] = None

    @classmethod
    def parse(cls, line: str):
        items = line.split(" ")
        kwargs = {item.split(":")[0]: item.split(":")[1] for item in items}
        return cls(**kwargs)


# Invalid passport won't be included

passports = []

for line in lines:
    try:
        passport = Passport.parse(line)
        passports.append(passport)
    except TypeError:
        pass

print(f"Valid Passports: {passports}")
print(f"Num of Valid Passports: {len(passports)}")
