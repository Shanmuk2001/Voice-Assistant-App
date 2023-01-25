from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from signin import SigninWindow
from listen_rece import listen_receWindow
from listen_msg import listen_msgWindow
from Sendmail import send_mailWindow
from os.path import join,dirname
#from iconfonts import *

class MainWindow(BoxLayout):
    listen_rec_widget = listen_receWindow()
    sign_in_widget = SigninWindow()
    listen_msg_widget = listen_msgWindow()
    send_mail_widget = send_mailWindow()
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.ids.scrn_si.add_widget(self.sign_in_widget)
        self.ids.scrn_li_re.add_widget(self.listen_rec_widget)
        self.ids.scrn_li_msg.add_widget(self.listen_msg_widget)
        self.ids.scrn_send_mail.add_widget(self.send_mail_widget)

class mainApp(App):
    def build(self):
        return MainWindow()

if __name__ =='__main__':
    #register('default_font', 'fontawesome-webfont.ttf',join(dirname(__file__),'font-awesome.fontd'))
    sa = mainApp()
    sa.run()