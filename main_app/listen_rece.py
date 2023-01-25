from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import speech_recognition as sr
from kivy.lang import Builder
import mysql.connector
mytext = ""
Builder.load_file('ListenApp.kv')

class listen_receWindow(BoxLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)

    def lis_rec(self):
        global mytext
        mytext=''
        info = self.ids.info
        info.text=''
        try:
            year = self.ids.year.text
            if year=='':
                info.text = '[color=#FF0000]Please Mention year[/color]'
                return
            year = int(year)
            if year not in range(1,5):
                info.text = "[color=#FF0000]Year must be between 1 and 4[/color]"
                return
        except:
            info.text = "[color=#FF0000]Year must be in numbers[/color]"
            return
        try:
            sec = self.ids.sec.text
            if sec=='':
                info.text = '[color=#FF0000]Please Mention Section[/color]'
                return
            sec = int(sec)
        except:
            info.text = "[color=#FF0000]section must be in numbers[/color]"
            return
        gen = self.ids.gen.text
        if gen=='':
            info.text = "[color=#FF0000]Please Mention gender[/color]"
            return
        if (year not in range(1,5)) or (sec not in range(1,15)) or (gen not in ['m','f']):
            info.text = "[color=#FF0000]Please Enter valid details[/color]"
            return
        else:
            dic_gen = {'m':'boy','f':'girl'}
            dic_sec=96
            sec = chr(dic_sec+sec)
            gen = dic_gen[gen]
            mydb = mysql.connector.connect(host="localhost", user='user1',password = 'MySQLdba',database = 'db')
            mycursor = mydb.cursor()
            mycursor.execute("select gmail from cr where sec='%s' and year='%d' and gender='%s'"%(sec,year,gen))
            myres = mycursor.fetchone()
            dic_print = {1:'st',2:'nd',3:'rd'}
            try:
                mytext = myres[0]
                prin_year = dic_print.get(year,'th')
                prin_sec = dic_print.get(ord(sec)-dic_sec,'th')
                info.text = "The Receiver is "+str(year)+str(prin_year)+" year "+str(ord(sec)-dic_sec)+str(prin_sec)+" section "+str(gen)+"'s cr."
            except:
                info.text = "[color=#FF0000]Given Receiver is not found in database[/color]"
            mydb.close()

    def prev_wind(self):
        self.parent.parent.current = 'scrn_si'
    def next_wind(self):
        if mytext!="":
            self.parent.parent.parent.ids.scrn_send_mail.children[0].ids.receiver_mail.text = mytext
            self.parent.parent.current = 'scrn_li_msg'
        else:
            info = self.ids.info
            info.text = "[color=#FF0000]You didnot mention the receiver[/color]"
            

class ListenApp(App):
    def build(self):
        return listen_receWindow()

if __name__ =='__main__':
    sa = ListenApp()
    sa.run()