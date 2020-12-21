import sys
import numpy as np
import re

class Tile:
  @classmethod
  def _BordersOf(cls, tile):
    N = tile.shape[0]
    p2 = np.power(np.ones(N, int) * 2, np.arange(N))
    def AsInt(bits):
      return np.sum(p2 * bits)
    a, b, c, d = tile[0], tile[:,0].reshape(-1), tile[-1], tile[:,-1].reshape(-1)
    return AsInt(a), AsInt(b), AsInt(c), AsInt(d)

  def __init__(self, tile_id, tile):
    self.tile_id = tile_id
    self.tile = tile
    self.borders = []
    for rot in range(4):
      self.borders.append(self._BordersOf(np.rot90(tile, k=rot)))
      self.borders.append(self._BordersOf(np.rot90(np.fliplr(tile), k=rot)))

  def OrientedTile(self, orientation):
    t = self.tile
    if orientation % 2:
      t = np.fliplr(t)
    return np.rot90(t, k=orientation // 2)    

  def OrientedBorders(self, orientation):
    return self.borders[orientation]

  @classmethod  
  def Read(cls, inf):
    tile_id = inf.readline()
    if tile_id == '':
      raise EOFError
    tile_id = re.match(r'Tile ([0-9]+):', tile_id).group(1)
    rows = []
    while True:
      row = inf.readline()
      if row.strip() == '':
        break
      rows.append(list(row.strip()))
    return cls(tile_id, (np.array(rows) == '#'))

  @classmethod
  def ReadAll(cls, inf):
    while True:
      try:
        yield cls.Read(inf)
      except EOFError:
        return

def Solve(tiles, placement, N):
  if not len(tiles):
    yield placement
  else:
    north = placement[-N] if len(placement) >= N else None
    west = placement[-1] if len(placement) % N else None
    north_border = None
    west_border = None

    if north is not None:
      north_border = north[0].OrientedBorders(north[1])[2]
    if west is not None:
      west_border = west[0].OrientedBorders(west[1])[3]

    for i, tile in enumerate(tiles):
      for orientation in range(8):
        b = tile.OrientedBorders(orientation)
        if north_border is not None and north_border != b[0]:
          continue
        if west_border is not None and west_border != b[1]:
          continue
        yield from Solve(tiles[:i]+tiles[i+1:], placement + ((tile, orientation),), N)


tiles = list(Tile.ReadAll(sys.stdin))
N_tiles = len(tiles)
N = int(N_tiles ** .5)
assert N * N == N_tiles

solution = next(Solve(tiles, (), N))

oriented_tiles = [
  t.OrientedTile(o)[1:-1,1:-1] for t, o in solution
]
rows = [
  np.concatenate(oriented_tiles[i:i+N], axis=1) for i in range(0, N*N, N)
]

img = np.concatenate(rows, axis=0)

sea_monster = np.array([
  list('..................#.'),
  list('#....##....##....###'),
  list('.#..#..#..#..#..#...')
]) == '#'

Sx, Sy = sea_monster.shape
Sc = np.sum(sea_monster)
Ix, Iy = img.shape

full_tile = Tile('', img)
for orientation in range(8):
  img = full_tile.OrientedTile(orientation)
  N_sea_monsters = 0
  for x in range(0, Ix-Sx):
    for y in range(0, Iy-Sy):
      if np.sum(img[x:x+Sx,y:y+Sy] * sea_monster) == Sc:
        N_sea_monsters += 1
  if N_sea_monsters != 0:
    break

print(np.sum(full_tile.tile) - Sc * N_sea_monsters)
