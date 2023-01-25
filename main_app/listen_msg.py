from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import speech_recognition as sr
from kivy.lang import Builder

Builder.load_file('Listenmsg.kv')
mytext = ""
class listen_msgWindow(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def lis_msg(self):
        global mytext
        msg = self.ids.msg
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source,duration=0.3)
            audio_temp = r.listen(source)
            try:
                mytext = r.recognize_google(audio_temp)
                mytext = mytext.lower()
                msg.text = mytext
            except sr.UnknownValueError:
                msg.text = "[color=#FF0000]I didnt get you[/color]"
                return
            except sr.RequestError:
                msg.text = "[color=#FF0000]Please Connect to internet to Continue[/color]"
                return

    def prev_wind(self):
        self.parent.parent.current = 'scrn_li_re'
    
    def next_wind(self):
        if mytext!="":
            self.parent.parent.parent.ids.scrn_send_mail.children[0].ids.msg.text = mytext
            self.parent.parent.current = 'scrn_send_mail'
        else:
            info = self.ids.info
            info.text = "[color=#FF0000]You didnot say the message[/color]"
            

class ListenmsgApp(App):
    def build(self):
        return listen_msgWindow()

if __name__ =='__main__':
    sa = ListenmsgApp()
    sa.run()