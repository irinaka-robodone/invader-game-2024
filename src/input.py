from pigframe import ActionMap
from dataclasses import dataclass
import pyxel

@dataclass
class Input(ActionMap):
    # ゲームで使うユーザーの入力を定義するクラス
    space: tuple = pyxel.btnp, pyxel.KEY_SPACE # スペースキー
    left: tuple = pyxel.btn, pyxel.KEY_A # 左キー
    right: tuple = pyxel.btn, pyxel.KEY_D # 右キー

