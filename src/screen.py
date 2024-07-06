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
            
class ScInvader(Screen):
    def draw(self):
        entities = self.world.entities.keys()
        invader_exist = False
        for ent in entities:
            if self.world.has_component(ent, Invader):
                invader_exist = True
        
        if invader_exist == False:
            return
        
        for ent, (invader) in self.world.get_component(Invader):
            pyxel.rect(invader.x, invader.y, 10, 10, 7)
            
class ScStatus(Screen):
    def draw(self):
        status = self.world.get_component(Status)[0][1]
        pyxel.text(0, 0, "SCORE:{}".format(status.score), 7)
        pyxel.text(0, 10, "LEVEL:{}".format(status.level), 7)
        pyxel.text(0, 20, "TIME:{}".format(status.elapsed_time), 7)
        pyxel.text(0, 30, "SPEED:{}".format(status.current_speed), 7)
        pyxel.text(0, 40, "DROP:{}".format(status.current_drop_pixel), 7)
        pyxel.text(0, 50, "ENEMY_DOWN:{}".format(status.enemy_down), 7)

class ScGameOver(Screen):
    def draw(self):
        pyxel.text(55, 50, "GAME OVER", 8)
        pyxel.text(55, 60, "SCORE:{}".format(self.world.get_component(Status)[0][1].score), 8)
        pyxel.text(55, 70, "TIME:{}".format(self.world.get_component(Status)[0][1].elapsed_time), 8)
        pyxel.text(55, 80, "LEVEL:{}".format(self.world.get_component(Status)[0][1].level), 8)
        pyxel.text(55, 90, "ENEMY_DOWN:{}".format(self.world.get_component(Status)[0][1].enemy_down), 8)
        pyxel.text(55, 100, "PRESS SPACE KEY", 8)