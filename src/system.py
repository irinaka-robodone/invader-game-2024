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

class SpawnInvader(System):
    def process(self):
        count_frame = self.world.count_frame
        
        status = self.world.get_component(Status)[0][1]
        current_drop_pixel = status.current_drop_pixel
        current_speed = status.current_speed
        
        if count_frame % 20 == 0:
            ent = self.world.create_entity()
            self.world.add_component_to_entity(ent, Invader, x = 10, y = 10, speed = current_speed, 
                                            drop_pixel = current_drop_pixel, direction = 1)

class InvaderMove(System):
    def process(self):
        entities = self.world.entities.keys()
        invader_exist = False
        for ent in entities:
            if self.world.has_component(ent, Invader):
                invader_exist = True
        
        if invader_exist == False:
            return
        
        width = self.world.SCREEN_SIZE[0]
        height = self.world.SCREEN_SIZE[1]
        
        for ent, (invader) in self.world.get_component(Invader):
            invader.x += invader.speed * invader.direction
            if invader.x > width or invader.x < 0:
                invader.direction *= -1
                invader.y += invader.drop_pixel
            if invader.y > height:
                self.world.remove_entity(ent)
                print(ent, "is removed")
                self.world.scene_manager.next_scene = "GameOver"

class BulletHitInvader(System):
    def process(self):
        entities = self.world.entities.keys()
        bullet_exist = False
        invader_exist = False
        
        for ent in entities:
            if self.world.has_component(ent, Bullet):
                bullet_exist = True
            if self.world.has_component(ent, Invader):
                invader_exist = True
        
        if bullet_exist == False or invader_exist == False:
            return
        
        status = self.world.get_component(Status)[0][1]
        
        for ent_b, (bullet) in self.world.get_component(Bullet):
            for ent_i, (invader) in self.world.get_component(Invader):
                if bullet.x < invader.x + 10 and bullet.x + 2 > invader.x and bullet.y < invader.y + 10 and bullet.y + 2 > invader.y:
                    self.world.remove_entity(ent_b)
                    self.world.remove_entity(ent_i)
                    status.enemy_down += 1 # 敵を倒した数をカウント
                    status.level_enemy_down += 1 # レベルアップのための敵を倒した数をカウント
                    status.score += status.level
                    print(ent_b, "and", ent_i, "are removed")
                    break

class UpdateLevel(System):
    def process(self):
        status = self.world.get_component(Status)[0][1]
        
        if status.level_enemy_down % 10 == 0 and status.level_enemy_down != 0:
            status.level += 1
            status.level_enemy_down = 0
            status.current_speed += 1
            status.current_drop_pixel += 1
            print("level up to", status.level)
            