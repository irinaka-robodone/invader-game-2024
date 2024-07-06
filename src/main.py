import pyxel
from pigframe import *
from input import Input
from screen import *
from system import *
from component import *

class App(World):
    # ゲームのクラス
    def __init__(self):
        # ゲームのウィンドウの初期化
        super().__init__()
        pyxel.init(160, 120, title = "インベーダーゲーム", fps = 60)
        
    def init(self):
        # ゲームの初期化、リスタートのときに使う関数
        pass
    
    def run(self):
        # ゲームのメインループを走らせる関数
        pyxel.run(self.update, self.draw)
    
    def update(self):
        # ゲームのシステムを動かす関数
        self.process()
        
    def draw(self):
        # 画面の描画をする関数
        pyxel.cls(0)
        self.process_screens()

app = App()
app.add_scenes(["Play", "Result"])
app.set_user_actions_map(Input())

# システムの追加
app.add_system_to_scenes(PlayerControl, "Play")
app.add_system_to_scenes(PlayerShoot, "Play")
app.add_system_to_scenes(BulletMove, "Play")

# スクリーンの追加
app.add_screen_to_scenes(ScPlayer, "Play")
app.add_screen_to_scenes(ScBullet, "Play")

# ゲームに登場するオブジェクトの追加
player = app.create_entity()
app.add_component_to_entity(player, Player, x = 60, y = 104)

# ゲームの初期状態を設定
app.current_scene = "Play"
app.run()
