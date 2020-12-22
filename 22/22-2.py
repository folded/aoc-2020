import sys
import collections
import numpy as np

memo = {}

class Player:
  def __init__(self, deck):
    self.deck = collections.deque(deck)

  @property
  def deck_count(self):
    return len(self.deck)

  @classmethod
  def Read(self, inf):
    header = inf.readline()
    if header == '':
      raise EOFError
    player = Player([])
    while True:
      line = inf.readline()
      if line.strip() == '':
        break
      player.deck.append(int(line))
    return player

  def Draw(self):
    return self.deck.popleft()
  
  def Take(self, *cards):
    self.deck.extend(cards)

  @property  
  def score(self):
    return np.sum(np.arange(self.deck_count, 0, -1) * np.array(self.deck))

  @property
  def state(self):
    return tuple(self.deck)

class Game:
  def __init__(self, player1, player2):
    self.player1 = player1
    self.player2 = player2

  def Play(self):
    observed_states = set()

    while self.player1.deck_count and self.player2.deck_count:
      state = self.player1.state, self.player2.state
      if state in observed_states:
        return self.player1
      observed_states.add(state)

      card1 = self.player1.Draw()
      card2 = self.player2.Draw()

      if state in memo:
        round_winner = self.player1 if memo[state] else self.player2
      else:
        if card1 <= self.player1.deck_count and card2 <= self.player2.deck_count:
          # recurse
          p1 = Player(tuple(self.player1.deck)[:card1])
          p2 = Player(tuple(self.player2.deck)[:card2])
          round_winner = self.player1 if Game(p1, p2).Play() is p1 else self.player2
        else:
          round_winner = self.player1 if card1 > card2 else self.player2

        memo[state] = round_winner is self.player1

      if round_winner is self.player1:
        self.player1.Take(card1, card2)
      else:
        self.player2.Take(card2, card1)

    if self.player1.deck_count:
      return self.player1
    else:
      return self.player2


player1 = Player.Read(sys.stdin)
player2 = Player.Read(sys.stdin)

winner = Game(player1, player2).Play()

print(winner.score)