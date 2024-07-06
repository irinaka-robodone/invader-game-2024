from pigframe import ActionMap
from dataclasses import dataclass
import pyxel

@dataclass
class Input(ActionMap):
    # ゲームで使うユーザーの入力を定義するクラス
    
    space = pyxel.btnp, pyxel.KEY_SPACE # スペースキー
    left = pyxel.btnp, pyxel.KEY_A # 左キー
    right = pyxel.btnp, pyxel.KEY_D # 右キー

