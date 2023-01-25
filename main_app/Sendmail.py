from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import smtplib
from kivy.lang import Builder


Builder.load_file('sendmail.kv')
class send_mailWindow(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
    
    def sending_mail(self):
        pwd = self.ids.pwd_field
        info = self.ids.info
        sender_mail = self.ids.sender_mail.text
        receivers = self.ids.receiver_mail.text
        text_msg = self.ids.msg.text
        sender_pass = pwd.text
        smtpObj = smtplib.SMTP('smtp.gmail.com' , 587)
        smtpObj.starttls()
        try:
            smtpObj.login(sender_mail,sender_pass)
            smtpObj.sendmail(sender_mail, receivers, str(text_msg))
            info.text = "[color=#00FF00]Successfully sent email[/color]"
        except smtplib.SMTPAuthenticationError:
            info.text = "[color=#FF0000]Authentication is incorrect.\nPlease change the security options.\n                   or\nUsername or password is incorrect.[/color]"
        finally:
            smtpObj.quit()
    def log_out(self):
        self.parent.parent.parent.ids.scrn_si.children[0].ids.username_field.text = ''
        self.parent.parent.parent.ids.scrn_si.children[0].ids.pwd_field.text = ''
        self.parent.parent.parent.ids.scrn_si.children[0].ids.info.text = ''
        self.parent.parent.current = 'scrn_si'

class sendmailApp(App):
    def build(self):
        return send_mailWindow()

if __name__ =='__main__':
    sa = sendmailApp()
    sa.run()