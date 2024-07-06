from pigframe import Event
from component import *

class Restart(Event):
    def _Event__process(self):
        self.world.init()
        self.world.scene_manager.next_scene = "Play"
        player_ent = self.world.get_component(Player)[0][0]
        status_ent = self.world.get_component(Status)[0][0]
        
        for bullet_ent, (_) in self.world.get_component(Bullet):
            self.world.remove_entity(bullet_ent)
        for invader_ent, (_) in self.world.get_component(Invader):
            self.world.remove_entity(invader_ent)
            
        self.world.remove_entity(player_ent)
        self.world.remove_entity(status_ent)
        