# ex43.py
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("Default enter method.")
        pass

class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        current_scene.enter()


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
            Come on, do stuff.

            """
        ))

        choice = input(">")
        if choice == '1':
            return 'laser_weapon_armory'
        else:
            print("Does note compute!")
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent(
            """
            You are in the laser weapon armory, an expansive room filled with
            shelving units & console displays. You spot a safe that appears 
            just the size, shape, and security for a laser weapon. 
            It appears to require a 3 digit code.

            """
        ))

        choice = input(">")

        if any(c in choice for c in ("look", "investigate")):
            print(dedent(
                """
                When looking around the room you notice a small
                yellow post-it note stuck to the bottom of a display
                with 'password' written on the top. Underneath,
                you're able to make out the first two digits as '57'
                The third is badly smudged and illegible.

                """
        ))
        
        print(dedent(
            """
            You approach the laser weapon safe keypad, your
            intuition tells you that yours attempts will be limited.

            """
        ))
        
        case_code = f"57{randint(0,9)}"
        guess = input("[keypad]>")
        guesses = 0

        while guess != case_code and guesses <= 10:
            guess = input("[keypad]>")
            guesses += 1
        
        if guess == case_code:
            print(dedent(
                """
                The case clicks open. You carefully lift the laser weapon from its
                secure case is toss it carelessly into your pack.

                It begins emitting a chirp at regular intervals.

                """
            ))
            return 'the_bridge'   
        else:
            print(dedent(
                """
                After your last incorrect attempt the keypad is no long responding to your input.
                The room's blast doors slam shut. A thick green gas begins to pour in from the
                room's ventilation system.

                """
            ))
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print(dedent(
            """
            You are in the bridge.
            """
        ))

        choice = input("Press 1 to plant the bomb> ")

        if choice == "1":
            return 'escape_pod'
        else:
            print("I can't believe you screwed that up.")
            return 'death'


class EscapePod(Scene):

    def enter(self):
        print(dedent(
            """
            You are in the escape pod.
            
            """
        ))
        return 'finished'


class Finished(Scene):

    def enter(self):
        print(dedent(
            """
            You see a blinding explosion that was once a ship from
            the window of your espace pod which launched mere seconds ago.
            You won the game, bigly.

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


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()