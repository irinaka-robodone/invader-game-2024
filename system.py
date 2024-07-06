from pigframe import System, Component

class Player(Component):
    # プレイヤーの部品を定義した
    x: int = 60
    y: int = 110

class PlayerControl(System):
    # プレイヤーを操作するクラス
    def process(self):
        # 操作に使うユーザーの入力を取得
        actions = self.world.actions
        
        # プレイヤーの座標を更新
        if actions.left:
            # 左に移動
            pass
        if actions.right:
            # 右に移動
            pass