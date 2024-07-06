import pyxel
from pigframe import *
from input import Input
from screen import *

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
app.add_scene("Play")
app.set_user_actions_map(Input())
app.current_scene = "Play"
app.add_screen(ScPlayer)
app.run()
