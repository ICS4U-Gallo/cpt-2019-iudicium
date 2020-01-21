import arcade

import settings

from menu import MenuView
from chapter_1 import MyGame
from chapter_2 import Chapter2View
from chapter_3 import ch3_MenuView
from chapter_4 import ch4_MenuView


class Director(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.view_index = 0
        self.views = [
            MenuView,
            MyGame,
            Chapter2View,
            ch3_MenuView,
            ch4_MenuView
        ]
        self.next_view()

    def next_view(self):
        next_view = self.views[self.view_index]()
        next_view.director = self
        self.show_view(next_view)
        self.view_index = (self.view_index + 1) % len(self.views)

def main():
    window = Director(settings.WIDTH, settings.HEIGHT, "CPT Structure")
    arcade.run()
    


if __name__ == "__main__":
    main()
