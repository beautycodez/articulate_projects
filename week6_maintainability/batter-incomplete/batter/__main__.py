import os
from constants import *
from game.directing.director import Director
from game.directing.scene_manager import SceneManager


def main():
    os.chdir(r'batter-incomplete')
    director = Director(SceneManager.VIDEO_SERVICE)
    director.start_game()

if __name__ == "__main__":
    main()