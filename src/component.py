from pigframe import Component
from dataclasses import dataclass

@dataclass
class Player(Component):
    # プレイヤーの部品を定義した
    x: int = 60
    y: int = 110

@dataclass
class Bullet(Component):
    # 弾の部品を定義した
    x: int = 0
    y: int = 0
    speed: int = 2
    