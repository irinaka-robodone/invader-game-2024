from pigframe import Screen
import pyxel
from component import *

class ScPlayer(Screen):
    # プレイヤーの描画
    def draw(self):
        for ent, (player) in self.world.get_component(Player):
            pyxel.rect(player.x, player.y, 10, 10, 9)

class ScBullet(Screen):
    def draw(self):
        entities = self.world.entities.keys()
        bullet_exist = False
        for ent in entities:
            if self.world.has_component(ent, Bullet):
                bullet_exist = True
        
        if bullet_exist == False:
            return
        
        for ent, (bullet) in self.world.get_component(Bullet):
            pyxel.rect(bullet.x, bullet.y, 2, 2, 8)