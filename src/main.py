import pyxel
from pigframe import *
from input import Input
from screen import *
from system import *
from component import *
from event import *

class App(World):
    # ゲームのクラス
    def __init__(self):
        # ゲームのウィンドウの初期化
        super().__init__()
        self.SCREEN_SIZE = (160, 120)
        pyxel.init(self.SCREEN_SIZE[0], self.SCREEN_SIZE[1], title = "インベーダーゲーム", fps = 60)
        self.init()
        
    def init(self):
        # ゲームの初期化、リスタートのときに使う関数
        self.count_frame = 0
        # ゲームに登場するオブジェクトの追加
        player = self.create_entity()
        self.add_component_to_entity(player, Player, x = 60, y = 104)

        status = self.create_entity()
        self.add_component_to_entity(status, Status, enemy_down = 0, score = 0, elapsed_time = 0, level = 1, current_speed = 1, current_drop_pixel = 10)

    
    def run(self):
        # ゲームのメインループを走らせる関数
        pyxel.run(self.update, self.draw)
    
    def update(self):
        # ゲームのシステムを動かす関数
        self.count_frame += 1
        self.process()
        
    def draw(self):
        # 画面の描画をする関数
        pyxel.cls(0)
        self.process_screens()

app = App()
app.add_scenes(["Play", "GameOver"])
app.set_user_actions_map(Input())

# システムの追加
app.add_system_to_scenes(PlayerControl, "Play")
app.add_system_to_scenes(PlayerShoot, "Play")
app.add_system_to_scenes(BulletMove, "Play")
app.add_system_to_scenes(SpawnInvader, "Play")
app.add_system_to_scenes(InvaderMove, "Play")
app.add_system_to_scenes(BulletHitInvader, "Play")
app.add_system_to_scenes(UpdateLevel, "Play")

# スクリーンの追加
app.add_screen_to_scenes(ScPlayer, "Play")
app.add_screen_to_scenes(ScBullet, "Play")
app.add_screen_to_scenes(ScInvader, "Play")
app.add_screen_to_scenes(ScStatus, "Play")
app.add_screen_to_scenes(ScGameOver, "GameOver")

# イベントの追加
app.add_event_to_scene(Restart, "GameOver", lambda: pyxel.btnp(pyxel.KEY_SPACE))

# ゲームの初期状態を設定
app.current_scene = "Play"
app.run()
