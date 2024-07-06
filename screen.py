from pigframe import Screen
import pyxel

class ScPlayer(Screen):
    # プレイヤーの描画
    def draw(self):
        # x, y座標, 大きさを指定して四角形を描画する
        pyxel.rect(80, 110, 8, 6, 3)
