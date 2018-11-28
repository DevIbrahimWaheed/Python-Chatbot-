from kivy.app import  App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
# All of the top imports are the Kivy GUI framework
#https://kivy.org/doc/ for help on the methods and classes

import Boxing as bk

# i know that global is bad , but it had to be done
height = 45
width = 500
Window.size = (width, height)



class TextDesign(BoxLayout): # Class inhertinace , the TestDesign used the boxlayout(from Kivy)
    sendText = ObjectProperty(None)
    sendBoxerText = ObjectProperty(None)

    def sendData(self):
        bk.StoreData(self.sendText.text)
        bk.BoxerConvo(self.sendBoxerText.text)
        bk.DumpData(self.sendBoxerText.text)


        # will send data to the function storedata in the boxing.py
        # the only way is to break up the entire boxing.py file and create a combat sport file
        # then create a true false statment!

        # #boxing convo
       # bk.MMAConvo(self.sendText.text)








class TextPageApp(App):
    pass


if __name__ == '__main__':
    TextPageApp().run()





#WEEK 3 SHOULD BE COMPLETED