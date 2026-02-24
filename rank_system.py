# rank_system.py
from config import *

class RankSystem:
    def __init__(self):
        self.rank = 2          # 筑基
        self.stars = 0
        self.points = 0
        self.just_ranked_up = False

    def win(self):
        self.just_ranked_up = False

        if self.rank in LOW_END:
            self.stars += 1
            if self.stars >= MAX_STARS:
                self.rank += 1
                self.stars = 0
                self.just_ranked_up = True

        elif self.rank in MID_END:
            self.stars += 1
            self.points += 20
            if self.stars >= MAX_STARS:
                self.rank += 1
                self.stars = 0
                self.points = 0
                self.just_ranked_up = True

        else:  # 高端
            self.points += 25
            if self.points >= 100:
                self.rank += 1
                self.points = 0
                self.just_ranked_up = True

    def lose(self):
        if self.rank in LOW_END:
            self.stars = max(0, self.stars - 1)
        elif self.rank in MID_END:
            self.points = max(0, self.points - 10)
        else:
            self.points = max(0, self.points - 20)

    @property
    def name(self):
        return RANKS[self.rank]