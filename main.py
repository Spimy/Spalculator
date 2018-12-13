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

        self.title('Spalculator v1.0 - by Spimy')
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

        self.result = Label(self, anchor='se', bg='#010101', fg='#f1f1f1', relief=FLAT, height=3, 
                       font=('Consolas', 20), justify='right')
        self.result['text'] = ''.join(RESULT_TEXT)
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

    def create_buttons(self):

        self.one = Button(self.btns, text='1', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.one)
        self.two = Button(self.btns, text='2', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.two)
        self.three = Button(self.btns, text='3', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.three)
        self.four = Button(self.btns, text='4', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.four)
        self.five = Button(self.btns, text='5', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.five)
        self.six = Button(self.btns, text='6', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.six)
        self.seven = Button(self.btns, text='7', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.seven)
        self.eight = Button(self.btns, text='8', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.eight)
        self.nine = Button(self.btns, text='9', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.nine)
        self.multi = Button(self.btns, text='×', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.multi)
        self.sub = Button(self.btns, text='-', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.sub)
        self.add = Button(self.btns, text='+', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.add)
        self.zero = Button(self.btns, text='0', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.zero)
        self.plusminus = Button(self.btns, text='±', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.plusminus)
        self.deci = Button(self.btns, text=',', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.deci)
        self.equal = Button(self.btns, text='=', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.equate)
        self.cancel = Button(self.btns, text='CE', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.cancel)
        self.root = Button(self.btns, text='√', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.root)
        self.undo = Button(self.btns, text='⌫', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.undo)
        self.div = Button(self.btns, text='÷', relief=FLAT, font=('Consolas', 15), width=2, height=2, bg='#030303', fg='#f1f1f1', command=self.div)

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

    def div(self):
        global RESULT_TEXT

        if ''.join(RESULT_TEXT) == '':
            return

        if len(RESULT_TEXT) == 3: 
            self.equate()

        RESULT_TEXT.append('÷')
        self.result['text'] = ''.join(RESULT_TEXT)

    def undo(self):
        global RESULT_TEXT

        if len(RESULT_TEXT[0]) == 1:
            RESULT_TEXT[0] = '0'
            self.result['text'] = ''.join(RESULT_TEXT)
            return

        if RESULT_TEXT[-1] == '':
            del RESULT_TEXT[-1]

        minus = RESULT_TEXT[-1][:-1]
        RESULT_TEXT[-1] = minus
        self.result['text'] = ''.join(RESULT_TEXT)

    def root(self):
        global RESULT_TEXT, ANS

        if len(RESULT_TEXT) < 1: return

        ANS = math.floor(math.sqrt(float(RESULT_TEXT[0]))) if math.sqrt(float(RESULT_TEXT[0])).is_integer() else math.sqrt(float(RESULT_TEXT[0]))
        RESULT_TEXT = [str(ANS)]
        self.result['text'] = ''.join(RESULT_TEXT)

    def cancel(self):
        global RESULT_TEXT

        RESULT_TEXT = ['0']
        self.result['text'] = ''.join(RESULT_TEXT)

    def one(self):
        global RESULT_TEXT, ANS

        self.enablebtns()
        
        if RESULT_TEXT[-1] == '0':
            RESULT_TEXT[-1] = ''

        if ANS != '' and RESULT_TEXT[-1] not in [i for i in ('+', '-', '÷', '×')]:
            ANS = ''
            RESULT_TEXT = ['']

        if RESULT_TEXT[-1] in [i for i in ('+', '-', '÷', '×')]: 
            RESULT_TEXT.append('1')
            self.result['text'] = ''.join(RESULT_TEXT)
            return

        RESULT_TEXT[-1] += '1'
        self.result['text'] = ''.join(RESULT_TEXT)

    def two(self):
        global RESULT_TEXT, ANS

        self.enablebtns()
        
        if RESULT_TEXT[-1] == '0':
            RESULT_TEXT[-1] = ''

        if ANS != '' and RESULT_TEXT[-1] not in [i for i in ('+', '-', '÷', '×')]:
            ANS = ''
            RESULT_TEXT = ['']

        if RESULT_TEXT[-1] in [i for i in ('+', '-', '÷', '×')]: 
            RESULT_TEXT.append('2')
            self.result['text'] = ''.join(RESULT_TEXT)
            return

        RESULT_TEXT[-1] += '2'
        self.result['text'] = ''.join(RESULT_TEXT)

    def three(self):
        global RESULT_TEXT, ANS

        self.enablebtns()
        
        if RESULT_TEXT[-1] == '0':
            RESULT_TEXT[-1] = ''

        if ANS != '' and RESULT_TEXT[-1] not in [i for i in ('+', '-', '÷', '×')]:
            ANS = ''
            RESULT_TEXT = ['']

        if RESULT_TEXT[-1] in [i for i in ('+', '-', '÷', '×')]: 
            RESULT_TEXT.append('3')
            self.result['text'] = ''.join(RESULT_TEXT)
            return

        RESULT_TEXT[-1] += '3'
        self.result['text'] = ''.join(RESULT_TEXT)

    def four(self):
        global RESULT_TEXT, ANS
        
        self.enablebtns()

        if RESULT_TEXT[-1] == '0':
            RESULT_TEXT[-1] = ''

        if ANS != '' and RESULT_TEXT[-1] not in [i for i in ('+', '-', '÷', '×')]:
            ANS = ''
            RESULT_TEXT = ['']

        if RESULT_TEXT[-1] in [i for i in ('+', '-', '÷', '×')]: 
            RESULT_TEXT.append('4')
            self.result['text'] = ''.join(RESULT_TEXT)
            return
        RESULT_TEXT[-1] += '4'
        self.result['text'] = ''.join(RESULT_TEXT)

    def five(self):
        global RESULT_TEXT, ANS

        self.enablebtns()

        if RESULT_TEXT[-1] == '0':
            RESULT_TEXT[-1] = ''

        if ANS != '' and RESULT_TEXT[-1] not in [i for i in ('+', '-', '÷', '×')]:
            ANS = ''
            RESULT_TEXT = ['']

        if RESULT_TEXT[-1] in [i for i in ('+', '-', '÷', '×')]: 
            RESULT_TEXT.append('5')
            self.result['text'] = ''.join(RESULT_TEXT)
            return
        RESULT_TEXT[-1] += '5'
        self.result['text'] = ''.join(RESULT_TEXT)

    def six(self):
        global RESULT_TEXT, ANS

        self.enablebtns()

        if RESULT_TEXT[-1] == '0':
            RESULT_TEXT[-1] = ''

        if ANS != '' and RESULT_TEXT[-1] not in [i for i in ('+', '-', '÷', '×')]:
            ANS = ''
            RESULT_TEXT = ['']

        if RESULT_TEXT[-1] in [i for i in ('+', '-', '÷', '×')]: 
            RESULT_TEXT.append('6')
            self.result['text'] = ''.join(RESULT_TEXT)
            return
        
        RESULT_TEXT[-1] += '6'
        self.result['text'] = ''.join(RESULT_TEXT)

    def seven(self):
        global RESULT_TEXT, ANS

        self.enablebtns()

        if RESULT_TEXT[-1] == '0':
            RESULT_TEXT[-1] = ''

        if ANS != '' and RESULT_TEXT[-1] not in [i for i in ('+', '-', '÷', '×')]:
            ANS = ''
            RESULT_TEXT = ['']

        if RESULT_TEXT[-1] in [i for i in ('+', '-', '÷', '×')]: 
            RESULT_TEXT.append('7')
            self.result['text'] = ''.join(RESULT_TEXT)
            return

        RESULT_TEXT[-1] += '7'
        self.result['text'] = ''.join(RESULT_TEXT)

    def eight(self):
        global RESULT_TEXT, ANS

        self.enablebtns()

        if RESULT_TEXT[-1] == '0':
            RESULT_TEXT[-1] = ''

        if ANS != '' and RESULT_TEXT[-1] not in [i for i in ('+', '-', '÷', '×')]:
            ANS = ''
            RESULT_TEXT = ['']

        if RESULT_TEXT[-1] in [i for i in ('+', '-', '÷', '×')]: 
            RESULT_TEXT.append('8')
            self.result['text'] = ''.join(RESULT_TEXT)
            return

        RESULT_TEXT[-1] += '8'
        self.result['text'] = ''.join(RESULT_TEXT)
    
    def nine(self):
        global RESULT_TEXT, ANS

        self.enablebtns()

        if RESULT_TEXT[-1] == '0':
            RESULT_TEXT[-1] = ''

        if ANS != '' and RESULT_TEXT[-1] not in [i for i in ('+', '-', '÷', '×')]:
            ANS = ''
            RESULT_TEXT = ['']

        if RESULT_TEXT[-1] in [i for i in ('+', '-', '÷', '×')]: 
            RESULT_TEXT.append('9')
            self.result['text'] = ''.join(RESULT_TEXT)
            return

        RESULT_TEXT[-1] += '9'
        self.result['text'] = ''.join(RESULT_TEXT)

    def zero(self):
        global RESULT_TEXT, ANS

        self.enablebtns()

        if RESULT_TEXT[-1] == '0':
            RESULT_TEXT[-1] = ''

        if ANS != '' and RESULT_TEXT[-1] not in [i for i in ('+', '-', '÷', '×')]:
            ANS = ''
            RESULT_TEXT = ['']

        if RESULT_TEXT[-1] in [i for i in ('+', '-', '÷', '×')]: 
            RESULT_TEXT.append('0')
            self.result['text'] = ''.join(RESULT_TEXT)
            return

        RESULT_TEXT[-1] += '0'
        self.result['text'] = ''.join(RESULT_TEXT)

    def deci(self):
        global RESULT_TEXT
        RESULT_TEXT[-1] += '.'
        self.result['text'] = ''.join(RESULT_TEXT)

    def add(self):
        global RESULT_TEXT

        if ''.join(RESULT_TEXT) == '':
            return

        if len(RESULT_TEXT) == 3: 
            self.equate()

        RESULT_TEXT.append('+')
        self.result['text'] = ''.join(RESULT_TEXT)

    def sub(self):
        global RESULT_TEXT

        if ''.join(RESULT_TEXT) == '':
            return

        if len(RESULT_TEXT) == 3: 
            self.equate()

        RESULT_TEXT.append('-')
        self.result['text'] = ''.join(RESULT_TEXT)

    def multi(self):
        global RESULT_TEXT

        if ''.join(RESULT_TEXT) == '':
            return

        if len(RESULT_TEXT) == 3: 
            self.equate()

        RESULT_TEXT.append('×')
        self.result['text'] = ''.join(RESULT_TEXT)

    def plusminus(self):
        global RESULT_TEXT

        if ''.join(RESULT_TEXT) == '':
            RESULT_TEXT[-1] = '-'
            self.result['text'] = ''.join(RESULT_TEXT)
            return

        if RESULT_TEXT[-1] == '0': return

        for i in range(len(RESULT_TEXT)):

            if RESULT_TEXT[i] in [j for j in ('+', '-', '×')]: continue
            if RESULT_TEXT[i] == '÷': continue

            if RESULT_TEXT[i][0] == '-':
                RESULT_TEXT[i] = RESULT_TEXT[i][1::]
                self.result['text'] = ''.join(RESULT_TEXT)
                continue
            else:
                RESULT_TEXT[i] = '-' + RESULT_TEXT[i]
                self.result['text'] = ''.join(RESULT_TEXT)
                continue
            
    def equate(self):
        global RESULT_TEXT, ANS

        if ANS == 'Cannot Divide By Zero':
            ANS = ''
            RESULT_TEXT = ['0']
            self.result['text'] = ''.join(RESULT_TEXT)
            self.enablebtns()

        if len(RESULT_TEXT) < 3: return

        def syms(sym):
            one = float(RESULT_TEXT[0])
            two = float(RESULT_TEXT[2])
            ans = ''

            try:
                ans = one / two
            except ZeroDivisionError:
                ans = 'Cannot Divide By Zero'

            switcher = {
                '+': one + two,
                '-': one - two,
                '×': one * two,
                '÷': ans,
                '√': math.sqrt(one)
            }

            return switcher.get(sym)

        if syms(RESULT_TEXT[1]) == 'Cannot Divide By Zero':
            self.disablebtns()
            ANS = syms(RESULT_TEXT[1])
            RESULT_TEXT = [str(ANS)]
            self.result['text'] = ANS
            return

        ANS = math.floor(syms(RESULT_TEXT[1])) if syms(RESULT_TEXT[1]).is_integer() else syms(RESULT_TEXT[1])
        RESULT_TEXT = [str(ANS)]
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
