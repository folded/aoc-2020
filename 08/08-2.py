import sys

def ReadInstruction(line):
  opcode, oparg = line.split()
  oparg = int(oparg)
  return opcode, oparg

instructions = list(map(ReadInstruction, sys.stdin))

def Execute():
  pc = 0
  acc = 0
  reached = set()
  while pc not in reached:
    reached.add(pc)
    opcode, oparg = instructions[pc]
    if opcode == 'acc':
      acc += oparg
      pc += 1
    elif opcode == 'jmp':
      pc += oparg
    else:
      pc += 1
    if pc == len(instructions):
      return acc
  return None

for i in range(len(instructions)):
  if instructions[i][0] in ('nop', 'jmp'):
    alt = {'jmp': 'nop', 'nop': 'jmp'}[instructions[i][0]], instructions[i][1]
    alt, instructions[i] = instructions[i], alt
    val = Execute()
    if val is not None:
      print(val)
    alt, instructions[i] = instructions[i], alt
