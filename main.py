import tkinter
import tkinter.ttk
import tkinter.messagebox
from tkinter import *


def show():
    progressbarOne['value'] = 0
    progressbarOne['maximum'] = maxbyte
    loading()


def loading():
    global byte
    byte += 200
    progressbarOne['value'] = byte
    if byte < maxbyte:
        progressbarOne.after(100, loading)
    if byte == 200:
        listbox.insert(0, "【提示】正在幫您選擇電腦配備...")
    if byte == 1000:
        listbox.insert(0, "【中央處理器】已選擇完畢...")
    if byte == 2000:
        listbox.insert(0, "【主機板】已選擇完畢...")
    if byte == 3000:
        listbox.insert(0, "【記憶體】已選擇完畢...")
    if byte == 4000:
        listbox.insert(0, "【硬碟】已選擇完畢...")
    if byte == 5000:
        listbox.insert(0, "【顯示卡】已選擇完畢...")
    if byte == 6000:
        listbox.insert(0, "【電源供應器】已選擇完畢...")
    if byte == 7000:
        listbox.insert(0, "【散熱塔散】已選擇完畢...")
    if byte == 8000:
        listbox.insert(0, "【機殼】已選擇完畢...")
    if byte == 9000:
        listbox.insert(0, "【提示】計算 & 輸出中...")
    if byte == 12000:
        tkinter.messagebox.showinfo(
            title='結果', message='您的電腦配備所需金額為：{}元'.format(entry.get()))


root = tkinter.Tk()
root.title('電腦配備估價系統v1.1')
root.geometry('290x295')
root.resizable(width=0, height=0)

byte = 0
maxbyte = 12000

label = tkinter.Label(root, text='請輸入您的購買預算')
label.place(x=84, y=10, width=120, height=25)


entry = tkinter.Entry(root, width=14, justify='center')
entry.insert(0, "0")
entry.place(x=58, y=40)


button = tkinter.Button(root, text='開始', command=show)
button.place(x=173, y=36)

progressbarOne = tkinter.ttk.Progressbar(root, length=210)
progressbarOne.place(x=39, y=75)

var = tkinter.StringVar()
var.set([])

listbox = tkinter.Listbox(root, width=30, listvariable=var)
listbox.place(x=39, y=100)

design = tkinter.Label(root, text='Designed by L.Z.L')
design.place(x=84, y=270)

root.mainloop()
