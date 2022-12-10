import constants
import random
from game.shared.color import Color
from game.shared.point import Point
from game.casting.cast import Cast
from game.casting.mineral import Mineral
from game.casting.food import Food
from game.casting.score import Score
from game.casting.score1 import Score1
#from game.casting.snake import Snake
#from game.casting.snake1 import Snake1
from game.casting.space_ship import Spaceship
from game.scripting.script import Script
from game.scripting.control_snake0_action import ControlSnake0Action
from game.scripting.control_snake1_action import ControlSnake1Action
from game.scripting.control_spaceship_action import ControlSpaceshipAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.scripting.random_growth import RandomGrowth
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("foods", Food())
    cast.add_actor("foods", Food())
    #cast.add_actor("snakes", Snake()) # Player 1
    #cast.add_actor("snakes", Snake1()) # Player 2
    cast.add_actor("ships", Spaceship())
    cast.add_actor("scores", Score())
    cast.add_actor("scores", Score1())

    for n in range(constants.DEFAULT_MINERALS):

        mineral_velocity = Point(0, 5)
        
        x = random.randint(1, constants.COLUMNS - 1)
        y = random.randint(1, constants.ROWS - 1)
        position = Point(x, y)
        position = position.scale(constants.CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        mineral = Mineral()
        mineral.rand_properties()
        mineral.set_font_size(constants.FONT_SIZE)
        mineral.set_color(color)
        mineral.set_position(position)
        mineral.set_velocity(mineral_velocity)
        cast.add_actor("minerals", mineral)  
  
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    #script.add_action("input", ControlSnake0Action(keyboard_service))
    #script.add_action("input", ControlSnake1Action(keyboard_service))
    script.add_action("input", ControlSpaceshipAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    #script.add_action("update", RandomGrowth())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()