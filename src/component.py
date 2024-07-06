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

@dataclass
class Invader(Component):
    # 敵の部品を定義した
    x: int = 0
    y: int = 0
    speed: int = 1
    drop_pixel: int = 10
    direction: int = 1

@dataclass
class Status(Component):
    # ゲームの状態を定義した
    enemy_down: int = 0
    level_enemy_down: int = 0
    score: int = 0
    elapsed_time: int = 0
    level: int = 1
    current_speed: int  =1
    current_drop_pixel: int = 10