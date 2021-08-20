import os, win32gui, win32con, win32api
import kivy
from KivyOnTop import register_topmost, unregister_topmost
from kivy.core.window import Window
import pyautogui
from kivy.config import Config
from kivy.animation import Animation
from kivy.properties import StringProperty, NumericProperty
from kivy.clock import Clock
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
# Config.set('kivy','window_icon','C:\\Users\\soumy\\Desktop\\WebDev\\CSS-PersonalSite\\Favicons\\favicon.ico')
kivy.require('1.11.0')
width, height = pyautogui.size()
#Config.set('graphics', 'width', str(width))
#Config.set('graphics', 'height', str(height))



from kivy.app import App
from kivy.uix.button import Label

class PyEye(App):
    count = 25

    def build(self):
        layout = GridLayout(cols=1, rows=7)
        layout.add_widget(Label(text=""))
        self.myLabel = Label(text ='Look Away For 25 Seconds...', font_size="40sp" )
        layout.add_widget(self.myLabel)
        Clock.schedule_interval(self.Callback_Clock, 1)
        Clock.schedule_once(App.get_running_app().stop, 25)
        
        if 1 == 1:
            
            ButtonSkip = Button(text ="Skip",size_hint_x=None, width=(25/100*))#
            layout.add_widget(Label(text=""))
            layout1 = AnchorLayout(anchor_x='center', anchor_y='bottom')
            layout1.add_widget(ButtonSkip)

            layout.add_widget(Label(text=""))
            layout.add_widget(Label(text=""))
            ButtonSkip.bind(on_press= App.get_running_app().stop)
            layout.add_widget(Label(text=""))
        return layout

    def Callback_Clock(self, dt):
        self.count = self.count - 1
        self.myLabel.text = "Look Away For %d Seconds" %(self.count)


helloKivy= PyEye()
helloKivy.run()
