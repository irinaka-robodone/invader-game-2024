from pigframe import System, Component
from component import *

class PlayerControl(System):
    # プレイヤーを操作するクラス
    def process(self):
        # 操作に使うユーザーの入力を取得
        actions = self.world.actions

        for entity, (player) in self.world.get_component(Player):
            # プレイヤーの座標を更新
            if actions.left:
                # 左に移動
                player.x -= 1
            if actions.right:
                # 右に移動
                player.x += 1

class PlayerShoot(System):
    def process(self):
        actions = self.world.actions
        
        for entity, (player) in self.world.get_component(Player):
            if actions.space:
                ent = self.world.create_entity()
                print("bullet is created as", ent)
                self.world.add_component_to_entity(ent, Bullet, x = player.x + 4, y = player.y - 2)
                
class BulletMove(System):
    def process(self):
        entities = self.world.entities.keys()
        bullet_exist = False
        for ent in entities:
            if self.world.has_component(ent, Bullet):
                bullet_exist = True
        
        if bullet_exist == False:
            return
        
        for ent, (bullet) in self.world.get_component(Bullet):
            bullet.y -= bullet.speed
            if bullet.y < 0:
                self.world.remove_entity(ent)
                print(ent, "is removed")