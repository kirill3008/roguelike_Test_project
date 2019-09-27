from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivy.uix.widget import Widget 
from kivy.core.window import Window
from time import sleep



Config.set('graphics', 'width', '768')
Config.set('graphics', 'height', '768')

class MainWidget(FloatLayout):
    def __init__(self):
        super(MainWidget, self).__init__()
        self.player_y = 0.5
        self.player_x = 0.5
        self.map = GridLayout(cols=12,rows=12,pos_hint = {'center_y':0.5, 'center_x':0.5},size_hint = (1,1))
        self.add_widget(self.map)
        f = open('polygon.txt')
        for line in f:
            for p in line:
                if p == '#':
                    self.map.add_widget(Image(source='sprites/wall1.png',allow_stretch=True))
                elif p == '.':
                    self.map.add_widget(Image(source='sprites/floor3.png',allow_stretch=True))




        self.player = Image(size_hint=(1/12,1/12),pos_hint={'center_x':0.5,'center_y':0.5},source='sprites/player.gif',allow_stretch=True,anim_delay=0.25)
        self.add_widget(self.player)

        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
    def update_pos(self):
        self.player.pos_hint = {'center_y':self.player_y, 'center_x':self.player_x}
    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None
    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'w' or keycode[1] == 'up':
            self.player_y += 1/24
            self.player_y = min(21/24,self.player_y)
            self.update_pos()
        elif keycode[1] == 's' or keycode[1] == 'down':
            self.player_y -= 1/24
            self.player_y = max(3/24,self.player_y)
            self.update_pos()
        elif keycode[1] == 'a' or keycode[1] == 'left':
            self.player_x -=1/24
            self.player_x = max(-3/24,self.player_x)
            self.update_pos()
        elif keycode[1] == 'd' or keycode[1] == 'right':
            self.player_x +=1/32
            self.player_x = min(27/24,self.player_x)
            self.update_pos()
        return True


class MainApp(App):
    def build(self):
        Window.size = (63*12, 64*12)
        return MainWidget()
MainApp().run()


class Player(object):
    def __init__(self,atack_range=64):
        pass