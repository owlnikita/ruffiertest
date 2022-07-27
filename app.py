from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen 
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.core.window import Window
from rufier import test
from instructions import *
from kivy.core.image import Image
from seconds import *
from sits import *
from runner import *

Window.size = (690,640)


age = 7 
name = ''
p1, p2, p3 = 0, 0, 0

def check_int(str_num):
    try:
        return int(str_num)
    except:
        return False

class InStrScr(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        
        instr = Label(text=txt_instruction)
        lbl1 = Label(text='Введите имя', halign='right')
        self.in_name = TextInput(multiline=False)
        lbl2 = Label(text='Введите возраст', halign='right')  
        self.in_age = TextInput(text='7', multiline=False)
        self.in_age = TextInput(text='7', multiline=False)
        self.btn = Button(text='Начать', size_hint=(.3, .2), pos_hint={'center_x': .5}, background_color=[.5,.1,1,7])
        self.btn.on_press = self.next
        
        line1 = BoxLayout(size_hint=(.8,None),height='30sp')
        line2 = BoxLayout(size_hint=(.8,None),height='30sp')
        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)
        line2.add_widget(lbl2)
        line2.add_widget(self.in_age)
        outer = BoxLayout(orientation='vertical',padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)
        # return Image(texture='imgs/bg.png')

        
    def next(self):
        global name
        name = self.in_name.text
        self.manager.current = 'pulse1'

class PulseScr(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.next_screen = False

        instr = Label(text=txt_test1)

        self.lbl_sec = Seconds(5)
        self.lbl_sec.bind(done=self.sec_finished)

        line = BoxLayout(size_hint=(.8,None),height='30sp')
        lbl_result = Label(text='Введите результат', halign='right')
        self.in_result = TextInput(text='0', multiline=False)
        self.in_result.set_disabled(True)

        line.add_widget(lbl_result)
        line.add_widget(self.in_result)

        self.btn = Button(text='Начать', size_hint=(.3, .2), pos_hint={'center_x': .5}, background_color=[1,.1,5,1])
        self.btn.on_press = self.next

        outer = BoxLayout(orientation='vertical',padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(self.lbl_sec)
        outer.add_widget(line)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    
    def sec_finished(self, *args):
        self.next_screen = True
        self.in_result.set_disabled(False)
        self.btn.set_disabled(False)
        self.btn.text = 'Продолжить'

    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else: 
            global p1
            p1 = check_int(self.in_result.text)
            if p1 == False or p1 <= 0:
                p1 = 0
                self.in_result.text = str(p1)
            else:
                self.manager.current = 'sits'
        # if ok_next == True:
        #     self.manager.current = 'sits'
        #     self.btn.on_press = self.next    

class CheckSits(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.next_screen = False

        instr = Label(text=txt_sits, size_hint=(0.5, 1))
        self.lbl_sits = Sits(5)
        self.run = Runner(total=5, steptime=1.5, size_hint=(0.4, 1))
        self.run.bind(finished=self.run_finished)

        line = BoxLayout()
        vlay = BoxLayout(orientation='vertical', size_hint=(0.3, 1))
        vlay.add_widget(self.lbl_sits)
        line.add_widget(instr)
        line.add_widget(vlay)
        line.add_widget(self.run)

        self.btn = Button(text='Начать', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.background_color = (.5,.4,.4,1)
        self.btn.on_press = self.next

        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(line)
        outer.add_widget(self.btn)

        self.add_widget(outer)

    def run_finished(self, instance, value):
        self.btn.set_disabled(False)
        self.btn.text = 'Продолжить'
        self.next_screen = True

    def next(self):
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.run.start()
            self.run.bind(value=self.lbl_sits.next)
        else:
            self.manager.current = 'pulse2'
        

class PulseScr2(Screen):
    def __init__(self, **kw):
        self.next_screen = False
        self.stage = 0

        super().__init__(**kw)

        instr = Label(text=txt_test3)
        line1 = BoxLayout(size_hint=(.8,None),height='30sp')

        self.lbl_sec = Seconds(15)
        self.lbl_sec.bind(done=self.sec_finished)
        self.lbl1 = Label(text='Считайте пульс')

        lbl_result1 = Label(text='Результат', halign='right')
        self.in_result1 = TextInput(text='0', multiline=False)

        line1.add_widget(lbl_result1)
        line1.add_widget(self.in_result1)

        line2 = BoxLayout(size_hint=(.8,None),height='30sp')
        lbl_result2 = Label(text='Результат после отдыха', halign='right')
        self.in_result2 = TextInput(text='0', multiline=False)

        self.in_result1.set_disabled(True)
        self.in_result2.set_disabled(True)

        line2.add_widget(lbl_result2)
        line2.add_widget(self.in_result2)

        self.btn = Button(text='Начать', size_hint=(.3, .2), pos_hint={'center_x': .5}, background_color=[.9,.3,1,1])
        self.btn.on_press = self.next

        outer = BoxLayout(orientation='vertical',padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(self.lbl1)
        outer.add_widget(self.lbl_sec)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)

    def sec_finished(self, *args):
        if self.lbl_sec.done:
            if self.stage == 0:
                self.stage = 1
                self.lbl1.text = 'Отдыхайте'
                self.lbl_sec.restart(30)
                self.in_result1.set_disabled(False)
            elif self.stage == 1:
                self.stage = 2
                self.lbl1.text = 'Считайте пульс'
                self.lbl_sec.restart(15)
            elif self.stage == 2:
                self.in_result2.set_disabled(False)
                self.btn.set_disabled(False)
                self.btn.text = 'Завершить'
                self.next_screen = True

    def next(self):
        # ok_next = True
        if not self.next_screen:
            self.btn.set_disabled(True)
            self.lbl_sec.start()
        else:
            global p2, p3
            p2 = check_int(self.in_result1.text)
            p3 = check_int(self.in_result2.text)
            if p2 == False:
                p2 = 0
                self.in_result2.text = str(p2)
            elif p3 == False:
                p3 = 0
                self.in_result2.text = str(p3)
            else:
                self.manager.current = 'result'

class Result(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)
        self.outer = BoxLayout(orientation='vertical',padding=8, spacing=8)
        self.instr = Label(text='')
        self.outer.add_widget(self.instr)

        self.add_widget(self.outer)
        self.on_enter = self.before
    def before(self):
        global name 
        self.instr.text = name + '\n' + test(age, p1,p2,p3)

class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InStrScr(name='instr'))
        sm.add_widget(PulseScr(name='pulse1'))
        sm.add_widget(CheckSits(name='sits'))
        sm.add_widget(PulseScr2(name='pulse2'))
        sm.add_widget(Result(name='result'))
        return sm

app = HeartCheck()

if __name__ == '__main__':
    app.run()