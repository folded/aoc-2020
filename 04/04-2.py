import sys
import itertools
import re

fields = { 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid' }

def Match(regexp):
  def Validate(val):
    return regexp.match(val) is not None
  return Validate

def YearInRange(lo, hi):
  def Validate(val):
    if not Match(re.compile(r'^[0-9]{4}$'))(val):
      return False
    return lo <= int(val) <= hi
  return Validate

def Height():
  def Validate(val):
    m = re.match(r'([0-9]+)cm$', val)
    if m is not None:
      return 150 <= int(m.group(1)) <= 193
    m = re.match(r'([0-9]+)in$', val)
    if m is not None:
      return 59 <= int(m.group(1)) <= 76
    return False
  return Validate

validators = dict(
  byr = YearInRange(1920,2002),
  iyr = YearInRange(2010,2020),
  eyr = YearInRange(2020,2030),
  hgt = Height(),
  hcl = Match(re.compile(r'^#[0-9a-f]{6}$')),
  ecl = Match(re.compile(r'^(amb|blu|brn|gry|grn|hzl|oth)$')),
  pid = Match(re.compile(r'^[0-9]{9}$'))
)

def ReadRecord(it):
  return list(itertools.takewhile(lambda x: x.strip(), it))

def IsValid(record):
  return (fields - set(record.keys())) <= { 'cid', } and all(v(record[k]) for k, v in validators.items())

def Records():
  lines = iter(sys.stdin)

  while True:
    record = ReadRecord(iter(sys.stdin))
    if not len(record): return
    record = { k: v for k, v in map(lambda x: x.split(':'), ' '.join(record).split()) }
    yield record

print(len([record for record in Records() if IsValid(record)]))