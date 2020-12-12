import sys
import itertools

fields = { 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid' }

def ReadRecord(it):
  return list(itertools.takewhile(lambda x: x.strip(), it))

def IsValid(record):
  return (fields - set(record.keys())) <= { 'cid', }

def Records():
  lines = iter(sys.stdin)

  while True:
    record = ReadRecord(iter(sys.stdin))
    if not len(record): return
    record = { k: v for k, v in map(lambda x: x.split(':'), ' '.join(record).split()) }
    yield record

print(len([record for record in Records() if IsValid(record)]))