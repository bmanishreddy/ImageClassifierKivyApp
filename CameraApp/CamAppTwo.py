'''
Camera Example
==============

This example demonstrates a simple use of the camera. It shows a window with
a buttoned labelled 'play' to turn the camera on and off. Note that
not finding a camera, perhaps because gstreamer is not installed, will
throw an exception during the kv language processing.

'''

# Uncomment these lines to see all the messages
# from kivy.logger import Logger
# import logging
# Logger.setLevel(logging.TRACE)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen



#class ScecondWindow(Screen):
#    pass
#class WindowManager(ScreenManager):
#    pass
class WindowManager(ScreenManager):
    pass
class ScecondWindow(Screen):
    pass




class CameraClick(BoxLayout,Screen):
    pass

    def capture(self):

        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")
        pass


#kv = Builder.load_file("testcamera.kv")


class TestCamera(App):

    def build(self):
        pass


TestCamera().run()
