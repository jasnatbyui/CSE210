import constants

from game.casting.cast import Cast
from game.casting.trail import Trail
from game.casting.score1 import Score1
from game.casting.score2 import Score2
from game.casting.cycle_one import CycleOne
from game.casting.cycle_two import CycleTwo
from game.scripting.script import Script
from game.scripting.control_actors_action1 import ControlActorsAction1
from game.scripting.control_actors_action2 import ControlActorsAction2
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("trails", Trail())
    cast.add_actor("snakes1", CycleOne())
    cast.add_actor("snakes2", CycleTwo())
    cast.add_actor("scores1", Score1())
    cast.add_actor("scores2", Score2())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction1(keyboard_service))
    script.add_action("input", ControlActorsAction2(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()