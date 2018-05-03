# ex43.py
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        pass


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        current_scene = self.scene_map.next_scene(current_scene.enter())
        #current_scene.enter()



class Death(Scene):

    death_message = ['You died.', 'Game over man, game over!', 
        'That looked like it hurt!', 'Go home, you are drunk']

    def enter(self):
        print(self.death_message[randint(0, len(self.death_message) - 1)])
        exit(1)


class CentralCorridor(Scene):
    
    def enter(self):
        print(dedent(
            """
            You are in the central corridor.
            """
        ))
        return 'death'


class LaserWeaponArmory(Scene):

        def enter(self):
            print(dedent(
                """
                You are in the central corridor.
                """
            ))
            return 'death'


class TheBridge(Scene):

        def enter(self):
            print(dedent(
                """
                You are in the central corridor.
                """
            ))
            return 'death'


class EscapePod(Scene):

        def enter(self):
            print(dedent(
                """
                You are in the central corridor.
                """
            ))
            return 'finished'


class Finished(Scene):

    def enter(self):
        print(dedent(
            """
            You see a blinding explosion that was once a ship from
            the window of your espace pod which launched mere seconds ago.
            You won the game, incredible.
            """
        ))


class Map(object):

    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        scene = Map.scenes.get(scene_name)
        return scene

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map  = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()