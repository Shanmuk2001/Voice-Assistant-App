import mysql.connector
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from datetime import datetime

Builder.load_file('SignApp.kv')

class SigninWindow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def validate_user(self):
        user = self.ids.username_field
        pwd = self.ids.pwd_field
        info = self.ids.info

        userid = user.text
        password = pwd.text

        if userid == '' or password == '':
            info.text = '[color=#FF0000]userid or password required[/color]'
        else:
            mydb = mysql.connector.connect(host="localhost", user='user1',password = 'MySQLdba',database = 'db')
            mycursor = mydb.cursor()
            mycursor.execute("select password from faculty where userid = %s",(userid,))
            myresult = mycursor.fetchone()
            try:
                if (myresult[0]==password):
                    info.text = '[color=#00FF00]Logged In Successfully[/color]' 
                    mycursor.execute("select gmail from faculty where userid = %s",(userid,))
                    my_res = mycursor.fetchone()
                    now = datetime.now()
                    sql_stat = "insert into history (userid,accessed_time) values (%s , %s)"
                    val = (userid , now)
                    mycursor.execute(sql_stat,val)
                    mydb.commit()
                    self.parent.parent.parent.ids.scrn_li_re.children[0].ids.year.text = ''
                    self.parent.parent.parent.ids.scrn_li_re.children[0].ids.sec.text = ''
                    self.parent.parent.parent.ids.scrn_li_re.children[0].ids.gen.text = ''
                    self.parent.parent.parent.ids.scrn_li_re.children[0].ids.info.text = ''
                    self.parent.parent.parent.ids.scrn_li_msg.children[0].ids.msg.text = ''
                    self.parent.parent.parent.ids.scrn_send_mail.children[0].ids.sender_mail.text = ''
                    self.parent.parent.parent.ids.scrn_send_mail.children[0].ids.receiver_mail.text = ''
                    self.parent.parent.parent.ids.scrn_send_mail.children[0].ids.msg.text = ''
                    self.parent.parent.parent.ids.scrn_send_mail.children[0].ids.pwd_field.text = ''
                    self.parent.parent.parent.ids.scrn_send_mail.children[0].ids.info.text = ''
                    self.parent.parent.parent.ids.scrn_send_mail.children[0].ids.sender_mail.text = str(my_res[0])
                    self.parent.parent.current = 'scrn_li_re'
                else:
                    info.text = '[color=#FF0000]Password is incorrect[/color]'
            except TypeError:
                info.text = '[color=#FF0000]No UserId Found[/color]'
            finally:
                mydb.close()


class SignApp(App):
    def build(self):
        return SigninWindow()

if __name__ =='__main__':
    sa = SignApp()
    sa.run()