"""
USE LOOPS TO CREATE THE BUTTONS!!
I WAS LAZY TO THINK OF A WAY TO DO IT...
SO IF YOU WANT TO MAKE YOUR OWN,
MAKE THE BUTTONS USING LOOPS!!!!!!!!!!!!

You have been advised :D
"""

from tkinter import *
import tkinter as tk
import math


WINDOW_WIDTH = 350
WINDOW_HEIGHT = 500
RESULT_TEXT = ['0']
ANS = ''


class App(Tk):

    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        x_coord = (self.winfo_screenwidth() // 2) - (WINDOW_WIDTH // 2)
        y_coord = (self.winfo_screenheight() // 2) - (WINDOW_HEIGHT // 2)

        self.title('Spalculator v2.0 - by Spimy')
        self.iconbitmap('icon.ico')
        self.geometry('{0}x{1}+{2}+{3}'.format(WINDOW_WIDTH, WINDOW_HEIGHT, x_coord, y_coord))
        self.configure(cursor='@anime.ani')

        container = Frame(self)
        container.pack(side=TOP, fill=BOTH, expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        frame = Main(container, self)
        self.frames[Main] = frame
        frame.grid(row=0, column=0, sticky=NSEW)

        self.show_frame(Main)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class Main(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        self.configure(background='#0f0f0f')

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.checker = ''


        self.result = Label(self, anchor='se', bg='#010101', fg='#f1f1f1', relief=FLAT, height=3, 
                            font=('Consolas', 20), justify='right')
        self.result['text'] = ''.join(RESULT_TEXT)

        self.theme = Button(self, text='Dark', font=('Consolas', 8), relief=FLAT, bg='#0a0a0a', fg='#f1f1f1',
                            command=self.theme_changer)
        self.theme.grid(row=0, column=0, sticky='nw', padx=5, pady=5)

        self.btns = Frame(self)
        # self.btns.grid_rowconfigure(0, weight=1)
        # self.btns.grid_rowconfigure(1, weight=1)
        # self.btns.grid_rowconfigure(2, weight=1)
        self.btns.configure(background='#0f0f0f')
        self.btns.grid_columnconfigure(0, weight=1)
        self.btns.grid_columnconfigure(1, weight=1)
        self.btns.grid_columnconfigure(2, weight=1)
        self.btns.grid_columnconfigure(3, weight=1)

        self.result.grid(row=0, column=0, sticky='new')
        self.btns.grid(row=1, column=0, sticky='nsew')

        self.create_buttons()

        controller.bind('<Return>', self.equate)
        controller.bind('<BackSpace>', self.undof)
        controller.bind('1', self.onef)
        controller.bind('2', self.twof)
        controller.bind('3', self.threef)
        controller.bind('4', self.fourf)
        controller.bind('5', self.fivef)
        controller.bind('6', self.sixf)
        controller.bind('7', self.sevenf)
        controller.bind('8', self.eightf)
        controller.bind('9', self.ninef)
        controller.bind('0', self.zerof)
        controller.bind('+', self.addf)
        controller.bind('-', self.subf)
        controller.bind('*', self.multif)
        controller.bind('/', self.divf)
        controller.bind('t', self.theme_changer)
        controller.bind('p', self.plusminusf)
        controller.bind('.', self.decif)
        controller.bind('<Shift-@>', self.rootf)
        controller.bind('<Escape>', self.cancelf)

    def theme_changer(self, smth=None):
        if self.theme['text'] == 'Dark':
            self.theme.configure(bg='#c9c9c9', fg='#000000', text='Light')
            self.one.configure(bg='#999999', fg='#000000')
            self.two.configure(bg='#999999', fg='#000000')
            self.three.configure(bg='#999999', fg='#000000')
            self.four.configure(bg='#999999', fg='#000000')
            self.five.configure(bg='#999999', fg='#000000')
            self.six.configure(bg='#999999', fg='#000000')
            self.seven.configure(bg='#999999', fg='#000000')
            self.eight.configure(bg='#999999', fg='#000000')
            self.nine.configure(bg='#999999', fg='#000000')
            self.zero.configure(bg='#999999', fg='#000000')
            self.add.configure(bg='#999999', fg='#000000')
            self.sub.configure(bg='#999999', fg='#000000')
            self.plusminus.configure(bg='#999999', fg='#000000')
            self.equal.configure(bg='#999999', fg='#000000')
            self.root.configure(bg='#999999', fg='#000000')
            self.cancel.configure(bg='#999999', fg='#000000')
            self.undo.configure(bg='#999999', fg='#000000')
            self.deci.configure(bg='#999999', fg='#000000')
            self.multi.configure(bg='#999999', fg='#000000')
            self.div.configure(bg='#999999', fg='#000000')
            self.result.configure(bg='#999999', fg='#000000')
            self.btns.configure(background='#e2e2e2')
            self.configure(background='#e2e2e2')
        else:
            self.theme.configure(bg='#0a0a0a', fg='#f1f1f1', text='Dark')
            self.one.configure(bg='#030303', fg='#f1f1f1')
            self.two.configure(bg='#030303', fg='#f1f1f1')
            self.three.configure(bg='#030303', fg='#f1f1f1')
            self.four.configure(bg='#030303', fg='#f1f1f1')
            self.five.configure(bg='#030303', fg='#f1f1f1')
            self.six.configure(bg='#030303', fg='#f1f1f1')
            self.seven.configure(bg='#030303', fg='#f1f1f1')
            self.eight.configure(bg='#030303', fg='#f1f1f1')
            self.nine.configure(bg='#030303', fg='#f1f1f1')
            self.zero.configure(bg='#030303', fg='#f1f1f1')
            self.add.configure(bg='#030303', fg='#f1f1f1')
            self.sub.configure(bg='#030303', fg='#f1f1f1')
            self.plusminus.configure(bg='#030303', fg='#f1f1f1')
            self.equal.configure(bg='#030303', fg='#f1f1f1')
            self.root.configure(bg='#030303', fg='#f1f1f1')
            self.cancel.configure(bg='#030303', fg='#f1f1f1')
            self.undo.configure(bg='#030303', fg='#f1f1f1')
            self.deci.configure(bg='#030303', fg='#f1f1f1')
            self.div.configure(bg='#030303', fg='#f1f1f1')
            self.multi.configure(bg='#030303', fg='#f1f1f1')
            self.result.configure(bg='#030303', fg='#f1f1f1')
            self.btns.configure(background='#0f0f0f')
            self.configure(background='#0f0f0f')

    def create_buttons(self):

        self.one = Button(self.btns, text='1', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.onef)
        self.two = Button(self.btns, text='2', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.twof)
        self.three = Button(self.btns, text='3', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.threef)
        self.four = Button(self.btns, text='4', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.fourf)
        self.five = Button(self.btns, text='5', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.fivef)
        self.six = Button(self.btns, text='6', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.sixf)
        self.seven = Button(self.btns, text='7', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.sevenf)
        self.eight = Button(self.btns, text='8', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.eightf)
        self.nine = Button(self.btns, text='9', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.ninef)
        self.multi = Button(self.btns, text='×', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.multif)
        self.sub = Button(self.btns, text='-', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.subf)
        self.add = Button(self.btns, text='+', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.addf)
        self.zero = Button(self.btns, text='0', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.zerof)
        self.plusminus = Button(self.btns, text='±', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.plusminusf)
        self.deci = Button(self.btns, text=',', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.decif)
        self.equal = Button(self.btns, text='=', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.equate)
        self.cancel = Button(self.btns, text='C', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.cancelf)
        self.root = Button(self.btns, text='√', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.rootf)
        self.undo = Button(self.btns, text='⌫', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.undof)
        self.div = Button(self.btns, text='÷', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.divf)

        self.div.grid(row=1, column=3, sticky='nsew', padx=10, pady=10)
        self.undo.grid(row=1, column=2, sticky='nsew', padx=10, pady=10)
        self.root.grid(row=1, column=1, sticky='nsew', padx=10, pady=10)
        self.cancel.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)
        self.one.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)
        self.two.grid(row=2, column=1, sticky='nsew', padx=10, pady=10)
        self.three.grid(row=2, column=2, sticky='nsew', padx=10, pady=10)
        self.four.grid(row=3, column=0, sticky='nsew', padx=10, pady=10)
        self.five.grid(row=3, column=1, sticky='nsew', padx=10, pady=10)
        self.six.grid(row=3, column=2, sticky='nsew', padx=10, pady=10)
        self.seven.grid(row=4, column=0, sticky='nsew', padx=10, pady=10)
        self.eight.grid(row=4, column=1, sticky='nsew', padx=10, pady=10)
        self.nine.grid(row=4, column=2, sticky='nsew', padx=10, pady=10)
        self.multi.grid(row=2, column=3, sticky='nsew', padx=10, pady=10)
        self.sub.grid(row=3, column=3, sticky='nsew', padx=10, pady=10)
        self.add.grid(row=4, column=3, sticky='nsew', padx=10, pady=10)
        self.plusminus.grid(row=5, column=0, sticky='nsew', padx=10, pady=10)
        self.zero.grid(row=5, column=1, sticky='nsew', padx=10, pady=10)
        self.deci.grid(row=5, column=2, sticky='nsew', padx=10, pady=10)
        self.equal.grid(row=5, column=3, sticky='nsew', padx=10, pady=10)

    def divf(self, smth=None):
        global RESULT_TEXT

        if ''.join(RESULT_TEXT) == '':
            return

        if len(RESULT_TEXT) == 2:
            RESULT_TEXT[1] = '÷'
            self.result['text'] = ''.join(RESULT_TEXT)
            return

        if len(RESULT_TEXT) == 3: 
            self.equate()

        RESULT_TEXT.append('÷')
        self.result['text'] = ''.join(RESULT_TEXT)

    def undof(self, smth=None):
        global RESULT_TEXT

        if len(RESULT_TEXT[0]) == 2 and RESULT_TEXT[0][0] == '-':
            RESULT_TEXT[0] = '0'
            self.result['text'] = ''.join(RESULT_TEXT)
            return

        if len(RESULT_TEXT[0]) == 1:
            RESULT_TEXT[0] = '0'
            self.result['text'] = ''.join(RESULT_TEXT)
            return

        if RESULT_TEXT[-1] == '':
            del RESULT_TEXT[-1]

        minus = RESULT_TEXT[-1][:-1]
        RESULT_TEXT[-1] = minus
        self.result['text'] = ''.join(RESULT_TEXT)

    def rootf(self, smth=None):
        global RESULT_TEXT, ANS

        if len(RESULT_TEXT) < 1: return
        if len(RESULT_TEXT) == 2: 
            
            if RESULT_TEXT[0][0] == '-':
                RESULT_TEXT.append(RESULT_TEXT[0][1::])
            else:
                RESULT_TEXT.append(RESULT_TEXT[0])

            ANS = math.floor(math.sqrt(float(RESULT_TEXT[-1]))) if math.sqrt(float(RESULT_TEXT[-1])).is_integer() else math.sqrt(float(RESULT_TEXT[-1]))
            final_ans = float(RESULT_TEXT[0]) + ANS
            final_ans = math.floor(final_ans) if final_ans.is_integer() else final_ans
            RESULT_TEXT = [str(final_ans)]
            self.checker = 'Ok!'
            self.result['text'] = ''.join(RESULT_TEXT)
            
            return

        try:
            ANS = math.floor(math.sqrt(float(RESULT_TEXT[-1]))) if math.sqrt(float(RESULT_TEXT[-1])).is_integer() else math.sqrt(float(RESULT_TEXT[-1]))
            RESULT_TEXT = [str(ANS)]
            self.checker = 'Ok!'
            self.result['text'] = ''.join(RESULT_TEXT)
        except ValueError:
            self.disablebtns()
            ANS = 'Maths Error'
            RESULT_TEXT = [str(ANS)]
            self.result['text'] = ANS
            return

    def cancelf(self, smth=None):
        global RESULT_TEXT

        RESULT_TEXT = ['0']
        self.result['text'] = ''.join(RESULT_TEXT)

    def onef(self, smth=None):
        global RESULT_TEXT, ANS

        self.enablebtns()
        
        if RESULT_TEXT[-1] == '0':
            RESULT_TEXT[-1] = ''

        if self.checker != '':
            if len(RESULT_TEXT) == 2:
                if RESULT_TEXT[1] in [i for i in ('+', '-', '÷', '×')]:
                    self.checker = ''
                    RESULT_TEXT.append('1')
                    self.result['text'] = ''.join(RESULT_TEXT)
                    return

            RESULT_TEXT = ['']
            self.checker = ''

        if ANS == 'Maths Error':
            ANS = ''
            RESULT_TEXT = ['']

        if RESULT_TEXT[-1] in [i for i in ('+', '-', '÷', '×')]: 
            RESULT_TEXT.append('1')
            self.result['text'] = ''.join(RESULT_TEXT)
            return

        RESULT_TEXT[-1] += '1'
        self.result['text'] = ''.join(RESULT_TEXT)

    def twof(self, smth=None):
        global RESULT_TEXT, ANS

        self.enablebtns()
        
        if RESULT_TEXT[-1] == '0':
            RESULT_TEXT[-1] = ''

        if self.checker != '':
            if len(RESULT_TEXT) == 2:
                if RESULT_TEXT[1] in [i for i in ('+', '-', '÷', '×')]:
                    self.checker = ''
                    RESULT_TEXT.append('2')
                    self.result['text'] = ''.join(RESULT_TEXT)
                    return

        if ANS == 'Maths Error':
            ANS = ''
            RESULT_TEXT = ['']

        if RESULT_TEXT[-1] in [i for i in ('+', '-', '÷', '×')]: 
            RESULT_TEXT.append('2')
            self.result['text'] = ''.join(RESULT_TEXT)
            return

        RESULT_TEXT[-1] += '2'
        self.result['text'] = ''.join(RESULT_TEXT)

    def threef(self, smth=None):
        global RESULT_TEXT, ANS

        self.enablebtns()
        
        if RESULT_TEXT[-1] == '0':
            RESULT_TEXT[-1] = ''

        if self.checker != '':
            if len(RESULT_TEXT) == 2:
                if RESULT_TEXT[1] in [i for i in ('+', '-', '÷', '×')]:
                    self.checker = ''
                    RESULT_TEXT.append('3')
                    self.result['text'] = ''.join(RESULT_TEXT)
                    return

        if ANS == 'Maths Error':
            ANS = ''
            RESULT_TEXT = ['']

        if RESULT_TEXT[-1] in [i for i in ('+', '-', '÷', '×')]: 
            RESULT_TEXT.append('3')
            self.result['text'] = ''.join(RESULT_TEXT)
            return

        RESULT_TEXT[-1] += '3'
        self.result['text'] = ''.join(RESULT_TEXT)

    def fourf(self, smth=None):
        global RESULT_TEXT, ANS
        
        self.enablebtns()

        if RESULT_TEXT[-1] == '0':
            RESULT_TEXT[-1] = ''

        if self.checker != '':
            if len(RESULT_TEXT) == 2:
                if RESULT_TEXT[1] in [i for i in ('+', '-', '÷', '×')]:
                    self.checker = ''
                    RESULT_TEXT.append('4')
                    self.result['text'] = ''.join(RESULT_TEXT)
                    return

        if ANS == 'Maths Error':
            ANS = ''
            RESULT_TEXT = ['']

        if RESULT_TEXT[-1] in [i for i in ('+', '-', '÷', '×')]: 
            RESULT_TEXT.append('4')
            self.result['text'] = ''.join(RESULT_TEXT)
            return
        RESULT_TEXT[-1] += '4'
        self.result['text'] = ''.join(RESULT_TEXT)

    def fivef(self, smth=None):
        global RESULT_TEXT, ANS

        self.enablebtns()

        if RESULT_TEXT[-1] == '0':
            RESULT_TEXT[-1] = ''

        if self.checker != '':
            if len(RESULT_TEXT) == 2:
                if RESULT_TEXT[1] in [i for i in ('+', '-', '÷', '×')]:
                    self.checker = ''
                    RESULT_TEXT.append('5')
                    self.result['text'] = ''.join(RESULT_TEXT)
                    return

        if ANS == 'Maths Error':
            ANS = ''
            RESULT_TEXT = ['']

        if RESULT_TEXT[-1] in [i for i in ('+', '-', '÷', '×')]: 
            RESULT_TEXT.append('5')
            self.result['text'] = ''.join(RESULT_TEXT)
            return
        RESULT_TEXT[-1] += '5'
        self.result['text'] = ''.join(RESULT_TEXT)

    def sixf(self, smth=None):
        global RESULT_TEXT, ANS

        self.enablebtns()

        if RESULT_TEXT[-1] == '0':
            RESULT_TEXT[-1] = ''

        if self.checker != '':
            if len(RESULT_TEXT) == 2:
                if RESULT_TEXT[1] in [i for i in ('+', '-', '÷', '×')]:
                    self.checker = ''
                    RESULT_TEXT.append('6')
                    self.result['text'] = ''.join(RESULT_TEXT)
                    return

        if ANS == 'Maths Error':
            ANS = ''
            RESULT_TEXT = ['']

        if RESULT_TEXT[-1] in [i for i in ('+', '-', '÷', '×')]: 
            RESULT_TEXT.append('6')
            self.result['text'] = ''.join(RESULT_TEXT)
            return
        
        RESULT_TEXT[-1] += '6'
        self.result['text'] = ''.join(RESULT_TEXT)

    def sevenf(self, smth=None):
        global RESULT_TEXT, ANS

        self.enablebtns()

        if RESULT_TEXT[-1] == '0':
            RESULT_TEXT[-1] = ''

        if self.checker != '':
            if len(RESULT_TEXT) == 2:
                if RESULT_TEXT[1] in [i for i in ('+', '-', '÷', '×')]:
                    self.checker = ''
                    RESULT_TEXT.append('7')
                    self.result['text'] = ''.join(RESULT_TEXT)
                    return

        if ANS == 'Maths Error':
            ANS = ''
            RESULT_TEXT = ['']

        if RESULT_TEXT[-1] in [i for i in ('+', '-', '÷', '×')]: 
            RESULT_TEXT.append('7')
            self.result['text'] = ''.join(RESULT_TEXT)
            return

        RESULT_TEXT[-1] += '7'
        self.result['text'] = ''.join(RESULT_TEXT)

    def eightf(self, smth=None):
        global RESULT_TEXT, ANS

        self.enablebtns()

        if RESULT_TEXT[-1] == '0':
            RESULT_TEXT[-1] = ''

        if self.checker != '':
            if len(RESULT_TEXT) == 2:
                if RESULT_TEXT[1] in [i for i in ('+', '-', '÷', '×')]:
                    self.checker = ''
                    RESULT_TEXT.append('8')
                    self.result['text'] = ''.join(RESULT_TEXT)
                    return

        if ANS == 'Maths Error':
            ANS = ''
            RESULT_TEXT = ['']

        if RESULT_TEXT[-1] in [i for i in ('+', '-', '÷', '×')]: 
            RESULT_TEXT.append('8')
            self.result['text'] = ''.join(RESULT_TEXT)
            return

        RESULT_TEXT[-1] += '8'
        self.result['text'] = ''.join(RESULT_TEXT)
    
    def ninef(self, smth=None):
        global RESULT_TEXT, ANS

        self.enablebtns()

        if RESULT_TEXT[-1] == '0':
            RESULT_TEXT[-1] = ''

        if self.checker != '':
            if len(RESULT_TEXT) == 2:
                if RESULT_TEXT[1] in [i for i in ('+', '-', '÷', '×')]:
                    self.checker = ''
                    RESULT_TEXT.append('9')
                    self.result['text'] = ''.join(RESULT_TEXT)
                    return

        if ANS == 'Maths Error':
            ANS = ''
            RESULT_TEXT = ['']

        if RESULT_TEXT[-1] in [i for i in ('+', '-', '÷', '×')]: 
            RESULT_TEXT.append('9')
            self.result['text'] = ''.join(RESULT_TEXT)
            return

        RESULT_TEXT[-1] += '9'
        self.result['text'] = ''.join(RESULT_TEXT)

    def zerof(self, smth=None):
        global RESULT_TEXT, ANS

        self.enablebtns()

        if RESULT_TEXT[-1] == '0':
            RESULT_TEXT[-1] = ''

        if self.checker != '':
            if len(RESULT_TEXT) == 2:
                if RESULT_TEXT[1] in [i for i in ('+', '-', '÷', '×')]:
                    self.checker = ''
                    RESULT_TEXT.append('0')
                    self.result['text'] = ''.join(RESULT_TEXT)
                    return

        if ANS == 'Maths Error':
            ANS = ''
            RESULT_TEXT = ['']

        if RESULT_TEXT[-1] in [i for i in ('+', '-', '÷', '×')]: 
            RESULT_TEXT.append('0')
            self.result['text'] = ''.join(RESULT_TEXT)
            return

        RESULT_TEXT[-1] += '0'
        self.result['text'] = ''.join(RESULT_TEXT)

    def decif(self, smth=None):
        global RESULT_TEXT

        if RESULT_TEXT[-1] not in [i for i in ('+', '-', '÷', '×')] and RESULT_TEXT[-1][-1] == '.':
            return
        
        if RESULT_TEXT[-1] in [i for i in ('+', '-', '÷', '×')]:
            RESULT_TEXT.append('0.')
            self.result['text'] = ''.join(RESULT_TEXT)
            return

        RESULT_TEXT[-1] += '.'
        self.result['text'] = ''.join(RESULT_TEXT)

    def addf(self, smth=None):
        global RESULT_TEXT

        if ''.join(RESULT_TEXT) == '':
            return

        if len(RESULT_TEXT) == 2:
            RESULT_TEXT[1] = '+'
            self.result['text'] = ''.join(RESULT_TEXT)
            return

        if len(RESULT_TEXT) == 3:
            self.equate()

        RESULT_TEXT.append('+')
        self.result['text'] = ''.join(RESULT_TEXT)

    def subf(self, smth=None):
        global RESULT_TEXT

        if ''.join(RESULT_TEXT) == '':
            return

        if len(RESULT_TEXT) == 2:
            RESULT_TEXT[1] = '-'
            self.result['text'] = ''.join(RESULT_TEXT)
            return

        if len(RESULT_TEXT) == 3: 
            self.equate()

        RESULT_TEXT.append('-')
        self.result['text'] = ''.join(RESULT_TEXT)

    def multif(self, smth=None):
        global RESULT_TEXT

        if ''.join(RESULT_TEXT) == '':
            return

        if len(RESULT_TEXT) == 2:
            RESULT_TEXT[1] = '×'
            self.result['text'] = ''.join(RESULT_TEXT)
            return

        if len(RESULT_TEXT) == 3: 
            self.equate()

        RESULT_TEXT.append('×')
        self.result['text'] = ''.join(RESULT_TEXT)

    def plusminusf(self, smth=None):
        global RESULT_TEXT

        if ''.join(RESULT_TEXT) == '':
            RESULT_TEXT[-1] = '-'
            self.result['text'] = ''.join(RESULT_TEXT)
            return

        if RESULT_TEXT[-1] == '0': return

        if RESULT_TEXT[-1][0] == '-':
            RESULT_TEXT[-1] = RESULT_TEXT[-1][1::]
            self.result['text'] = ''.join(RESULT_TEXT)
            return
        else:
            RESULT_TEXT[-1] = '-' + RESULT_TEXT[-1]
            self.result['text'] = ''.join(RESULT_TEXT)
            return
            
    def equate(self, smth=None):
        global RESULT_TEXT, ANS

        if ANS == 'Maths Error':
            ANS = ''
            RESULT_TEXT = ['0']
            self.result['text'] = ''.join(RESULT_TEXT)
            self.enablebtns()

        if len(RESULT_TEXT) < 3: return

        def syms(sym):
            one = float(RESULT_TEXT[0])
            two = float(RESULT_TEXT[2])
            ansdiv = ''

            try:
                ansdiv = one / two
            except ZeroDivisionError:
                ansdiv = 'Maths Error'

            switcher = {
                '+': one + two,
                '-': one - two,
                '×': one * two,
                '÷': ansdiv
            }

            return switcher.get(sym)

        if syms(RESULT_TEXT[1]) == 'Maths Error':
            self.disablebtns()
            ANS = syms(RESULT_TEXT[1])
            RESULT_TEXT = [str(ANS)]
            self.result['text'] = ANS
            return

        ANS = math.floor(syms(RESULT_TEXT[1])) if syms(RESULT_TEXT[1]).is_integer() else syms(RESULT_TEXT[1])
        RESULT_TEXT = [str(ANS)]
        self.checker = 'Ok!'
        self.result['text'] = ANS

    def disablebtns(self):
        self.div.config(state='disabled')
        self.undo.config(state='disabled')
        self.root.config(state='disabled')
        self.cancel.config(state='disabled')
        self.multi.config(state='disabled')
        self.sub.config(state='disabled')
        self.add.config(state='disabled')
        self.plusminus.config(state='disabled')
        self.deci.config(state='disabled')

    def enablebtns(self):
        self.div.config(state='normal')
        self.undo.config(state='normal')
        self.root.config(state='normal')
        self.cancel.config(state='normal')
        self.multi.config(state='normal')
        self.sub.config(state='normal')
        self.add.config(state='normal')
        self.plusminus.config(state='normal')
        self.deci.config(state='normal')


def loadapp():
    app = App()
    app.mainloop()


if __name__ == '__main__':
    loadapp()
