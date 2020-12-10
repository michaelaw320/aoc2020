import attr

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


class ValidationError(Exception):
    pass


@attr.s
class Passport:
    byr: str = attr.ib()
    iyr: str = attr.ib()
    eyr: str = attr.ib()
    hgt: str = attr.ib()
    hcl: str = attr.ib()
    ecl: str = attr.ib()
    pid: str = attr.ib()
    cid: Optional[str] = attr.ib(default=None)

    @classmethod
    def parse(cls, line: str):
        items = line.split(" ")
        kwargs = {item.split(":")[0]: item.split(":")[1] for item in items}
        return cls(**kwargs)

    @byr.validator
    def byr_valid(self, attribute, value):
        try:
            valid = len(value) == 4 and (1920 <= int(value) <= 2002)
            if not valid:
                raise ValidationError()
        except:
            raise ValidationError()

    @iyr.validator
    def iyr_valid(self, attribute, value):
        try:
            valid = len(value) == 4 and (2010 <= int(value) <= 2020)
            if not valid:
                raise ValidationError()
        except:
            raise ValidationError()

    @eyr.validator
    def eyr_valid(self, attribute, value):
        try:
            valid = len(value) == 4 and (2020 <= int(value) <= 2030)
            if not valid:
                raise ValidationError()
        except:
            raise ValidationError()

    @hgt.validator
    def hgt_valid(self, attribute, value):
        try:
            if not value.endswith(("cm", "in")):
                raise ValidationError()
            hgt = int(value[:-2])
            unit = value[-2:]
            if unit == "cm":
                if 150 <= hgt <= 193:
                    return
                else:
                    raise ValidationError()
            else:
                if 59 <= hgt <= 76:
                    return
                else:
                    raise ValidationError()
        except:
            raise ValidationError()

    @hcl.validator
    def hcl_valid(self, attribute, value):
        if not value.startswith("#"):
            raise ValidationError()
        try:
            int(value[1:], 16)
        except:
            raise ValidationError()

    @ecl.validator
    def ecl_valid(self, attribute, value):
        if value not in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
            raise ValidationError()

    @pid.validator
    def pid_valid(self, attribute, value):
        if len(value) != 9:
            raise ValidationError()
        try:
            int(value)
        except:
            raise ValidationError()


# Invalid passport won't be included

passports = []

for line in lines:
    try:
        passport = Passport.parse(line)
        passports.append(passport)
    except (TypeError, ValidationError):
        pass

print(f"Valid Passports: {passports}")
print(f"Num of Valid Passports: {len(passports)}")

