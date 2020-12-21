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
s = np.array([ int(t.tile_id) for t,o in solution ]).reshape(N,N)
print(s[0,0]*s[-1,0]*s[0,-1]*s[-1,-1])
